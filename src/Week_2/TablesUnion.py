def find(idx):
    global indexes
    steps = []
    while not idx == indexes[idx]:
        steps += [idx]
        idx = indexes[idx]
    for i in steps:
        indexes[i] = idx
    return idx


def union(dest, source):
    global tables, indexes, n, m
    id_dest = find(dest)
    id_source = find(source)
    if not id_dest == id_source:
        tables[id_dest] += tables[id_source]
        indexes[id_source] = id_dest
        if tables[id_dest] > tables[0]:
            tables[0] = tables[id_dest]
    print(tables[0])
n, m = map(int, input().split())
tables = [0]
tables += list(map(int, input().split()))
tables[0] = max(tables)
indexes = list(range(n+1))

for i in range(1,m+1):
    destination, source = map(int, input().split())
    union(destination, source)
