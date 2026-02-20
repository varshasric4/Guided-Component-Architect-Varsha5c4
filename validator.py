import re


def validate_tokens(code: str, design_system: dict):
    """
    Ensures required design tokens are present in the generated code.
    """
    errors = []

    if design_system["primary_color"] not in code:
        errors.append("Primary color not used.")

    if design_system["secondary_color"] not in code:
        errors.append("Secondary color not used.")

    if design_system["border_radius"] not in code:
        errors.append("Border radius not used.")

    if design_system["font_family"] not in code:
        errors.append("Font family not used.")

    return errors


def validate_syntax(code: str):
    """
    Basic structural validation.
    Not a full AST parser — lightweight safety check.
    """
    errors = []

    if code.count("{") != code.count("}"):
        errors.append("Mismatched curly brackets.")

    if code.count("(") != code.count(")"):
        errors.append("Mismatched parentheses.")

    if code.count("<") != code.count(">"):
        errors.append("Mismatched angle brackets.")

    if "export class" not in code:
        errors.append("Missing Angular component class export.")

    return errors


def detect_unauthorized_colors(code: str, design_system: dict):
    """
    Detect any HEX color not defined in design system.
    """
    hex_colors = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", code)

    allowed_colors = {
        design_system["primary_color"],
        design_system["secondary_color"]
    }

    errors = []

    for color in hex_colors:
        if color not in allowed_colors:
            errors.append(f"Unauthorized HEX color used: {color}")

    return errors


def detect_tailwind_color_classes(code: str):
    """
    Prevent usage of default Tailwind color classes like:
    bg-indigo-600, text-gray-500, border-red-300, etc.
    Forces strict design token usage.
    """
    pattern = r"(bg|text|border)-(red|blue|green|gray|yellow|indigo|purple|pink)-\d{2,3}"
    matches = re.findall(pattern, code)

    errors = []

    if matches:
        errors.append("Unauthorized Tailwind color classes detected.")

    return errors