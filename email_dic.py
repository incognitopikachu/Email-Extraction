import re

f = open("sample.txt", 'r')
file_text = f.read()
f.close()

pattern = "\w+@(\w+(\.\w+)*)"
domain_list = re.findall(pattern, file_text)

domain_dic = {}

for domain in domain_list:
    if domain[0] in domain_dic:
        domain_dic[domain[0]] = domain_dic[domain[0]] + 1
    else:
        domain_dic[domain[0]] = 1


print(domain_dic)
