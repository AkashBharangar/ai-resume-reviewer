import json
from prompts import RESUME_REVIEW_PROMPT
from groq import Groq
from config import GROQ_API_KEY


class ResumeReviewer:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def review_resume(self, resume_text: str):

        prompt = RESUME_REVIEW_PROMPT.format(
            resume = resume_text
        )
        
        response = self.client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"system",
                    "content":"You are an experienced resume reviewer. Review in 1 line"
                },
                {
                    "role":"user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        answer = response.choices[0].message.content
        return json.loads(answer)