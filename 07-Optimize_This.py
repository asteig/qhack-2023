import json
import pennylane as qml
import pennylane.numpy as np

def three_optimization_steps(data):
    """Performs three optimization steps on a quantum machine learning model.

    Args:
        data (list(float)): Classical data that is to be embedded in a quantum circuit.

    Returns:
        (float): The cost function evaluated after three optimization steps.
    """

    normalize = np.sqrt(np.sum(data[i] ** 2 for i in range(len(data))))
    data /= normalize

    dev = qml.device("default.qubit", wires=3)

    @qml.qnode(dev)
    def cost(weights, data=data):
        """A circuit that embeds classical data and has quantum gates with tunable parameters/weights.

        Args:
            weights (numpy.array): An array of tunable parameters that help define the gates needed.

        Kwargs:
            data (list(float)): Classical data that is to be embedded in a quantum circuit.

        Returns:
            (float): The expectation value of the sum of the Pauli Z operator on every qubit.
        """


        # Put your code here #

        return


    # initialize the weights
    shape = qml.BasicEntanglerLayers.shape(n_layers=2, n_wires=dev.num_wires)
    weights = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6], requires_grad=True).reshape(
        shape
    )


    # Put your code here #

    # Define a gradient descent optimizer with a step size of 0.01

    # Optimize the cost function for three steps


    return cost(weights, data=data)


# These functions are responsible for testing the solution.
def run(test_case_input: str) -> str:
    data = json.loads(test_case_input)
    cost_val = three_optimization_steps(data)
    return str(cost_val)

def check(solution_output: str, expected_output: str) -> None:
    solution_output = json.loads(solution_output)
    expected_output = json.loads(expected_output)
    assert np.allclose(solution_output, expected_output, rtol=1e-4)


test_cases = [['[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]', '0.066040']]

for i, (input_, expected_output) in enumerate(test_cases):
    print(f"Running test case {i} with input '{input_}'...")

    try:
        output = run(input_)

    except Exception as exc:
        print(f"Runtime Error. {exc}")

    else:
        if message := check(output, expected_output):
            print(f"Wrong Answer. Have: '{output}'. Want: '{expected_output}'.")

        else:
            print("Correct!")