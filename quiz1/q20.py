#! /usr/bin/env python
import sys
import argparse
import random

def readdata(filepath):
	f = open(filepath, 'r')

	D = []
	for line in f:
		line = line.strip()
		(xn1, xn2, xn3, xn4, yn) = map(float, line.split())
		xn = [1, xn1, xn2, xn3, xn4]
		d = (xn, yn)
		D.append(d)

	return D

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

def mistakes(D, w):
	count = 0
	for d in D:
		(x, y) = d

		if sign(w, x) != y:
			count += 1

	return count

def new_w(w, x, y):
	neww = w[:]
	for i in range(len(w)):
		neww[i] = w[i] + y * x[i]

	return neww

# pocket algorithm
def pocket(D, w0):
	w = w0
	bestw = w
	min_mistakes = mistakes(D, w)

	LIMIT = 100
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
		m = mistakes(D, w)
		if min_mistakes > m:
			min_mistakes = m
			bestw = w
		t += 1

	return bestw

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--train', help='training data file', required=True)
	parser.add_argument('--test', help='test data file', required=True)
	args = parser.parse_args()

	Dtrain = readdata(args.train)
	Dtest = readdata(args.test)

	threshold = 0
	w0 = [-threshold, 0, 0, 0, 0]

	err_rate = 0.0
	for i in range(2000):
		w_pocket= pocket(Dtrain, w0)
		errs = mistakes(Dtest, w_pocket)
		err_rate += float(errs) / len(Dtest)
	err_rate /= 2000
	print err_rate

if __name__ == '__main__':
	main()
