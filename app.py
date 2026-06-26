from reviewer import ResumeReviewer
from parser import extract_text

text = input("Enter:")

resume_text = extract_text(text)

reviewer = ResumeReviewer()

response = reviewer.review_resume(resume_text)

print(f"ATS Score: {response['ats_score']}")

print("\nMissing Keywords:")
for keyword in response["missing_keywords"]:
    print(f"- {keyword}")

print("\nSuggestions:")
for suggestion in response["suggestions"]:
    print(f"- {suggestion}")