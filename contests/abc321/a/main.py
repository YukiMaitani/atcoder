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
  S = s()
  pre = int(S[0])
  ans = True
  for c in S[1:]:
    now = int(c)
    if now >= pre:
      ans = False
      break
    pre = now
  pyn(ans)

main()
