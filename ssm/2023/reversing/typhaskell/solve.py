#!/usr/bin/env python3
import sympy
import sys
import string

def split_into_sections(string):
    sections = []
    current_section = []
    open_parentheses = 0

    for char in string:
        if char == '(':
            open_parentheses += 1
            current_section.append(char)
        elif char == ')':
            open_parentheses -= 1
            current_section.append(char)
            if open_parentheses == 0:
                sections.append(''.join(current_section))
                current_section = []
        elif open_parentheses > 0:
            current_section.append(char)
        elif char.strip():
            sections.append(char)

    return sections


op_map = {
    'PAdd': '+',
    'PMul': '*',
    'PEq': '='
}

alpha = "_" + string.ascii_lowercase + string.digits

lines = []
with open("./challenge.hs", "r") as f:
    
    for line in f:
        line = line.strip()

        if line[:11] == "instance (P" and "Apply" in line:
            lines.append(line)


flag: str = ""

for line in lines:
    line = line.removeprefix("instance ")
    line = line.split(' =>')[0]

    parts = line.split(', ')

    # print(f"{parts = }")

    symbols = dict()
    eq = []

    for part in parts:
        op, args = part.split(' ', 1)

        op = op.strip('()')
        
        args = args.strip('')
        args = split_into_sections(args)

        # print(f"{op = }")
        # print(f"{args = }")

        a, b, c = args

        if op != 'PEq':
            if a[0] == '(':
                a = a.count('S')

            if b[0] == '(':
                b = b.count('S')
            
            if c[0] == '(':
                c = c.count('S')

            if isinstance(a, str):
                if not a in symbols:
                    symbols[a] = sympy.Symbol(a)
                A = symbols[a]
            else:
                A = a

            if isinstance(b, str):
                if not b in symbols:
                    symbols[b] = sympy.Symbol(b)
                B = symbols[b]
            else:
                B = b

            if isinstance(c, str):
                if not c in symbols:
                    symbols[c] = sympy.Symbol(c)
                C = symbols[c]
            else:
                C = c

            if op == 'PAdd':
                eq.append(A + B - C)
            else:
                eq.append(A * B - C)

            # print(f"{a} {op_map[op]} {b} = {c}")
        else:
            if a[0] == '(':
                a = a.count('S')

            if b[0] == '(':
                b = b.count('S')
            

            if isinstance(a, str):
                if not a in symbols:
                    symbols[a] = sympy.Symbol(a)
                A = symbols[a]
            else:
                A = a

            if isinstance(b, str):
                if not b in symbols:
                    symbols[b] = sympy.Symbol(b)
                B = symbols[b]
            else:
                B = b


            eq.append(A - B)

            # print(f"{a} = {b}")

    ans = sympy.nonlinsolve(eq, list(symbols.values()))

    # print(f"{ans = }")

    # print(f"{list(ans) = }")

    xdx = list(symbols.values()).index(symbols['x'])

    # print(f"{xdx = }")

    x = list(ans)[0][xdx]

    # print(f"{x = }")

    flag += alpha[x]
    # print(f"{alpha[x] = }")

print(f"SSM{{{flag}}}")
