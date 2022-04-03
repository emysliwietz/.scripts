#!/bin/python3

content = ""
with open("/home/user/.config/i3/config") as f:
    content = f.read()

sets = {}
for line in content.splitlines():
    if line.startswith("set"):
        line = line.split(" ")
        sets[line[1]] = " ".join(line[2:]).strip()



for a in sets:
    print(sets[a])
    content = content.replace(a, sets[a])
        
        
parsed_content = ""
# parse all bindsyms (this does not handle bindcodes, as I do not use them and don't see a reason why one should)
for line in content.splitlines():
    if line.startswith("bindsym"):
        line = line.strip()[8:]
        line = line.replace("\t", " ")
        keys = line.split(" ")[0]
        command = " ".join(line.split(" ")[1:]).strip()

        keys = keys.replace("Mod4", "win")
        keys = keys.replace("Return", "Enter")
        keys = keys.replace("+", " ")
        keys = keys.replace("odiaeresis", "oe")
        keys = keys.replace("adiaeresis", "ae")
        keys = keys.replace("udiaeresis", "ue")
        keys = keys.replace("KP_Add", "num_plus")
        keys = keys.replace("KP_Multiply", "num_times")
        keys = keys.replace("KP_Subtract", "num_minus")
        keys = keys.replace("KP_Divide", "num_div")
        keys = keys.replace("period", ".")
        keys = keys.replace("minus", "-")
        keys = keys.replace("num_-", "num_minus")
        keys = keys.replace("comma", ",")
        keys = keys.replace("KP_Insert", "num_0")
        keys = keys.replace("KP_End", "num_1")
        keys = keys.replace("KP_Down", "num_2")
        keys = keys.replace("KP_Next", "num_3")
        keys = keys.replace("KP_Left", "num_4")
        keys = keys.replace("KP_Begin", "num_5")
        keys = keys.replace("KP_Right", "num_6")
        keys = keys.replace("KP_Home", "num_7")
        keys = keys.replace("KP_Up", "num_8")
        keys = keys.replace("KP_Prior", "num_9")
        keys = keys.replace("print", "b_print")

        parsed_content += (keys + ": " + command) + "\n"

with open("/tmp/testkeys", "w") as f:
    f.write(parsed_content)

