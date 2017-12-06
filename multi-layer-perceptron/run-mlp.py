from mlp import *
from readfile import *

# Usage Example:

# Set hyperparameters:
sample_size = 4
output_size = 3
example_cnt = 300

batch_size  = 10
epoch_cnt   = 10000
report_freq = 10
learn_rate  = 0.05

# Construct MLP:
mlp = Mlp( [ sample_size, 15, output_size ], "tanh" )
	#	self,layer_sizes,activation_fn_name

# Construct dataset:
dataset = constructData("iris.txt", 4)
training_inputs = dataset[0]
training_outputs = dataset[1]

#training_inputs  = np.random.uniform( 0.0, np.pi * 2.0, ( sample_size, example_cnt ) )
#training_outputs = np.sin( training_inputs )

print(training_inputs)
print(training_outputs)


# Train MLP:
mlp.train( training_inputs, training_outputs, learn_rate, epoch_cnt, batch_size, report_freq )

# Make predictions:
training_guesses = mlp.predict( training_inputs )

# Print correct and predicted outputs:
print ( "Outputs: %s\nGuesses: %s\n" ) % ( training_outputs, training_guesses )


