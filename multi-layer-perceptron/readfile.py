import numpy as np

def constructData(filename, num_of_inputs):

	#dat = np.loadtxt( filename )

	data_file = open(filename, "r")
	entries = data_file.read().split("\n")

	dataArray = createEntriesArray(entries, num_of_inputs)
	
	return dataArray

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
					outputlist.append([1,-1,-1])
				if (inp == 'Iris-versicolor'):
					outputlist.append([-1,1,-1])
				if (inp == 'Iris-virginica'):
					outputlist.append([-1,-1,1])

		inputslist.append(inp_list)	

	inputsarray = np.array(inputslist)
	outputsarray = np.array(outputlist)
	return inputsarray, outputsarray



	