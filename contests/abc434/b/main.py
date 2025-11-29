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
  n, m = iis()
  dataA = [0]*m
  dataB = [0]*m
  for _ in range(n):
    a,b = iis()
    dataA[a-1] += 1
    dataB[a-1] += b
  for i in range(m):
    print(dataB[i] / dataA[i])

main()
