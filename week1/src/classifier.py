from transformers import pipeline


pipelineLabel="zero-shot-classification"
prompt="This is a course on computer science"
print("example: ", pipelineLabel)
print("prompt = " , prompt)

classifier = pipeline(pipelineLabel )
res = classifier(
    prompt, 
    ["education", "politics", "business"]
)

print(res)
