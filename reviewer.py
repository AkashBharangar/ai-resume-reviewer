import json
from prompts import (
    RESUME_REVIEW_PROMPT,
    RESUME_REWRITE_PROMPT
)
from groq import Groq
from config import GROQ_API_KEY


class ResumeReviewer:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def review_resume(self, resume_text: str, job_description: str):

        prompt = RESUME_REVIEW_PROMPT.format(
            resume = resume_text,
            job_description=job_description
        )
        
        response = self.client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"system",
                    "content":"You are an expert ATS resume writer."
                },
                {
                    "role":"user",
                    "content": prompt
                }
            ],
            temperature=0
        )
        return json.loads(response.choices[0].message.content)
    
    def rewrite_resume(self, resume_text, job_description):

        prompt = RESUME_REWRITE_PROMPT.format(
            resume=resume_text,
            job_description=job_description
        )

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert ATS resume writer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return json.loads(response.choices[0].message.content)