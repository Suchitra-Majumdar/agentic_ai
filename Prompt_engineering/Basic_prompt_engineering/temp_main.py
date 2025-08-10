from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model = "gpt-4.1-mini-2025-04-14",
    input = """Wrtie a poem 'Amader chhoto nodi'  in bengali in englist letters"""

)
with open("bengali_response.txt", "w") as f:
    f.write(response.output_text)


