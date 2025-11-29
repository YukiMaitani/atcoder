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
  n,x = iis()
  a = iil()
  ans = 101
  for i in range(101):
    score = sum(sorted(a+[i])[1:n-1])
    if score >= x:
      ans = min(i, ans)
  if ans == 101:
    ans = -1
  print(ans)

main()
