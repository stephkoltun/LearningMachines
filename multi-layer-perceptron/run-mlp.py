from mlp import *
from readfile import *


# Set hyperparameters:
sample_size = 4		# input dimensions
output_size = 3		# output dimensions
example_cnt = 150	# number of examples in the dataset

batch_size  = 10
epoch_cnt   = 30000
report_freq = 10
report_buff = 100
learn_rate  = 0.05


# Construct MLP:
# takes layer_sizes and activation_fn_name as arguments
mlp = Mlp( "iris", [ sample_size, 15, output_size ], "sig" )
			
# Construct dataset, returns both training and validation sets:
datasets = constructData("iris.txt", 4)

training = datasets[0]
validation = datasets[1]

print(training)
print(validation)


training_inputs = training[0]
training_outputs = training[1]

validation_inputs = validation[0]
validation_outputs = validation[1]


# Train MLP:
# arguments are: training_samples, training_labels, validation_samples, validation_labels, learn_rate, epochs, batch_size, report_freq, report_buff
mlp.train( training_inputs, training_outputs, validation_inputs, validation_outputs, learn_rate, epoch_cnt, batch_size, report_freq,  report_buff)


# Print correct and predicted outputs:
# print ( "Outputs: %s\nGuesses: %s\n" ) % ( training_outputs, training_guesses )


