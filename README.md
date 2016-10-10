# Perceptron

This is the implementation for a single two-input one-output neuron in a neural network which learns using training data and tests on test data where the data is divided into training and test sections using k-fold cross-validation technique.

The two input perceptron is trained on sample data and using a graph, it is shown that as training proceeds, the error between predicted output and target output is reduced. This means that the perceptron is learning to predict output for cases satisfying the function (here, linearly separable functions).

Here,
h(x) = summation of (weights*input)
g(h) = 1/(1 + exp**(-h))           ..it is the sigmoid function and acts as the activation function here. 

Our goal is to find a (linear) function (w1)x1 + (w2)x2 + w0 such that it separates the two classes of outputs (0 or 1), given the two inputs. The constants (weights- w0, w1, w2) are so adjusted based on the training data to minimize the error.

A number of epochs (iterations) are done for each of the training data instance and error is found as the difference between the predicted output and target output. The weights are adjusted based on the formula-

delta_w = -1*learning_rate*(predicted_output - target_output)*derivative_of_g*input_value

After the training, the final constants (weights) are used in the equation and it is used to determine if the test_input point (x1,x2) lies below the line or above it (class 0 or 1). This is compared to the target output to determine the accuracy. K-fold validation is used for partitioning data in training and test sets. The results are displayed through graphs.

The training and graphs are also done for the boolean gates- AND, OR, NAND, NOR, XOR and the graphs are plotted. Since XOR is not linearly separable, it cannot be put into any of the classes defined by the line (w1)x + (w2)y + w0. As seen in the graph of Error vs. Epoch for XOR, the error is to the degree of e**-1 and varies very little with each epoch. That means, varying the weights of the line cannot reduce the error for this function and hence, this perceptron cannot be trained for XOR.
