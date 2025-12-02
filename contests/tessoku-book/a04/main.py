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
  n = ii()
  ans = ''
  # 2進数変換
  while n > 0:
    ans += str(n % 2)
    n //= 2
  ans += '0'* (10-len(ans))
  print(ans[::-1])

main()
