from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from typing import Iterable

def main():
  load_dotenv()
  client = OpenAI()

  # Which model we want the AI Chef to use
  MODEL = "gpt-4o-mini"

  # Read all the recipes that we saved in the file, so that the Chef can use them
  with open('recipes.txt', 'r') as recipes_file:
    recipes = recipes_file.read()

  messages: Iterable[ChatCompletionMessageParam] = [
    {
      "role": "system",
      "content": f"""
        You are a Montenegrin AI Chef. You should only respond about the recipes you know. If you don't know the recipe, say so, don't make it up.
        These are the types of requests you allow:
        1. If the user gives lists you some ingredient, give them a list of names of the recipes that contain those ingredient. Just the name, don't give any details.
        2. If the user tells you a dish name, provide a detailed recipe.
        3. If the users suggests a recipe or asks for improvements for one, even if you don't know it, offer a constructive critique with suggested improvements.
        If the user asks anything else, explain that it's outside your scope, and what you are able to do.

        These are the recipes you know:
        {recipes}
      """,
    }
  ]

  while True:
    user_input = input("(Type \"exit\" to stop) Ask the AI Chef: ")

    if user_input == "exit":
      break

    messages.append(
      {
        "role": "user",
        "content": user_input,
      }
    )

    stream = client.chat.completions.create(
      model=MODEL,
      messages=messages,
      stream=True,
    )

    collected_messages = []
    for chunk in stream:
      chunk_message = chunk.choices[0].delta.content or ""
      print(chunk_message, end="")
      collected_messages.append(chunk_message)

    print('\n')

    messages.append(
      {
        "role": "assistant",
        "content": "".join(collected_messages)
      }
    )
  
  print("Thanks for using our AI Chef!")

# Check if we're running as the main file
if __name__ == "__main__":
  main()
