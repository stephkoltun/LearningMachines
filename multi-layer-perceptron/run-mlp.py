from mlp import *
from readfile import *


# Set hyperparameters:
sample_size = 9		# input dimensions
output_size = 7		# output dimensions

batch_size  = 10
epoch_cnt   = 3000
report_freq = 10
report_buff = 100
learn_rate  = 0.05

# Construct MLP:
# takes layer_sizes and activation_fn_name as arguments
mlp = Mlp( "forest", [ sample_size, 15, output_size ], "tanh" )
			
# Construct dataset, returns training, validation and test sets:
datasets = constructData("data/forestcovertype.txt", 4)
training = datasets[0]
validation = datasets[1]
test = datasets[1]

# Split them into their inputs and outputs
training_inputs = training[0]
print(training_inputs)
training_outputs = training[1]
validation_inputs = validation[0]
validation_outputs = validation[1]
test_inputs = test[0]
test_outputs = test[1]

# Train MLP:
# arguments are: training_samples, training_labels, validation_samples, validation_labels, learn_rate, epochs, batch_size, report_freq, report_buff
mlp.train( training_inputs, training_outputs, validation_inputs, validation_outputs, learn_rate, epoch_cnt, batch_size, report_freq,  report_buff)

# Do a final guess
# Make predictions:
test_guesses = mlp.predict( test_inputs )
test_error = mlp.getErrorRate( test_outputs, test_guesses )
# Print correct and predicted outputs:
print ( "Outputs: %s\nGuesses: %s\nError: %s\n" ) % ( test_outputs, test_guesses, test_error )
