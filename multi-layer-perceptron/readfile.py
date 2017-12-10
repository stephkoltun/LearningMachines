import numpy as np
from random import shuffle

# uses the Forest Covertype data set from UCI archives
# https://archive.ics.uci.edu/ml/datasets/covertype
# http://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.info


def constructData(filename, num_of_inputs):
	#num_of_inputs = input dimensions

	data_file = open(filename, "r")
	entries = data_file.read().split("\n")
	data_file.close()

	print("total examples: " + str(len(entries)))

	# randomize the examples
	shuffle(entries)

	# split into training (80%), validation (15%), and text (5%) sets
	trainingCount = 5000
	validCountEnd = trainingCount + 2000
	testCountEnd = validCountEnd + 100
	trainingExamples = entries[:trainingCount]
	validationExamples = entries[trainingCount:validCountEnd]
	textExamples = entries[validCountEnd:testCountEnd]

	print("training count: " + str(trainingCount) + ", validation count: 2000, test count: 100")

	# create input and output arrays for each set
 	trainingArrays = createEntriesArray(trainingExamples, num_of_inputs)
 	print("completed training construction")
 	validateArrays = createEntriesArray(validationExamples, num_of_inputs)
 	print("completed validation construction")
 	testArrays = createEntriesArray(textExamples, num_of_inputs)

 	print("completed data construction")
	
 	return trainingArrays, validateArrays, testArrays

def createEntriesArray(entries, input_num):
	# create lists for the inputs and outputs
	inputslist = []
	outputlist = []


	for line in entries:

		inp_list = []
		line_values = line.split(",")

		for index,inp in enumerate(line_values):
			#elevation
			if index == 0:
				thisVal = float(inp)
				mappedVal = mapVal(thisVal,1863.0,3849.0,-1.0,1.0)
				inp_list.append(mappedVal)

			#aspect
			if index == 1:
				thisVal = float(inp)
				mappedVal = mapVal(thisVal,0.0,360.0,-1.0,1.0)
				inp_list.append(mappedVal)

			#slope
			if index == 2:
				thisVal = float(inp)
				mappedVal = mapVal(thisVal,0.0,61.0,-1.0,1.0)
				inp_list.append(mappedVal)

			#horizontal dist to water
			if index == 3:
				thisVal = float(inp)
				mappedVal = mapVal(thisVal,0.0,1343.0,-1.0,1.0)
				inp_list.append(mappedVal)

			#vertical dist to water
			if index == 4:
				thisVal = float(inp)
				mappedVal = mapVal(thisVal,-146.0,554.0,-1.0,1.0)
				inp_list.append(mappedVal)

			#horizontal dist to roadway	
			if index == 5:
				thisVal = float(inp)
				mappedVal = mapVal(thisVal,0.0,7117.0,-1.0,1.0)
				inp_list.append(mappedVal)

			#hillshade: 9am, Noon, 3pm
			if index >= 6 and index <= 8: 
				thisVal = float(inp)
				mappedVal = mapVal(thisVal,0.0,255.0,-1.0,1.0)
				inp_list.append(mappedVal)

			#temporarily ignoring the hot-encoded binary variables
			if index == 54:
				#use hot-encoding for the categories
				if (inp == '1'):
					outputlist.append([1,-1,-1,-1,-1,-1,-1])
				if (inp == '2'):
					outputlist.append([-1,1,-1,-1,-1,-1,-1])
				if (inp == '3'):
					outputlist.append([-1,-1,1,-1,-1,-1,-1])
				if (inp == '4'):
					outputlist.append([-1,-1,-1,1,-1,-1,-1])
				if (inp == '5'):
					outputlist.append([-1,-1,-1,-1,1,-1,-1])
				if (inp == '6'):
					outputlist.append([-1,-1,-1,-1,-1,1,-1])
				if (inp == '7'):
					outputlist.append([-1,-1,-1,-1,-1,-1,1])

		inputslist.append(inp_list)	

	inputsarray = np.array(inputslist)
	outputsarray = np.array(outputlist)
	return inputsarray, outputsarray


def mapVal(value, istart, istop, ostart, ostop):
    return ostart + ( ostop - ostart ) * ( ( value - istart ) / ( istop - istart ) );

	