RESUME_REVIEW_PROMPT = """
You are an experienced ATS (Applicant Tracking System) and technical recruiter.

Analyze the following resume and return your analysis in the specified JSON format.

Resume:
--------------------
{resume}
--------------------

Return ONLY valid JSON in the following format:

{{
    "ats_score": <integer>,
    "match score": <interger>,
    "missing_keywords": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}

Rules:
- ATS score must be between 0 and 100.
- Suggestions should be specific and actionable.
- Do not include markdown.
- Do not wrap the JSON inside ```json.
- Return only the JSON object.
"""




RESUME_REWRITE_PROMPT = """
You are an expert resume writer.

Rewrite the following resume to better match the provided job description.

Resume:
--------------------
{resume}
--------------------

Job Description:
--------------------
{job_description}
--------------------

Return ONLY valid JSON in this format:

{{
    "professional_summary": "",
    "technical_skills": [],
    "work_experience": "",
    "projects": "",
    "additional_suggestions": []
}}

Do not hallucinate experience.
Do not invent projects.
Only improve wording, organization, and ATS optimization.
Return ONLY valid JSON.
Do NOT wrap the JSON inside ```json or ```.
Do NOT include any explanation before or after the JSON.
"""