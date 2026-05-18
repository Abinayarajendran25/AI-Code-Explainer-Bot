import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyAQDavS5j3c2UpYmLQqY_gSaKeGS3OwxD8")


model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Code Explainer Bot")

st.title("💻 AI Code Explainer Bot")

st.write("Paste your code and get AI explanation.")


code = st.text_area("Enter your code here", height=300)

if st.button("Explain Code"):

    if code.strip() == "":
        st.warning("Please enter code.")
    else:

        prompt = f"""
        Explain this code in simple words.
        Give:
        1. Overall purpose
        2. Line-by-line explanation
        3. Possible improvements

        Code:
        {code}
        """

        response = model.generate_content(prompt)

        st.subheader("Explanation")
        st.write(response.text)
