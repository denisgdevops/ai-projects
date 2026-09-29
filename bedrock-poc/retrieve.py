import os
import boto3
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("AWS_REGION")
KB_ID = os.getenv("KNOWLEDGE_BASE_ID")

client = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)

question = "What authentication standard should external APIs use?"

response = client.retrieve(
    knowledgeBaseId=KB_ID,
    retrievalQuery={
        "text": question
    },
    retrievalConfiguration={
        "managedSearchConfiguration": {
            "numberOfResults": 5
        }
    }
)

results = response.get("retrievalResults", [])

print(f"\nQuestion: {question}")
print(f"Retrieved results: {len(results)}")

for index, result in enumerate(results, start=1):

    print("\n" + "=" * 70)
    print(f"RESULT {index}")

    print("\nScore:")
    print(result.get("score"))

    print("\nContent:")
    print(result.get("content", {}).get("text"))

    print("\nLocation:")
    print(result.get("location"))
