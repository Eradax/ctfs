#!/usr/bin/env python3
import requests
import re

r = requests.get("http://188.126.67.132:50021/")

p1 = re.search(r"SSM{[a-zA-Z\d:_]*", r.text).group(0)

# print(f"{p1 = }")

r = requests.get("http://188.126.67.132:50021/x.mp3")

p2 = re.search(r"}[a-zA-Z\d:_]*", r.headers["X-flag"][::-1]).group(0)[::-1]

# print(f"{p2 = }")

print(p1 + p2)

