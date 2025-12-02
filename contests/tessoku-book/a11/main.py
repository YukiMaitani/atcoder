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
  n, x = iis()
  A = iil()
  l,r = 0, n-1
  ans = -1
  # 二分探索
  while l <= r:
    m = (l + r) // 2
    if A[m] < x:
      l = m + 1
    elif A[m] > x:
      r = m -1
    else:
      ans = m
      break

  print(ans+1)

main()
