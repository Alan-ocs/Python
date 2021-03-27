import re
import webbrowser

shakes = open("KaSolutionChat.txt", "r")

for line in shakes:
    if re.match("(.*)linkedin(.*)*", line):
        webbrowser.open(line, new = 2)
        print(line)

