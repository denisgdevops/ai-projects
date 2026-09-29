import boto3
import time

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

model_id = "amazon.nova-lite-v1:0"

messages = [
    {
        "role": "user",
        "content": [
            {
                "text": "Explain Amazon Bedrock using a restaurant analogy."
            }
        ]
    }
]

start = time.time()

response = client.converse(
    modelId=model_id,
    messages=messages,
    inferenceConfig={
        "temperature": 0.2,
        "topP": 0.9,
        "maxTokens": 1000
    }
)

end = time.time()

latency_ms = (end - start) * 1000

text = response["output"]["message"]["content"][0]["text"]
usage = response["usage"]

print("\n--- RESPONSE ---")
print(text)

print("\n--- METRICS ---")
print("Input tokens :", usage["inputTokens"])
print("Output tokens:", usage["outputTokens"])
print("Total tokens :", usage["totalTokens"])
print(f"Latency      : {latency_ms:.0f} ms")
