from transformers import pipeline


pipelineLabel="text-generation"
modelLabel="distilgpt2"
prompt="In this course we will teach you how to"
print("example: ", pipelineLabel, modelLabel)
print("prompt = " , prompt)

generator = pipeline(pipelineLabel, model=modelLabel)
res = generator(prompt, max_length=30, num_return_sequences=2)
print(res)
