from model_processing import llm_analysis
import json


def get_question_prompt(prompt_file):
    with open(prompt_file, "r") as prompt:
        prompt_text = prompt.read()

    return prompt_text


def generate_questions(job_role, concept, difficulty, number_of_questions, prompt):
    prompt_template = get_question_prompt(prompt)

    model_prompt = (f"Instructions: {prompt_template}\n"
                    f"Concept: {concept}\n"
                    f"Number of questions: {number_of_questions}\n"
                    f"Difficulty Level: {difficulty}\n"
                    f"Job Role: {job_role}")

    response = llm_analysis(model_prompt, "gemma3:4b")

    clean_response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    final_response = json.loads(clean_response)

    return final_response


def display_questions(questions_dictionary):
    for question in questions_dictionary["questions"]:
        print(f"Question {question['question_number']}:\n"
              f"{question['question']}\n")
