from openai import OpenAI
import os

def call_ai(resume_text, job_description, prompt):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "Simulation Mode: AI not connected."

    try:
        client = OpenAI(api_key=api_key)

        final_prompt = (
            prompt +
            "\n\nJob Description:\n" + job_description +
            "\n\nResume:\n" + resume_text
        )

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=final_prompt
        )

        return response.output_text

    except Exception:
        return "Simulation Mode: AI quota unavailable."
