import streamlit as st
import json
from agent_loop import run_agent

st.set_page_config(page_title="Guided Component Architect", layout="centered")

st.title("🧠 Guided Component Architect")
st.markdown("Generate governed Angular components using a strict design system.")

# Load design system
with open("design_system.json") as f:
    design_system = json.load(f)

# Input field
user_prompt = st.text_area(
    "Describe your Angular component",
    placeholder="A login card with a glassmorphism effect..."
)

if st.button("Generate Component"):

    if not user_prompt.strip():
        st.warning("Please enter a component description.")
    else:
        with st.spinner("Running agentic generation + validation loop..."):
            final_code = run_agent(user_prompt, design_system)

        st.success("Component Generated Successfully!")

        st.subheader("Generated Angular Component")
        st.code(final_code, language="typescript")

        st.download_button(
            label="Download as .ts file",
            data=final_code,
            file_name="generated-component.ts",
            mime="text/plain"
        )