from openai import OpenAI
import json
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_component(user_prompt, design_system):
    system_prompt = f"""
You are an Angular code generator.

CRITICAL OUTPUT RULES:
- Output ONLY raw Angular TypeScript component code.
- Do NOT include markdown.
- Do NOT include triple backticks.
- Do NOT include explanations.
- Start directly with: import {{ Component }}

STRICT DESIGN SYSTEM:
You MUST use ONLY the following design tokens.
Do not invent colors.
Do not use Tailwind default colors like bg-indigo-600.

Design Tokens:
{json.dumps(design_system, indent=2)}

Use inline styles referencing these tokens.
"""
    response = client.chat.completions.create(
       model="openai/gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content