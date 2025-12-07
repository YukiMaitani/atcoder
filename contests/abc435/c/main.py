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
  n, A = ii(), iil()
  ans = 1
  for i, a in enumerate(A):
    if i == ans:
      break
    ans = max(ans, i + a)
  print(min(ans, n))

main()
