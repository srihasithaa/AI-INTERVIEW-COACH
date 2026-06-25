from resume_analyzer import analyze_resume
from job_role_analyzer import analyze_job_role

user_resume = "resume/sample_resume.txt"
resume_prompt = "prompts/resume_prompt.txt"

user_job_role="AI/ML or LLM Engineer"
job_prompt="prompts/job_role_prompt.txt"

resume_analysis=analyze_resume(user_resume, resume_prompt)

job_analysis=analyze_job_role(user_job_role,job_prompt)

print(f'{resume_analysis["technical_skills"]}\n {job_analysis["technical_skills"]}')
print(f'{resume_analysis["programming_languages"]}\n {job_analysis["programming_languages"]}')
print(f'{resume_analysis["tools"]}\n {job_analysis["tools"]}')


