import json

with open('scoring.json') as file:
    data = json.load(file)

sum_all = 0

for i, elem in enumerate(data['scoring']):
    p = data["scoring"][i]["points"]
    n = len(data["scoring"][i]["required_tests"])
    subgroup_count = 0
    for j in range(n):
        verdict = input()
        if verdict == 'ok':
            subgroup_count += 1
    sum_all += p * subgroup_count // n

print(sum_all)
