import re

textRaw = r'\r\n$500 per week\n                    '
resultRaw = re.search(r'\$[ \w]*', textRaw)

result = re.search(r'\$(\d+)([ \w]+)', textRaw)
resultNumber = result[1]
resultText = result[2].strip()
print(resultNumber)
print(resultText)