from mlp import *
from readfile import *


# Set hyperparameters:
sample_size = 4		# input dimensions
output_size = 3		# output dimensions
example_cnt = 150	# number of examples in the dataset

batch_size  = 10
epoch_cnt   = 30000
report_freq = 10
learn_rate  = 0.05

# Construct MLP:
# takes layer_sizes and activation_fn_name as arguments
mlp = Mlp( [ sample_size, 15, output_size ], "sig" )
			
# Construct dataset:
dataset = constructData("iris.txt", 4)

# TO DO split into training and testing (80%, 20%)
training_inputs = dataset[0]
training_outputs = dataset[1]

print(training_inputs)
print(training_outputs)

# Train MLP:
mlp.train( training_inputs, training_outputs, learn_rate, epoch_cnt, batch_size, report_freq )

# Make predictions:
# TO DO: Replace with testing inputs (not trainig)
training_guesses = mlp.predict( training_inputs )

# Print correct and predicted outputs:
print ( "Outputs: %s\nGuesses: %s\n" ) % ( training_outputs, training_guesses )


