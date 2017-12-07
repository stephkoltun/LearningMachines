import numpy as np
from random import shuffle

def constructData(filename, num_of_inputs):
	#num_of_inputs = input dimensions

	data_file = open(filename, "r")
	entries = data_file.read().split("\n")
	data_file.close()

	# randomize the examples
	shuffle(entries)

	# split into training (80%), validation (15%), and text (5%) sets
	trainingCount = (len(entries)/5)*4
	validCountEnd = (len(entries)/20)*3 + trainingCount
	print(trainingCount)
	trainingExamples = entries[:trainingCount]
	validationExamples = entries[trainingCount:validCountEnd]
	textExamples = entries[validCountEnd:]

	# create input and output arrays for each set
 	trainingArrays = createEntriesArray(trainingExamples, num_of_inputs)
 	validateArrays = createEntriesArray(validationExamples, num_of_inputs)
 	testArrays = createEntriesArray(textExamples, num_of_inputs)
	
 	return trainingArrays, validateArrays, testArrays

def createEntriesArray(entries, input_num):
	# create lists for the inputs and outputs
	inputslist = []
	outputlist = []

	for line in entries:

		inp_list = []
		line_values = line.split(",")

		for index,inp in enumerate(line_values):
			if index < input_num:
				inp_list.append(float(inp))
			else:
				#use hot-encoding for the categories
				if (inp == 'Iris-setosa'):
					outputlist.append([1,-1,-1])
				if (inp == 'Iris-versicolor'):
					outputlist.append([-1,1,-1])
				if (inp == 'Iris-virginica'):
					outputlist.append([-1,-1,1])

		inputslist.append(inp_list)	

	inputsarray = np.array(inputslist)
	outputsarray = np.array(outputlist)
	return inputsarray, outputsarray



	