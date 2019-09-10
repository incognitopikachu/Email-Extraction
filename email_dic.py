import re
from bs4 import BeautifulSoup
import urllib.request

f = open("sample.txt", 'r')
file_text = f.read()
f.close()

link = "http://www.ex-parrot.com/pdw/Mail-RFC822-Address/Mail-RFC822-Address.html"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, "html.parser")
file_text = str(soup)


pattern = "\w+@(\w+([\.|-]\w+)*)"
domain_list = re.findall(pattern, file_text)

dic = {}

for domain in domain_list:
    # print(domain[0])
    if domain[0].split('.')[0] in dic:
        dic[domain[0].split('.')[0]] = 1 + dic[domain[0].split('.')[0]]
    else:
        dic[domain[0].split('.')[0]] = 1


def PrintMostCommon(mydict, count = 10, freq = 0):
    k = 0
    for key, value in sorted(mydict.items(), key=lambda item: item[1], reverse = True):
        if k < count and value > freq:
            print("%s: %s" % (key, value))
        k = k + 1


# PrintMostCommon(domain_dic)
user_input = input("Minimum frequency: ")
freq = int(user_input)
PrintMostCommon(dic, len(dic.keys()), freq)
