import os
import boto3
import streamlit as st

from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
KNOWLEDGE_BASE_ID = os.getenv("KNOWLEDGE_BASE_ID")
MODEL_ID = os.getenv(
    "MODEL_ID",
    "amazon.nova-lite-v1:0"
)


kb_client = boto3.client(
    "bedrock-agent-runtime",
    region_name=AWS_REGION
)

model_client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION
)


st.set_page_config(
    page_title="Architecture Knowledge Assistant",
    page_icon="🏗️"
)

st.title("Enterprise Architecture Knowledge Assistant")

st.caption(
    "Ask questions about the architecture standards "
    "loaded into Amazon Bedrock."
)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


question = st.chat_input(
    "Ask about architecture standards..."
)


if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        try:

            retrieve_response = kb_client.retrieve(
                knowledgeBaseId=KNOWLEDGE_BASE_ID,
                retrievalQuery={
                    "text": question
                },
                retrievalConfiguration={
                    "managedSearchConfiguration": {
                        "numberOfResults": 5
                    }
                }
            )

            chunks = []

            for result in retrieve_response.get(
                "retrievalResults",
                []
            ):

                text = result.get(
                    "content",
                    {}
                ).get(
                    "text",
                    ""
                )

                if text:
                    chunks.append(text)


            if not chunks:

                answer = (
                    "I could not find relevant information "
                    "in the knowledge base."
                )

            else:

                context = "\n\n".join(chunks)

                prompt = f"""
You are an Enterprise Architecture Knowledge Assistant.

Use only the provided context to answer the question.

If the information is not available in the context,
state that clearly.

Context:
{context}

Question:
{question}
"""

                model_response = model_client.converse(
                    modelId=MODEL_ID,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "text": prompt
                                }
                            ]
                        }
                    ]
                )

                answer = (
                    model_response
                    ["output"]
                    ["message"]
                    ["content"][0]
                    ["text"]
                )


            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })


        except Exception as e:

            st.error(f"AWS Bedrock error: {e}")