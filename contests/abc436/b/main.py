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
  data = [[-1]*n for _ in range(n)]
  pre = (0, (n-1)/2)
  k = 1
  data[int(pre[0])][int(pre[1])] = k
  for i in range(n*n-1):
    x = (pre[0]-1)%n
    y = (pre[1]+1)%n
    if data[int(x)][int(y)] != -1:
      x = (pre[0]+1)%n
      y = pre[1]
    k += 1
    data[int(x)][int(y)] = k
    pre = (x, y)
  for i in range(n):
    print(' '.join(map(str, data[i])))

main()
