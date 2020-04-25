#!/usr/bin/env python

import numpy as np
import pandas as pd
import sys
import getopt
import logging

def main(argv):
	Ax = ''
	Ay = ''
	Az = ''
	Gx = ''
	Gy = ''
	Gz = ''

	try:
		opts, args = getopt.getopt(argv, "hx:y:z:a:b:c:",["Ax=","Ay=","Az=","Gx=","Gy=","Gz="])
	except getopt.GetoptError:
		print("not defined !!!!!")
		print("\tmpu6050.py -h <help>")
		sys.exit(2)
	if len(sys.argv) < 2:
		print("mpu6050.py -h <help>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("mpu6050.py [options]")
			print("option lists :")
			print("\t-x [Ax Value]")
			print("\t-y [Ay Value]")
			print("\t-z [Az Value]")
			print("\t-a [Gx Value]")
			print("\t-b [Gy Value]")
			print("\t-c [Gz Value]")
			sys.exit()
		elif opt in ("-x", "--Ax"):
			Ax = arg
		elif opt in ("-y", "--Ay"):
			Ay = arg
		elif opt in ("-z", "--Az"):
			Az = arg
		elif opt in ("-a", "--Gx"):
			Gx = arg
		elif opt in ("-b", "--Gy"):
			Gy = arg
		elif opt in ("-c", "--Gz"):
			Gz = arg

	filepath = r'c:\xampp\htdocs\piranticerdas\mpudataset.csv'

	data = pd.read_csv(filepath)

	from sklearn import preprocessing
	ley = preprocessing.LabelEncoder()
	X = data.drop(columns=['Label'])
	y = data['Label'].values
	y = ley.fit_transform(y)
	from sklearn.preprocessing import StandardScaler
	scaler = StandardScaler()
	X = scaler.fit_transform(X)


	from sklearn.svm import SVC
	import datetime

	clf = SVC(gamma=0.01, C=10)

	clf.fit(X,y)
	new = np.array([[float(Ax),float(Ay),float(Az),float(Gx),float(Gy),float(Gz)]])
	new = scaler.transform(new)
	res = clf.predict(new)
	print(ley.inverse_transform(res)[0])

if __name__=="__main__":
	main(sys.argv[1:])
