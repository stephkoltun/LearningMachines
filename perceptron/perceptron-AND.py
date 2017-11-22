# Learning Machines, Assignment 1
# Fall 2017, ITP NYU
# Stephanie Koltun

import sys
import random
import numpy as np

training_and = np.array([
	([1,1],1),	# true true = true
	([1,0],0),	# true false = false
	([0,1],0),	# false true = false
	([0,0],1),	# false false = true
])

inputweight = np.random.rand(2)	# generate an array of random weights
biasinput = 1	# as a scalar
biasweight = np.random.rand(1)
learnconst = 0.3

def train():
	print "training..."
	# pick on of the known input/output combos from the training set
	knowninput, expected = random.choice(training_and)
	print knowninput, expected
	error = check(knowninput, expected)
	
	if (error != 0):
		# let's assign new weights
		adjustweights(error, knowninput)
		# train again....
		train()
	else:
		# check if the weights work for all the inputs...
		print "these weights are fine. but let's try it on all the inputs"
		if checkAllInputs():
			print "success!"
		else:
			print "train again!"
			#train()
		# print "weightA: " + str(inputweight[0])
		# print "weightB: " + str(inputweight[1])
		# print "weightBias: " + str(biasweight[0])

def check(inp, exp):
	guess = np.dot(inp,inputweight) + np.dot(biasinput,biasweight)
	print "guess: " + str(guess)

	evalu = evaluate(guess)
	print "evalu: " + str(evalu)

	err = exp - evalu
	print "error: " + str(err)

	return err

def checkAllInputs():
	#for inp in training_and
	print "done!"
	#return true


	
def adjustweights(err, inp):
	print "adjustweights"
	
	#get error delta
	delta = 0
	for i in inp:
		delta += i*err
	print "delta: " + str(delta)

	newweights = np.dot(inp,(delta*learnconst))

	print "orig weights: " + str(inputweight) 
	print "weights: " + str(newweights)
	#reassign weights
	inputweight[0] = newweights[0]
	inputweight[1] = newweights[1]


def evaluate(val):
	#this is the decision node
	if val >= 1:
		return 1
	else:
		return 0	


train()

