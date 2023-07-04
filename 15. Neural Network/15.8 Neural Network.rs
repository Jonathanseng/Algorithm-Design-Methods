use std::vec::Vec;

struct Neuron {
  weights: Vec<f32>,
  bias: f32,
}

impl Neuron {
  fn new(weights: Vec<f32>, bias: f32) -> Self {
    Self { weights, bias }
  }

  fn forward(&self, inputs: &[f32]) -> f32 {
    let sum = inputs.iter().zip(&self.weights).map(|(x, w)| x * w).sum();
    sum + self.bias
  }
}

fn main() {
  let mut neural_network = Vec::new();
  neural_network.push(Neuron::new(vec![1.0, 2.0, 3.0], 4.0));
  neural_network.push(Neuron::new(vec![4.0, 5.0, 6.0], 7.0));

  let output = neural_network[0].forward(&[1.0, 2.0, 3.0]);

  println!("The output of the neural network is: {}", output);
}

// This code defines a simple neural network with two neurons. The first neuron has three weights and one bias, and the second neuron has three weights and one bias. The forward() function calculates the output of the neural network by multiplying the inputs by the weights and adding the bias. The main() function creates a neural network with the specified weights and biases, and then calculates the output of the neural network for a given set of inputs.

//There are a number of Rust crates that provide support for neural networks. Some of the most popular crates include:

//neuroflow: This crate provides a high-level API for building and training neural networks.
//tch-rs: This crate provides a low-level API for building and training neural networks.
//burn: This crate provides a high-performance API for building and training neural networks.
//These crates can be used to build neural networks for a variety of applications, such as image recognition, natural language processing, and speech recognition.
