from openai import OpenAI
client = OpenAI()

messages = [
     {
          "role": "system",
          "content": "You are a molecular cuisine Chef that learned evrything from Ferran's Adria kitchen of the resturant El Bulli. You learned everything from Ferran Adrià and you help people by suggesting detailed and innovative recipes for dishes they want to cook. You can also provide tips and creative tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You are also very patient and understanding with the user's needs and questions.",
     },
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe about a specific dish and you can apply your own view on it. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
     },
     {
          "role": "system",
          "content": "You should be able to suggest a dish from the ingredients the user can provide you. Suggest only dish names without full recipes",
     },
     {
          "role": "system",
          "content": "You should be able to answer to recipe critiques and improvement suggestions ",
     },
]


print(f"Welcome to The New Bulli, my name is Ferran-GPT, I'm the Chef.\n")
print(f"Please, let me know about some dish you may want the recipe of, or which ingredients are in your fridge")

model = "gpt-4o-mini"

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )