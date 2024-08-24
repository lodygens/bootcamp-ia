import torch
from pytorch_transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
text = "Welcome to the open data science conference it is"
indexed_tokens = tokenizer.encode(text)
print(indexed_tokens)

tokens_tensor = torch.tensor([indexed_tokens])
print(tokens_tensor)

model = GPT2LMHeadModel.from_pretrained('gpt2')
model.eval()
print(model)

print("Using mps which is Apple only; otherwise, yous should try cuda")
tokens_tensor = tokens_tensor.to('mps')
model.to('mps')

with torch.no_grad():
    outputs = model(tokens_tensor)
    predictions = outputs[0]
    print(predictions.shape)
    predicted_index = torch.argmax(predictions[0, -1, :]).item()
    predicted_text = tokenizer.decode(indexed_tokens + [predicted_index])
    print(predicted_text)

start = 'Natural Language Processing is slowly becoming'
indexed_tokens = tokenizer.encode(start)

for i in range(75):
  tokens_tensor = torch.tensor([indexed_tokens])
  tokens_tensor = tokens_tensor.to('mps')
  with torch.no_grad():
    outputs = model(tokens_tensor)
    predictions = outputs[0]
    predicted_index = torch.argmax(predictions[0, -1, :]).item()
    indexed_tokens = indexed_tokens + [predicted_index]
    predicted_text = tokenizer.decode(indexed_tokens + [predicted_index])
    print(predicted_text)
