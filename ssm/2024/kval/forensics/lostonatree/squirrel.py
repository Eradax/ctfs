#!/usr/bin/env python3

FLAG = "SSM{yay}"

# Adjacency list for Chungus' neighborhood
edges = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6]]

n = len(edges)

degrees = [len(adjs) for adjs in edges]

def XORadjs(adjs):
    temp = 0
    for x in adjs:
        temp ^= x
    return temp

XOR = [XORadjs(adjs) for adjs in edges]

# Sort the adjacency list according to Chungus' preference
for nei in edges:
    nei.sort(reverse = True) 

flagIdx = 0
visited = [0] * n
fragments = ["" for _ in range(n)]

def squirrelWalk(curr):

    global flagIdx

    for nei in edges[curr]:
        if not visited[nei]:
            visited[nei] = 1
            squirrelWalk(nei)

    # Uh oh Chungus dropped a bit of the flag on the current node!!!
    fragments[curr] = FLAG[flagIdx]

    flagIdx += 1

visited[0] = 1

squirrelWalk(0)

print(degrees)
print(XOR)
print(fragments)
