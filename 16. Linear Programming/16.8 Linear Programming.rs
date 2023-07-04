use minilp::*;

fn main() {
    let problem = Problem::new();
    problem.add_constraint(Variable::new("x") <= 5);
    problem.add_constraint(Variable::new("y") <= 10);
    problem.set_objective(Variable::new("x") + Variable::new("y"));

    let solution = problem.solve();

    println!("The optimal solution is: {}", solution.objective_value);
}

// This code defines a simple linear programming problem with two variables, x and y. The problem has two constraints: x must be less than or equal to 5, and y must be less than or equal to 10. The objective of the problem is to maximize the value of x + y.

//The main() function first creates a new Problem object. The Problem object is used to define the linear programming problem. The add_constraint() method is used to add constraints to the problem. The set_objective() method is used to set the objective of the problem.

//The problem.solve() method solves the linear programming problem and returns a Solution object. The Solution object contains the values of the variables in the optimal solution.

//The main() function then prints the value of the objective function in the optimal solution.

//To run this code, you can use the following command:
