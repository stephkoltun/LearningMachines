import numpy as np
from random import shuffle

def constructData(filename, num_of_inputs):

	data_file = open(filename, "r")
	entries = data_file.read().split("\n")
	data_file.close()

	# randomize the examples
	shuffle(entries)
	print(entries)

	# split into training and validatition sets
	trainingCount = (len(entries)/5)*4
	print(trainingCount)
	trainingExamples = entries[:trainingCount]
	validationExamples = entries[trainingCount:]

	# create input and output arrays for each set
 	trainingArrays = createEntriesArray(trainingExamples, num_of_inputs)
 	validateArrays = createEntriesArray(validationExamples, num_of_inputs)
	
 	return trainingArrays, validateArrays

def createEntriesArray(entries, input_num):
	inputslist = []
	outputlist = []

	for line in entries:

		inp_list = []
		line_values = line.split(",")

		for index,inp in enumerate(line_values):
			if index < input_num:
				inp_list.append(float(inp))
			else:
				if (inp == 'Iris-setosa'):
					outputlist.append([1,0,0])
				if (inp == 'Iris-versicolor'):
					outputlist.append([0,1,0])
				if (inp == 'Iris-virginica'):
					outputlist.append([0,0,1])

		inputslist.append(inp_list)	

	inputsarray = np.array(inputslist)
	outputsarray = np.array(outputlist)
	return inputsarray, outputsarray



	