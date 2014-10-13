#! /usr/bin/env python
import sys
import random

def sign(w, x):
	p = 0
	for i in range(len(w)):
		p += w[i] * x[i]

	if p > 0:
		return 1
	else:
		return -1

def mistake_d(D, w):
	for d in D:
		(x, y) = d

		if sign(w, x) != y:
			return d

	return None

def new_w(w, x, y):
	neww = w[:]
	for i in range(len(w)):
		neww[i] = w[i] + y * x[i]

	return neww

# fixed precompiled random cycles
def prc_pla(D, w0):
	w = w0

	LIMIT = 1000
	t = 0
	while t < LIMIT:
#		print 'w%d' % t, w
		random.shuffle(D)
		d_err = mistake_d(D, w)
		if d_err == None:
			# no error found, we are done
			break

		(x, y) = d_err
		w = new_w(w, x, y)
		t += 1

	return t

def main():
	D = []
	for line in sys.stdin:
		(xn1, xn2, xn3, xn4, yn) = map(float, line.split())
		xn = [1, xn1, xn2, xn3, xn4]
		d = (xn, yn)
		D.append(d)

	threshold = 0.0
	w0 = [-threshold, 0.0, 0.0, 0.0, 0.0]

	t = 0
	for i in range(2000):
		t += prc_pla(D, w0)

	print t / 2000

if __name__ == '__main__':
	main()
