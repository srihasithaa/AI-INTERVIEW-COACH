from model_processing import llm_analysis
import json


def read_resume(file):
    with open(file, "r") as resume:
        details = resume.read()

    return details


def get_prompt(prompt_file):
    with open(prompt_file, "r") as prompt:
        prompt_text = prompt.read()

    return prompt_text


def analyze_resume(resume, prompt):
    resume_text = read_resume(resume)
    prompt_template = get_prompt(prompt)

    model_prompt = (f"Instructions:{prompt_template}\n"
                    f"Resume:{resume_text}")

    response = llm_analysis(model_prompt, "gemma3:4b")

    clean_response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    final_response = json.loads(clean_response)

    return final_response