import re
from collections import defaultdict

s = "1234567"
b = re.findall(r"(\d)(?:\d)(\d)",s)
print(b)
print(s)
