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
  n, m = iis()
  data = [0] * (n+1)
  for _ in range(m):
    l, r = iis()
    data[l-1] += 1
    data[r] -= 1
  for i in range(1, n):
    data[i] += data[i-1]
  ans = 10**9
  for i in range(n):
    ans = min(ans, data[i])
  print(ans)

main()
