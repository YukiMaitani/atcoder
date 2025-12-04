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
  l = 0
  r = 10**9
  while l < r:
    m = (l + r) // 2
    c = sum(m//a for a in A)
    if c < k:
      l = m+1
    else:
      r = m
  print(l)

main()
