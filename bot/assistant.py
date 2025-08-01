import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_ai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except:
        return "AI Assistant not available."
