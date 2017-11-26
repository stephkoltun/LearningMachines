# Learning Machines, Assignment 3
# perceptron for AND and OR tables
# Fall 2017, ITP NYU
# Stephanie Koltun

import sys
import random
import numpy as np

# cmd line: python perceptron [TABLE] (argument takes either AND or OR)
# it only works for my OR table
# for the AND table, I get recursion depth errors
#...File "/Library/Python/2.7/site-packages/numpy-override/numpy/core/numeric.py", line 2507, in seterr
#    old = geterr()
#RuntimeError: maximum recursion depth exceeded 

orTable = np.array([
	([1,1],1),	# true true = true
	([1,0],1),	# true false = true
	([0,1],1),	# false true = true
	([0,0],0),	# false false = false
])

andTable = np.array([
	([1,1],1),	# true true = true
	([1,0],0),	# true false = false
	([0,1],0),	# false true = false
	([0,0],1),	# false false = true
])

inputweight = np.random.rand(2)	# generate an array of random weights
biasinput = 1	# as a scalar
biasweight = np.random.rand(1)
learnconst = 0.2


def train(trainArray):
	print "training..."
	# pick on of the known input/output combos from the training set
	knowninput, expected = random.choice(trainArray)
	print knowninput, expected
	thiserror = check(knowninput, expected)
	
	if (thiserror != 0):
		# let's assign new weights - based on the error and the tested inputs
		adjustweights(thiserror, knowninput)
		# train again....
		train(trainArray)
	else:
		# check if the weights work for all the inputs...
		print "-----these weights are fine for this random input. but let's try it on all the inputs..."
		
		if checkAllInputs(trainArray):
			print "------- FINAL weights"
			print "weightA: " + str(inputweight[0])
			print "weightB: " + str(inputweight[1])
			print "weightBias: " + str(biasweight[0])	
			print "success!"
		else:
			print "failed"
			train(trainArray);
		

def check(inp, outputexp):

	combinedVal = np.dot(inputweight,inp) + np.dot(biasweight,biasinput)
	print "combined: " + str(combinedVal)

	outputguess = decide(combinedVal)

	err = outputexp - outputguess
	print "error: " + str(err)
	return err

def decide(val):
	#this is the decision node
	if val >= 1:
		return 1
	else:
		return 0	


def checkAllInputs(trainArray):
	#print "done!"

	for known in trainArray:
		knowninput, expected = known;
		print knowninput, expected
		error = check(knowninput, expected)
		if (error != 0):
			print "welp, doesn't work for one of the inputs"
			adjustweights(error, knowninput)
			return False
			#train(trainArray);
	else:
		return True



# give this the error, and just the input that was used when testing	
def adjustweights(err, inputs):
	print "------- old weights"
	print "weightA: " + str(inputweight[0])
	print "weightB: " + str(inputweight[1])
	print "weightBias: " + str(biasweight[0])
	
	#get error delta
	delta = 0
	for val in inputs:
	 	delta += val*err
	print "delta: " + str(delta)

	# adjust the INPUT weights
	#print "--- input weights"
	count = 0;
	for oldweight in inputweight:
		newweight = oldweight + (delta*learnconst)
		#print newweight
		#reassign the revised weight
		inputweight[count] = newweight
		count += 1
	
	# adjust the BIAS weights
	#print "--- biasweight"
	newbias = biasweight[0] + (delta*learnconst)
	#print newbias

	biasweight[0] = newbias

	print "------- new weights"
	print "weightA: " + str(inputweight[0])
	print "weightB: " + str(inputweight[1])
	print "weightBias: " + str(biasweight[0])	

if (sys.argv[1] == "AND"):
	train(andTable)

if (sys.argv[1] == "OR"):
	train(orTable)

