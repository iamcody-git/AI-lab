from math import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

def summation_neural(x1, x2, weights):
    return weights[0] + x1 * weights[1] + x2 * weights[2]

def OR_gate(x1, x2):
    literal_str = f"{x1} OR {x2} = "
    weights = [-1, 2, 2]
    Z = summation_neural(x1, x2, weights)
    sigmoid_val = sigmoid(Z)
    if sigmoid_val >= 0.5:
        print(literal_str + "1")
    else:
        print(literal_str + "0")

def AND_gate(x1, x2):
    literal_str = f"{x1} AND {x2} = "
    weights = [-2, 1, 1]
    Z = summation_neural(x1, x2, weights)
    sigmoid_val = sigmoid(Z)
    if sigmoid_val >= 0.5:
        print(literal_str + "1")
    else:
        print(literal_str + "0")

for x1 in range(2):
    for x2 in range(2):
        AND_gate(x1, x2)

for x1 in range(2):
    for x2 in range(2):
        OR_gate(x1, x2)

