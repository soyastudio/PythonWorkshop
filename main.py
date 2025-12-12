from openai import OpenAI

client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)