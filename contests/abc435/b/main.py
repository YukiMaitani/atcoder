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
  ans = 0
  n, A = ii(), iil()
  for l in range(n):
    for r in range(l,n):
      s = sum(A[l:r+1])
      ok = True
      for i in range(l, r+1):
        if s % A[i] == 0:
          ok = False
          break
      if ok:
        ans += 1
  print(ans)

main()
