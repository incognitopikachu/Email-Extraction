import re

f = open("sample.txt", 'r')
file_text = f.read()
f.close()
# [A-Za-z0-9\.'%\+-]
pattern = "\w+@(\w+(\.\w+)*)"
domain_list = re.findall(pattern, file_text)

domain_dic = {}
dic={}
for domain in domain_list:
    # print(domain[0])
    if domain[0] in domain_dic:
        domain_dic[domain[0]] = domain_dic[domain[0]] + 1

    else:
        domain_dic[domain[0]] = 1



for domain in domain_list:
    # print(domain[0])
    if domain[0].split('.')[0] in dic:
        dic[domain[0].split('.')[0]] = 1 + dic[domain[0].split('.')[0]]
    else:
        dic[domain[0].split('.')[0]] = 1
print(dic)
print(domain_dic)

def PrintMostCommon(mydict, count = 10, freq = 0):
    k = 0
    for key, value in sorted(mydict.items(), key=lambda item: item[1], reverse = True):
        if k < count and value > freq:
            print("%s: %s" % (key, value))
        k = k + 1


# print(domain_dic)
# PrintMostCommon(domain_dic)

# user_input = input("Minimum frequency: ")
# freq = int(user_input)
# PrintMostCommon(dic, len(domain_dic.keys()), freq)
