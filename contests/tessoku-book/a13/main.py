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
  n, k = iis()
  A = iil()
  R = [0]
  for i, a in enumerate(A[:n-1]):
    r = R[i]
    while r < n-1 and A[r+1] - a <= k:
      r += 1
    R.append(r)
  ans = 0
  for i, r in enumerate(R[1:]):
    ans += r -i
  print(ans)

main()
