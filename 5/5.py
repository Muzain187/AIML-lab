import numpy as np

# Activation function and its derivative
def sigmoid(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# Input data
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# Output data
y = np.array([[0],
              [1],
              [1],
              [0]])

# Seed the random number generator
np.random.seed(1)

# Initialize weights randomly with mean 0
weights0 = 2 * np.random.random((3, 4)) - 1
weights1 = 2 * np.random.random((4, 1)) - 1

# Train the ANN
for i in range(1000):
    # Forward propagation
    layer0 = X
    layer1 = sigmoid(np.dot(layer0, weights0))
    layer2 = sigmoid(np.dot(layer1, weights1))

    # Compute the error
    error = y - layer2

    # Backpropagation
    d_layer2 = error * sigmoid(layer2, True)
    d_weights1 = np.dot(layer1.T, d_layer2)
    d_layer1 = np.dot(d_layer2, weights1.T) * sigmoid(layer1, deriv=True)
    d_weights0 = np.dot(layer0.T, d_layer1)

    # Update the weights
    weights1 += d_weights1
    weights0 += d_weights0

    print('-------Epoch '+str(i)+'---------')
    print('Input ' + str(X))
    print('Output ' + str(y))
    print('Predicted '+ str(layer2))
    print('-------------------------')


# Test the ANN 3 input neurons , 4 hiiden neurons and 1 output neurons


