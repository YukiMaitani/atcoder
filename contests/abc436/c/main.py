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
  data = set()
  ans = 0
  for _ in range(m):
    a, b = iis()
    a -= 1
    b -= 1
    w, x, y, z = a*n+b, a*n+b+1, (a+1)*n+b, (a+1)*n+b+1
    if w not in data and x not in data and y not in data and z not in data:
      data.add(w)
      data.add(x)
      data.add(y)
      data.add(z)
      ans += 1
  print(ans)

main()
