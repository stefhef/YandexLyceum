import requests


url = f"{input()}:{input()}"
params = {"a": input(), "b": input()}
data = requests.get(url, params=params).json()

print(*sorted(data['result']))
print(data["check"])