from generator import generate_component
from validator import (
    validate_tokens,
    validate_syntax,
    detect_unauthorized_colors,
    detect_tailwind_color_classes
)


def clean_code(code: str):
    """
    Removes markdown wrappers if LLM accidentally includes them.
    """
    code = code.replace("```typescript", "")
    code = code.replace("```ts", "")
    code = code.replace("```", "")
    return code.strip()


def run_agent(user_prompt: str, design_system: dict, max_retries: int = 2):
    """
    Agentic self-correction loop:
    1. Generate
    2. Validate
    3. Retry with error feedback if needed
    """

    for attempt in range(max_retries):
        print(f"\n--- Attempt {attempt + 1} ---")

        code = generate_component(user_prompt, design_system)
        code = clean_code(code)

        # Run all validators
        token_errors = validate_tokens(code, design_system)
        syntax_errors = validate_syntax(code)
        color_errors = detect_unauthorized_colors(code, design_system)
        tailwind_errors = detect_tailwind_color_classes(code)

        errors = (
            token_errors +
            syntax_errors +
            color_errors +
            tailwind_errors
        )

        if not errors:
            print("Validation passed.")
            return code

        print("Validation failed with errors:")
        for err in errors:
            print(f"- {err}")

        # Self-correction prompt injection
        user_prompt = f"""
You generated an Angular component that failed validation.

Errors:
{errors}

Fix the component so that:
- It strictly uses ONLY the provided design tokens.
- No Tailwind default color classes are used.
- Syntax issues are corrected.
- Output raw Angular TypeScript code only.
- No markdown.

Previous Code:
{code}
"""

    print("\nMax retries reached. Returning last attempt.")
    return code