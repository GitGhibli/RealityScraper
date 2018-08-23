import re

textRaw = r'\r\n$500 per week\n                    '
resultRaw = re.search(r'\$[ \w]*', textRaw)
print(resultRaw[0])