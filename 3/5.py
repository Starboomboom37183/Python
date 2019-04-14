# -*- coding: utf-8 -*-
import re
Rule = "(=\s*?){"
c0 = re.compile(Rule)
input = open("Dijkstra.c","r")
lines = input.read()
input.close()
count = 0
end = 0
place = 0
output = open("Dijkstra.c","w")
while True:
    match = c0.search(lines,place)
    if not match:
        break
    start = match.end()
    i = start-1
    while i < len(lines):
        if lines[i] == "{":
            if count == 0:
                start = end = i
            count += 1
        elif lines[i] == "}":
            if count == 0:
                break
            count -= 1
            if count == 0:
                end = i + 1
                temp = lines[start:end].splitlines()
                if len(temp) > 1:
                    print(temp)
                    pos = lines.rfind("\n", 0, start)
                    for k in range(start + 1, end):
                        if lines[k] != " ":
                            break
                    tab_num = len(re.findall("\t", lines[pos:k]))
                    length = k - pos - 1+3*tab_num
                    line_replace = ""
                    temp[0] = temp[0][1:]
                    for i in range(0, len(temp)):
                        temp[i] = " " * length + temp[i].lstrip()
                    for s in temp:
                        line_replace = line_replace + s + "\n"
                    lines = lines[:start+1]+"\n"+ line_replace.rstrip() + lines[end:]
                    i = start+1 + len(line_replace) + 1
                    print(lines[pos:i])
                    break

        i += 1

    place = i


output.write(lines)
output.close()

