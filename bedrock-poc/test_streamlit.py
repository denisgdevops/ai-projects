import streamlit as st

st.set_page_config(
    page_title="Bedrock Test",
    page_icon="🤖"
)

st.title("AWS Bedrock POC")

st.success("Streamlit is working correctly.")

st.write("If you can see this, the Streamlit UI is healthy.")

question = st.chat_input("Ask me something...")

if question:
    st.write(f"You asked: {question}")