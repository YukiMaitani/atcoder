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
  n, s = iis()
  T = iil()
  ans = True
  pre = 0
  for t in T:
    if t - pre > s+0.5:
      ans = False
      break
    pre = t
  pyn(ans)

main()
