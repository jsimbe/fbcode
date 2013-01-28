#!/usr/bin/env python
import sys
sys.stdin = open("find_the_mintxt","r")
T = input()
"""
n,k = 98,59
a,b,c,r = 6,30,524,98
m = [0] * k
m[0] = a
"""
case = 1
while T != 0:
	n,k = map(int,raw_input().split())
	a,b,c,r = map(int,raw_input().split())
	m = [0] * k
	m[0] = a
	for i in xrange(1,k):
		m[i] = (b * m[i - 1] + c) % r
	while len(m) != n:
		for i in xrange(n):
			if(i not in m[-k:]):
				m.append(i)
				break;
	print "Case #%d: %d" % (case,m[n-1])
	case += 1
	T -= 1
