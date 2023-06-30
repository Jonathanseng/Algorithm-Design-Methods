fn max_sliding_window_recursive(data: &[i32], window_size: usize) -> Vec<i32> {
    if data.len() < window_size {
        return Vec::new();
    }

    return vec![
        max_sliding_window_recursive(&data[1..], window_size - 1).first().unwrap()
            if data[0] > max_sliding_window_recursive(&data[1..], window_size - 1).first().unwrap()
            else data[0],
        max_sliding_window_recursive(&data[1..], window_size)
            .into_iter()
            .max()
            .unwrap(),
    ];
}

// This code first checks if the length of the data is less than the window size. If it is, then it returns an empty vector. Otherwise, it returns a vector of the maximum values of each sliding window. The sliding window is calculated by starting at the beginning of the data and moving forward by the window size. The maximum value of each sliding window is then calculated recursively and added to the vector.

fn max_sliding_window_iterative(data: &[i32], window_size: usize) -> Vec<i32> {
    let mut maximum_values: Vec<i32> = Vec::new();
    let mut current_window: Vec<i32> = data[0..window_size].to_vec();
    maximum_values.push(current_window.iter().max().unwrap());

    for i in window_size..data.len() {
        current_window.remove(0);
        current_window.push(data[i]);
        maximum_values.push(current_window.iter().max().unwrap());
    }

    return maximum_values;
}

// This code first initializes the maximum values vector to an empty vector. Then, it initializes the current window to the first window size elements of the data. The maximum value of the current window is then added to the maximum values vector. Next, it iterates over the data starting from the window size element. For each element, it removes the oldest element from the current window and adds the new element to the current window. The maximum value of the current window is then added to the maximum values vector. Finally, the maximum values vector is returned.

//Both of these codes work by maintaining a sliding window of the data. The difference is that the recursive code uses recursion to calculate the maximum value of each sliding window, while the iterative code uses a loop to calculate the maximum value of each sliding window.
