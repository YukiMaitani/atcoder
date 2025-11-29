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
  T = ii()
  for _ in range(T):
    n, h = iis()
    pl = h
    ph = h
    ok = True
    for _ in range(n):
      t, l, u = iis()
      low = max(1, pl - t)
      high = ph + t
      if not (((l <= high) and (l >= low)) or ((u <= high) and (u >= low))):
        ok = False
      pl = max(low, l)
      ph = min(high, u)
    pyn(ok)
main()
