# Class CR AI Assistant API

An AI-powered complaint management backend built using Python, FastAPI, SQLModel, and Hugging Face Transformers.

## Problem Statement

In colleges, Class Representatives (CRs) often receive complaints from students regarding different issues, including:

- Internet and Wi-Fi connectivity.
- Hostel and mess facilities.
- Academic concerns.
- Maintenance problems.

When complaints arrive through informal messages, manually reading and categorising each issue can become time-consuming.

This project explores how Natural Language Processing (NLP) can help organise student complaints by automatically identifying their likely categories.

## Solution

Class CR AI Assistant API provides a backend service where students can submit complaints.

The application uses a pre-trained zero-shot classification model from Hugging Face Transformers to analyse complaint text and assign it to one of four predefined categories.

The complaint and its predicted category are then stored in an SQLite database.

## Tech Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLModel
- **AI / NLP:** Hugging Face Transformers
- **Model:** cross-encoder/nli-distilroberta-base
- **Classification:** Zero-shot classification
- **API Documentation:** Swagger UI / OpenAPI

## Features

### 1. Complaint Submission
Students can submit complaints using an API endpoint.

### 2. AI-Based Classification
The application analyses submitted complaint text and predicts the most relevant category.

### 3. Predefined Categories

The current classification categories are:

- IT and Wi-Fi
- Hostel and Mess
- Academics
- Maintenance

### 4. Database Storage
The application stores:
- Complaint ID.
- Student name.
- Complaint text.
- AI-predicted category.

### 5. Complaint Retrieval
The CR can retrieve all complaints or filter complaints using a specific category.

## How It Works

1. A student submits a complaint.
2. FastAPI receives the request.
3. The complaint text is passed to the Hugging Face classification pipeline.
4. The model compares the text against predefined categories.
5. The highest-ranked category is selected.
6. The complaint and predicted category are stored in SQLite.
7. The API returns the stored complaint information.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/complaints` | Submit and classify a complaint |
| GET | `/complaints` | Retrieve all complaints |
| GET | `/complaints?category=Academics` | Filter complaints by category |

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/krmahadik456/class-cr-ai.git
cd class-cr-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Linux / macOS:
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi "uvicorn[standard]" sqlmodel transformers torch
```

The Hugging Face model will be downloaded when the application starts for the first time.

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Open API documentation

Visit:

http://127.0.0.1:8000/docs

## Future Improvements

- Student and CR authentication.
- Role-based access control.
- Complaint status tracking.
- Department assignment.
- Classification confidence scores.
- Manual category correction.
- PostgreSQL integration.
- Automated API testing using Pytest.
- Docker containerization and deployment.

## Project Status

Beginner-level AI-integrated backend project demonstrating REST API development, NLP-based text classification, database integration, and automated complaint categorisation.

## Author

Kaustubh Mahadik

GitHub: https://github.com/krmahadik456
