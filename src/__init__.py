import math
import csv
import random
import matplotlib.pyplot as plt

LEARNING_RATE = 0.001
EPOCH = 1000
ERROR_TOLERANCE = 0.0001
FILE_NAME = '../data.csv'

with open(FILE_NAME, 'rb') as f:
    reader = csv.reader(f)
    data_set = list(reader)


def h_function(weight0, weight1, weight2, input1, input2):
    return weight0 + (weight1 * input1) + (weight2 * input2)


def g_function(weight0, weight1, weight2, input1, input2):
    h = h_function(weight0, weight1, weight2, input1, input2)
    return float(1) / (1 + math.exp(-1 * h))


def calculate_error(target_output, actual_output):
    return math.pow((target_output - actual_output), 2)


def derivative_of_g(g_result):
    return g_result * (1 - g_result)


def delta_w(g_result, input_value, target_output, learning_rate=0.001):
    derivative = derivative_of_g(g_result)
    return -1 * learning_rate * (g_result - target_output) * derivative * input_value


avg_error_plot = []


def train(data):
    w0 = random.uniform(-0.2, 0.2)
    w1 = random.uniform(-0.2, 0.2)
    w2 = random.uniform(-0.2, 0.2)

    average_error = 100
    iteration = 0
    while iteration < EPOCH and average_error > ERROR_TOLERANCE:
        total_error = 0

        for row in data:
            x1 = float(row[0])
            x2 = float(row[1])
            target_output = float(row[2])

            g_result = g_function(w0, w1, w2, x1, x2)

            error = calculate_error(target_output, g_result)
            total_error += error

            w0 += delta_w(g_result, 1, target_output, LEARNING_RATE)
            w1 += delta_w(g_result, x1, target_output, LEARNING_RATE)
            w2 += delta_w(g_result, x2, target_output, LEARNING_RATE)

        iteration += 1
        average_error = float(total_error) / len(data)
        avg_error_plot.append(average_error)

    print "w0 is: " + str(w0) + "  w1 is: " + str(w1) + "    w2 is: " + str(w2)
    return {'w0': w0, 'w1': w1, 'w2': w2}


def find_accuracy(test_data, weights):
    match = 0
    for test_case in test_data:
        test_input1 = float(test_case[0])
        test_input2 = float(test_case[1])
        expected_output = float(test_case[2])

        g_of_h = g_function(weights['w0'], weights['w1'], weights['w2'], test_input1, test_input2)
        if g_of_h <= 0.5:
            predicted_output = 0
        else:
            predicted_output = 1

        if expected_output == predicted_output:
            match += 1
    return float(match) / len(test_data) * 100


def n_fold_validation(data_set, n=10):
    total_accuracy = 0
    step = int(math.ceil(float(len(data_set)) / n))
    for start in range(1, len(data_set), step):
        test_set = []
        training_set = []

        for index in range(1, len(data_set)):
            if start <= index < (start + step):
                test_set.append(data_set[index])
            else:
                training_set.append(data_set[index])
        weights = train(training_set)
        accuracy = find_accuracy(test_set, weights)
        total_accuracy += accuracy
        print "Accuracy = " + str(accuracy)
    print "Average accuracy for n-folds: " + str(float(total_accuracy) / n)


# For Output:

print "\nN-fold cross validation for the data set (here, n=10)-> "
n_fold_validation(data_set, 10)

plt.plot(avg_error_plot, marker='o', linestyle='--', color='r', label='Error')
plt.xlabel('Epoch')
plt.ylabel('Average Error')
plt.title('Epoch Vs. Average Error for each of the n-folds')
plt.legend()
plt.show()


# AND gate validation:

with open('../and.csv', 'rb') as f:
    reader = csv.reader(f)
    or_data = list(reader)

avg_error_plot = []

and_weights = train(or_data)
plt.plot(avg_error_plot, marker='s', linestyle='-', color='b', label='Error')
plt.xlabel('Epoch')
plt.ylabel('Average Error')
plt.title('Epoch Vs. Average Error for AND gate')
plt.legend()
plt.show()


# OR gate validation:

with open('../or.csv', 'rb') as f:
    reader = csv.reader(f)
    or_data = list(reader)

avg_error_plot = []

or_weights = train(or_data)
plt.plot(avg_error_plot, marker='D', linestyle='-', color='g', label='Error')
plt.xlabel('Epoch')
plt.ylabel('Average Error')
plt.title('Epoch Vs. Average Error for OR gate')
plt.legend()
plt.show()


# NAND gate validation:

with open('../nand.csv', 'rb') as f:
    reader = csv.reader(f)
    nand_data = list(reader)

avg_error_plot = []

nand_weights = train(nand_data)
plt.plot(avg_error_plot, marker='x', linestyle='-', color='m', label='Error')
plt.xlabel('Epoch')
plt.ylabel('Average Error')
plt.title('Epoch Vs. Average Error for NAND gate')
plt.legend()
plt.show()


# NOR gate validation:

with open('../nor.csv', 'rb') as f:
    reader = csv.reader(f)
    nor_data = list(reader)

avg_error_plot = []

nor_weights = train(nor_data)
plt.plot(avg_error_plot, marker='h', linestyle='-', color='c', label='Error')
plt.xlabel('Epoch')
plt.ylabel('Average Error')
plt.title('Epoch Vs. Average Error for NOR gate')
plt.legend()
plt.show()


# XOR gate validation:

with open('../xor.csv', 'rb') as f:
    reader = csv.reader(f)
    xor_data = list(reader)

avg_error_plot = []

xor_weights = train(xor_data)
plt.plot(avg_error_plot, marker='^', linestyle='-', color='y', label='Error')
plt.xlabel('Epoch')
plt.ylabel('Average Error')
plt.title('Epoch Vs. Average Error for XOR gate')
plt.legend()
plt.show()