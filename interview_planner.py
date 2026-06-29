from model_processing import llm_analysis
import json

def get_interview_prompt(prompt_file):
    with open(prompt_file, "r") as prompt:
        prompt_text=prompt.read()

    return prompt_text

def interview_planner(comparison, prompt):
    prompt_template=get_interview_prompt(prompt)

    model_prompt=(f"Instructions:{prompt_template}\n"
                    f"Comparison of job and resume: {comparison}")

    response = llm_analysis(model_prompt, "gemma3:4b")

    clean_response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    final_response = json.loads(clean_response)

    return final_response

def display_concepts(concepts_dictionary):
    print("Recommended Interview Topics:\n")

    for index, concept in enumerate(concepts_dictionary["recommended_concepts"], start=1):
        print(f"{index}. {concept['concept']}")