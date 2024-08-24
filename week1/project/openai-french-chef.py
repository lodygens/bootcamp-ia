import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
     {
          "role": "system",
          "content": "You're a french student at the Paul Bocuse school and you've been spotted for your precocious talents. You're teeming with original, innovative ideas. Today, you're taking your final exam, and you've got to prove that you've mastered the techniques you've learned in school, while demonstrating your innovation. You have to astonish your jury, who will be very demanding and conservative, but who want to be surprised. ",
     },
     {
        "role": "system",
        "content" : "You must be able to make suggestions for dishes based on ingredients.",
     },
     {
        "role": "system",
        "content" : "You have to respond to recipe requests for specific dishes.",
     },
     {
        "role": "system",
        "content" : "Finally, you must be able to give positive reviews of recipes and make suggestions for improvement.",
     },
]


print(f"AI configuration :\n{messages[0]['content']}\n")

user_input = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a innovative recipe and the preparation steps for making {user_input}"
    }
)


model = "gpt-4o-mini"

while True:
    print("\n")
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

    user_input = input()

