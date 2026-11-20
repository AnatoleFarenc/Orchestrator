from openai import OpenAI


with OpenAI(
    base_url="https://openrouter.ai/api/v1/"
) as client:
    response = client.responses.create(
        model="baidu/ernie-5.5-flash-preview:free",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    print(response.output_text)
