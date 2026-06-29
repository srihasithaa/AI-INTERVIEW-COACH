from resume_analyzer import analyze_resume
from job_role_analyzer import analyze_job_role
from comparison import compare_resume_job
from interview_planner import interview_planner, display_concepts
from question_generator import generate_questions, display_questions

user_resume = "resume/sample_resume.txt"
resume_prompt = "prompts/resume_prompt.txt"

user_job_role = "AI/ML or LLM Engineer"
job_prompt = "prompts/job_role_prompt.txt"

planner_prompt = "prompts/interview_planner_prompt.txt"

question_prompt = "prompts/question_prompt.txt"

resume_analysis = analyze_resume(user_resume, resume_prompt)

job_analysis = analyze_job_role(user_job_role, job_prompt)

comparison_analysis = compare_resume_job(resume_analysis, job_analysis)

interview_plan = interview_planner(comparison_analysis, planner_prompt)
display_concepts(interview_plan)

while True:
    user_concept = int(input("Choose a concept: "))
    if 1 <= user_concept <= len(interview_plan["recommended_concepts"]):
        break
    print("Invalid choice. Please choose a valid concept number.")
chosen_concept = interview_plan["recommended_concepts"][user_concept - 1]["concept"]

user_difficulty = input("Choose a difficulty: ").lower()
while user_difficulty not in ["easy", "medium", "hard"]:
    print("Invalid difficulty.")
    user_difficulty = input("Choose Easy, Medium or Hard: ").lower()

while True:
    user_number_of_questions = int(input("How many questions? "))
    if user_number_of_questions > 0:
        break
    print("Please enter a positive number.")

questions = generate_questions(user_job_role, chosen_concept, user_difficulty, user_number_of_questions,
                               question_prompt)
display_questions(questions)
