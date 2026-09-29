import os
import boto3
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("AWS_REGION")
KB_ID = os.getenv("KNOWLEDGE_BASE_ID")
MODEL_ID = os.getenv("MODEL_ID")


# Bedrock Knowledge Base client
kb_client = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)


# Bedrock Runtime client
runtime_client = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)


def check_guardrail(text):

    response = runtime_client.apply_guardrail(
        guardrailIdentifier=os.getenv("GUARDRAIL_ID"),
        guardrailVersion=os.getenv("GUARDRAIL_VERSION"),
        source="INPUT",
        content=[
            {
                "text": {
                    "text": text
                }
            }
        ]
    )

    return response


def retrieve_documents(question):

    response = kb_client.retrieve(
        knowledgeBaseId=KB_ID,
        retrievalQuery={
            "text": question
        },
        retrievalConfiguration={
            "vectorSearchConfiguration": {
                "numberOfResults": 5
            }
        }
    )

    return response.get("retrievalResults", [])


def build_context(results):

    context_parts = []

    for index, result in enumerate(results, start=1):

        text = result.get(
            "content",
            {}
        ).get(
            "text",
            ""
        )

        if text:

            context_parts.append(
                f"Source {index}:\n{text}"
            )

    return "\n\n".join(context_parts)


def generate_answer(question, context):

    prompt = f"""
You are an Enterprise Architecture Knowledge Assistant.

Answer the user's question using ONLY the supplied enterprise
knowledge.

Rules:

1. Do not invent company policies.
2. If the supplied knowledge does not contain the answer,
   say:
   "The available enterprise knowledge does not specify this."
3. Keep the answer clear and concise.
4. Explain which source supports the answer where possible.

ENTERPRISE KNOWLEDGE:

{context}

USER QUESTION:

{question}
"""

    response = runtime_client.converse(
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
        ],

        inferenceConfig={
            "temperature": 0.1,
            "maxTokens": 700
        }
    )

    return response["output"]["message"]["content"][0]["text"]


# --------------------------------------------------
# MAIN APPLICATION FLOW
# --------------------------------------------------

question = input("\nAsk a question: ")


# 1. Guardrail check
guardrail_response = check_guardrail(question)

action = guardrail_response.get("action")

print("\nGuardrail action:", action)


# 2. Stop if guardrail blocks request
if action == "GUARDRAIL_INTERVENED":

    print("\nREQUEST BLOCKED")

    print(
        "This request was blocked by the enterprise AI security policy."
    )


# 3. Otherwise continue to RAG
else:

    print("\nRequest allowed.")

    print("Searching enterprise knowledge...")


    # Retrieve documents
    results = retrieve_documents(question)


    # Build context
    context = build_context(results)


    # Generate answer
    answer = generate_answer(
        question,
        context
    )


    print("\nANSWER\n")
    print(answer)


    print("\nRETRIEVED SOURCES")

    for index, result in enumerate(
        results,
        start=1
    ):

        print(
            f"\n{index}. Score: {result.get('score')}"
        )

        print(
            result.get("location")
        )