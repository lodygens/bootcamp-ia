# Week1

## Installation 
- Virtual env
```
python3 -m venv .  
source bin/acticate
```

- Librairies
```
pip3 install torch torchvision tensorflow flax transformers pytorch-transformers openai
````
- Test installation
```
python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"
```

## Configuration

Save openai api key to openaikey

```
cat openaikey >> .gitignore
export OPENAI_API_KEY=`cat openaikey`
```

## Exercices

Located in __src__ directory

## Weekend project

We have three versions
- ./project/openai-ferran-gpt.py by @Dani    (zAspwz)
- ./project/openai-french-chef.py by @oleglod#0001    (nVKpoe)
- ./Montenegrin-AI/Chef by @Perper.net Ivan    (jQ5gT7)


