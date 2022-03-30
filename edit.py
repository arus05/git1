import re
from collections import defaultdict

s = "12345678"
b = re.findall(r"(\d)(?:\d)(\d)",s)
print(b)
print(s)
