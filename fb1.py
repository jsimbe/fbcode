#!/usr/bin/env python
import sys
from collections import Counter
sys.stdin = open("beautiful_stringstxt","r")
sys.stdout = open("output1","w")
def score(s):
	s = s.lower()
	a = ''.join(letter for letter in s if letter.isalpha())
	score = 0
	c = Counter(a)
	aval = 26
	lcount = sorted(c.values(), reverse=True)
	for val in lcount:
		score += val * aval
		aval -= 1
	return score


T = int(raw_input())
case = 1
while T != 0:
	s = raw_input()
	print "Case #%d: %d" %(case,score(s))
	case += 1
	T -= 1
