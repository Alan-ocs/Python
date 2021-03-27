import re
import webbrowser

linkedin = open("KaSolutionChat.txt", "r")

for contatos in linkedin:
    if re.match("(.*)linkedin(.*)*", contatos):
        webbrowser.open(contatos, new = 2)
        print(contatos)
