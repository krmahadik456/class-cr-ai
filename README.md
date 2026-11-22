# Class CR AI Assistant API

## The Problem
College Class Representatives (CRs) receive hundreds of messages from students regarding various issues (Wi-Fi, Mess food, Lab equipment). It is impossible for a CR to manually read and forward every complaint to the right department.

## The Solution
This FastAPI backend acts as a smart complaint portal. When a student submits a complaint, the API uses a pre-trained NLP model (via Hugging Face Transformers) to **automatically classify** the text into departments like "IT and Wi-Fi", "Hostel and Mess", "Academics", or "Maintenance". 

## Tech Stack
*   **Backend:** Python, FastAPI
*   **Database:** SQLite, SQLModel
*   **AI/NLP:** Hugging Face `transformers` (Zero-Shot Classification)

## How to Run
1. Install dependencies:
   `pip install fastapi "uvicorn[standard]" sqlmodel transformers torch`
2. Run the server:
   `uvicorn main:app --reload`
3. Open `http://127.0.0.1:8000/docs` to test the AI.