fn brute_force(x: &[i32]) -> i32 {
  // Initialize the largest number to the first element in the list.
  let mut largest = x[0];

  // Iterate through the list, keeping track of the largest number seen so far.
  for i in 1..x.len() {
    if x[i] > largest {
      largest = x[i];
    }
  }

  // Return the largest number.
  largest
}

fn main() {
  // Create a list of numbers.
  let x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  // Find the largest number in the list using brute force.
  let largest = brute_force(&x);

  // Print the largest number.
  println!("The largest number in the list is: {}", largest);
}
