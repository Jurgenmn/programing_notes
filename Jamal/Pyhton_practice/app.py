#python -m venv env
#./env/Scripts/activate.bat

import requests

result = requests.get("https://jamal.netlify.com")

print(result.status_code)
print(result.text)

file = open("Jamal.html", "w")
file.write(result.text)

