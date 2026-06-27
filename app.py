from reviewer import ResumeReviewer
from parser import extract_text, extract_job_description

text = input("Enter:")

resume_text = extract_text(text)

job_description = extract_job_description("job_descriptions/sample_jd.txt")

reviewer = ResumeReviewer()

response = reviewer.review_resume(resume_text, job_description)
print(response)

print(f"ATS Score: {response['ats_score']}")
print(f"Match Score: {response['match_score']}")

print("\nMatching Keywords:")
for keyword in response["matching_keywords"]:
    print("-", keyword)

print("\nMissing Keywords:")
for keyword in response["missing_keywords"]:
    print("-", keyword)

print("\nSuggestions:")
for suggestion in response["suggestions"]:
    print("-", suggestion)