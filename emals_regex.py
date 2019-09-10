import re

f = open("sample.txt", 'r')
file_text = f.read()
f.close()

pattern = "\w+@softwire.com"

matchList = re.findall(pattern, file_text)

print("No. matches: " + str(len(matchList)))
print(matchList)