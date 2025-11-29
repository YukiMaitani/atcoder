import sys
import math
from collections import deque, defaultdict
input = sys.stdin.readline

def s(): return input().rstrip()
def ii(): return int(input())
def iis(): return map(int, input().split())
def iil(): return list(map(int, input().split()))
def iss(): return input().split()
def py(): print("Yes")
def pn(): print("No")
def pyn(yes): py() if yes else pn()

def main():
  n = ii()
  c = 2001
  data = [[0]*c for _ in range(c)]
  clouds = []
  for _ in range(n):
    u, d, l, r = iis()
    u -= 1
    d -= 1
    l -= 1
    r -= 1
    clouds.append((u,d,l,r))
    data[u][l] += 1
    data[u][r+1] -= 1
    data[d+1][l] -= 1
    data[d+1][r+1] += 1
  for i in range(c):
    for j in range(1,c):
      data[i][j] += data[i][j-1]
  for j in range(c):
    for i in range(1,c):
      data[i][j] += data[i-1][j]
  single = [[1 if data[i][j] == 1 else 0 for j in range(c)] for i in range(c)]
  for i in range(c):
      for j in range(1, c):
          single[i][j] += single[i][j-1]
  for j in range(c):
      for i in range(1, c):
          single[i][j] += single[i-1][j]
  empty = 0
  for i in range(c-1):
    for j in range(c-1):
      if data[i][j] == 0:
        empty += 1
  for cloud in clouds:
    u, d, l, r = cloud
    area = single[d][r]
    if u > 0:
        area -= single[u-1][r]
    if l > 0:
        area -= single[d][l-1]
    if u > 0 and l > 0:
        area += single[u-1][l-1]

    ans = empty + area
    print(ans)

main()
