import numpy as np

class NeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size):
    self.weights_1 = np.random.rand(input_size, hidden_size)
    self.weights_2 = np.random.rand(hidden_size, output_size)

  def feedforward(self, inputs):
    hidden_layer_activations = np.dot(inputs, self.weights_1)
    hidden_layer_outputs = np.tanh(hidden_layer_activations)
    output_layer_activations = np.dot(hidden_layer_outputs, self.weights_2)
    return output_layer_activations


def main():
  network = NeuralNetwork(3, 2, 1)
  inputs = np.array([1, 2, 3])
  outputs = network.feedforward(inputs)
  print(outputs)


if __name__ == "__main__":
  main()

# This code first defines a class called NeuralNetwork. This class has three attributes: weights_1, weights_2, and output_size. weights_1 is a matrix of weights that connect the input layer to the hidden layer. weights_2 is a matrix of weights that connect the hidden layer to the output layer. output_size is the number of neurons in the output layer.

#The NeuralNetwork class also has a method called feedforward(). This method takes an input vector and returns the output vector of the neural network. The feedforward() method works by first calculating the activations of the hidden layer. The activations of the hidden layer are calculated by multiplying the input vector by the weights_1 matrix and then applying the tanh function. The output of the neural network is then calculated by multiplying the activations of the hidden layer by the weights_2 matrix.

#The main() function then creates an instance of the NeuralNetwork class and then feeds it the input vector [1, 2, 3]. The main() function then prints the output vector of the neural network.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as neural_network.py, you can run it by typing the following command into the command line:
