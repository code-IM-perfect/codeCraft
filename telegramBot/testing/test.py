import re

txt = "230456 23046284"
x = re.findall("\d\d\d\d\d\d\d\d|\d\d\d\d\d\d", txt)


print(x)