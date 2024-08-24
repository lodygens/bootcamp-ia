from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification


pipelineLabel="sentiment-analysis"
prompt="hugging face is marvelous"
print("example: ", pipelineLabel)
print("prompt = " , prompt)

modelName = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(modelName)
tokenizer = AutoTokenizer.from_pretrained(modelName)
classifier = pipeline(pipelineLabel, model=model, tokenizer=tokenizer, device="mps")
res = classifier(prompt)
print(res)


res=tokenizer(prompt)
print(res)

tokens=tokenizer.tokenize(prompt)
print("tokens")
print(tokens)

ids=tokenizer.convert_tokens_to_ids(tokens)
print("ids")
print(ids)

decoded_str = tokenizer.decode(ids)
print("decoded string")
print(decoded_str)

