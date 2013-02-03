#!/usr/bin/env python
import string
import sys
sys.stdin = open("input3","r")
sys.stdout = open("output2","w")
def is_balanced(exp):
	allowed = set(string.lowercase + " " + ':' + '(' + ')')
	stack = []
	start = set('(:')
	end = set(')')
	for char in exp:
		if char not in allowed:
			return False
		if char in set('()') and ':' in stack:
			stack.pop()
			continue
		if char in start:
			stack.append(char)
		elif char in end:
			if len(stack) == 0: return False
			stack.pop()
		print stack
	if len(stack) != 0:
		for s in stack:
			if s == '(':
				return False
	return True

T = int(raw_input())
case = 0
while T != 0:
	s = raw_input()
	if is_balanced(s):
		ans = "YES"
	else: ans = "NO"
	print "Case #%d: %s" %(case,ans)
	case += 1
	T -= 1
