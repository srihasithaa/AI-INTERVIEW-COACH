from ollama import chat


def llm_analysis(prompt, llm_model):
    response = chat(
        model=llm_model,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return response.message.content
