"""
automatically check if it's possible to assign integer values to variables
    so that equalities (x_i == x_j) and inequalities (x_i != x_j) hold using disjoint sets.
input: 
first line: number of variables n; number of equalities e, number of inequalities d
consequent lines : 
e lines of equalities (e.g. "2 3" means x_2 == x_3)
d lines of inequalities (e.g. "4 5" means x_4 != x_5)

output: 1 if the system is consistent, 0 otherwise

Sample input:
6 5 3
2 3
1 5
2 5
3 4
4 2
6 1
4 6
4 5

Sample output:
0
"""


class dsets:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if not i == self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id: return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


flag = 1

n, e, d = [int(x) for x in input().split()]

sets = dsets(n)

for i in range(e):
    xi, xj = [int(x) - 1 for x in input().split()]
    sets.union(xi, xj)

for k in range(d):
    xi, xj = [int(x) - 1 for x in input().split()]
    if sets.find(xi) == sets.find(xj):
        flag = 0
        print(flag)
        break
if flag == 1:
    print(flag)
