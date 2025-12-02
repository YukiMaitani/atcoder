import sys
import math
from collections import deque, defaultdict
from bisect import bisect
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
  # 2分探索 bisect
  print(bisect(iil(), x))

main()
