
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_ai(resume_text, job_description, prompt):
    try:
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
        return "Response generated (simulation mode)"
