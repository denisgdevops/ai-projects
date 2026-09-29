import os
import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION")
)

text = input("Enter text to evaluate: ")

response = client.apply_guardrail(

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

print("\nAction:")
print(response["action"])

print("\nAssessment:")
print(response.get("assessments"))

print("\nOutputs:")
print(response.get("outputs"))