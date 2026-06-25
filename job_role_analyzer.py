from model_processing import llm_analysis
import json

def get_job_prompt(prompt_file):
    with open(prompt_file, "r") as prompt:
        prompt_text=prompt.read()

    return prompt_text

def analyze_job_role(job_role, prompt):
    prompt_template=get_job_prompt(prompt)

    model_prompt=(f"Instructions:{prompt_template}\n"
                    f"Job Role:{job_role}")

    response = llm_analysis(model_prompt, "gemma3:4b")

    clean_response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    final_response = json.loads(clean_response)

    return final_response

