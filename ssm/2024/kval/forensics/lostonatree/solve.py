#!/usr/bin/env python3
# degrees: tuple[int]
# xor: tuple[int]
# flag_bits: tuple[str]

with open("./tree.txt", "r") as f:
    degrees = eval(f"tuple({f.readline()})")
    xor = eval(f"tuple({f.readline()})")
    flag_bits = eval(f"tuple({f.readline()})")

# print(f"{degrees = }")
# print(f"{xor = }")
# print(f"{flag_bits = }")

n = len(degrees)

# nodes: list[tuple[int, int, int, str]]
nodes = [tuple((i, j, k, l)) for i, j, k, l in zip(tuple(range(n)), degrees, xor, flag_bits)]

# nodes.sort(key = lambda x: x[1])

# print(f"{nodes = }")

# adj: list[list[int]]
adj = [[] for _ in range(n)]

while nodes:
    node = nodes.pop(0)

    curr_xor = 0
    for i in adj[node[0]]: curr_xor ^= i

    if node[1] == len(adj[node[0]]) + 1:
        new_edge = node[2] ^ curr_xor
        adj[node[0]].append(new_edge)
        adj[new_edge].append(node[0])
        # print(f"{adj = }")
    elif node[1] == len(adj[node[0]]):
        pass
    else:
        nodes.append(node)
    
# print(f"{adj = }")

for nei in adj:
    nei.sort(reverse = True) 

flagIdx = 0
visited = [0] * n

# Recover the flag by retracing the post-dfs
def squirrelWalk(curr):

    global flagIdx

    for nei in adj[curr]:
        if not visited[nei]:
            visited[nei] = 1
            squirrelWalk(nei)

    print(flag_bits[curr], end="")

    flagIdx += 1

visited[0] = 1

squirrelWalk(0)
print()

