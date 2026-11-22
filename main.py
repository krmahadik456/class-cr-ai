from fastapi import FastAPI, HTTPException
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel
from transformers import pipeline

# ==========================================
# 🧠 THE AI MAGIC (Hugging Face)
# ==========================================
# This downloads a free, pre-trained AI model. 
# It takes any text and matches it to the categories we give it.
print("Loading AI Model... please wait (only takes a moment)...")
classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-distilroberta-base")

# Our predefined categories for a college
CATEGORIES = ["IT and Wi-Fi", "Hostel and Mess", "Academics", "Maintenance"]

# ==========================================
# 📊 DATABASE MODELS
# ==========================================
class Complaint(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    student_name: str
    complaint_text: str
    ai_category: str # This will be filled by the AI

# This is what the student sends us
class ComplaintCreate(BaseModel):
    student_name: str
    complaint_text: str

sqlite_url = "sqlite:///campus.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

app = FastAPI(title="Class CR AI Assistant")

# ==========================================
# 🛣️ API ENDPOINTS
# ==========================================

@app.post("/complaints")
def submit_complaint(payload: ComplaintCreate):
    if len(payload.complaint_text) < 5:
        raise HTTPException(status_code=400, detail="Complaint is too short.")

    # 1. Ask the AI to categorize the text
    ai_result = classifier(payload.complaint_text, candidate_labels=CATEGORIES)
    
    # The AI returns a list of scores. We grab the one with the highest score.
    best_category = ai_result['labels'][0]

    # 2. Save to the database
    new_complaint = Complaint(
        student_name=payload.student_name,
        complaint_text=payload.complaint_text,
        ai_category=best_category
    )

    with Session(engine) as session:
        session.add(new_complaint)
        session.commit()
        session.refresh(new_complaint)

    # 3. Return the result to the CR
    return {
        "message": "Complaint submitted and auto-sorted by AI!",
        "data": new_complaint
    }

@app.get("/complaints")
def get_all_complaints(category: str = None):
    with Session(engine) as session:
        # If the CR searches for a specific category (like ?category=IT and Wi-Fi)
        if category:
            complaints = session.exec(select(Complaint).where(Complaint.ai_category == category)).all()
        else:
            # Otherwise, show all complaints
            complaints = session.exec(select(Complaint)).all()
        return complaints