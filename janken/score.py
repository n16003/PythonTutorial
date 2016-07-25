import json
x = {}
with open("score.txt", "r") as f:
    x = json.load(f)

print(x)