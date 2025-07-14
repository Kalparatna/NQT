import re

x = "[^a-zA-ZO-9]"
matcher = re.finditer(x,"afddfs@#$32")
for match in matcher:
    print(match.start(),"...", match.group())
    