#!/usr/bin/env python
import itertools
import sys
from math import factorial
sys.stdin = open("card_game.txt","r")
sys.stdout = open("fbr11out","w")

def combination(n,k):
	a = factorial(n) / factorial(k)
	return a / factorial(n-k)
N = int(raw_input())
c = 1
while N != 0:
	ans = 0
	n,k = map(int,raw_input().split())
	s = map(int,raw_input().split())
	s.sort(reverse=True)
	while n!= k-1:
		n -= 1
		mult = combination(n,k-1)
		ans += s[0] * mult
		s.remove(s[0])

	ans = ans % 1000000007
	print "Case #%d: %d" % (c,ans)
	c += 1
	N -= 1

