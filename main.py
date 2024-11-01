from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from google.generativeai import GenerativeModel

# Configure Gemini API (replace with your API key)
genai.configure(api_key="AIzaSyDkAfPr2MhxSVfHE39ZDfPUzSiIq7Bktbo")
model = GenerativeModel("gemini-1.5-flash")  # Replace with your preferred Gemini model version

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


async def get_creative_response() -> str:
    try:
        response = model.generate_content(
            f"tell me a random fun fortune",
        )
        return response.text.strip()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to generate response")

@app.get("/generate-fortune")
async def generate_fortune():
    response_text = await get_creative_response()
    return {"response": response_text}