

def CountEmails():
    counter = 0
    for i in range(0, len(file_text)):
        if (file_text[i: i + 13] == '@softwire.com'):
            counter = counter + 1
    print("No. email addresses: " + str(counter))


f = open("sample.txt", 'r')
file_text = f.read()
f.close()
# print(file_text)

text_list = file_text.split()
email_list = []

for word in text_list:
    for i in range(0, len(word)):
        if (word[i: i + 13] == '@softwire.com'):
            email_list.append(word)

print(email_list)