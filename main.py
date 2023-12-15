# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

app = firebase_admin.initialize_app()
db = firestore.client()
app = FastAPI()

cred = credentials.Certificate('path/to/serviceAccount.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity; update as needed for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

class MeetingData(BaseModel):
    ToplantiKonusu: str
    Tarih: str
    BaslangicSaati: str
    BitisSaati: str
    Katilimcilar: list

@app.post("/register-meeting")
def submit_meeting_data(meeting_data: MeetingData):

    print("Meeting Data Received:")
    print(meeting_data.dict())

    return {"message": "Meeting data received successfully!"}
