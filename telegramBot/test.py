import re

txt = "23045678"
x = re.findall("\d\d\d\d\d\d|\d\d\d", txt)


print(x)