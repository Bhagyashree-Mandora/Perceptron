import math
import csv
import random

with open('../Data.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)


def h_function(w0, w1, w2, x1, x2):
    return (w1 * x1) + (w2 * x2) + w0


def g_function(h):
    return float(1) / (1 + math.exp(-h))


def calculate_error(target_output, actual_output):
    return math.pow((target_output - actual_output), 2)


def derivative_of_g(g_result):
    return g_result * (1 - g_result)


def delta_w(g_result, input_value, target_output, actual_output, learning_rate=0.001):
    derivative = derivative_of_g(g_result)
    return learning_rate * (target_output - actual_output) * derivative * input_value


w0 = random.random()
w1 = random.random()
w2 = random.random()

print "w1 is: " + str(w1)
print "w2 is: " + str(w2)

error = 1
iteration = 0
while error > 0.0001 or iteration < 1000:
    delta_w0 = 0
    delta_w1 = 0
    delta_w2 = 0

    for row in data:
        x1 = float(row[0])
        x2 = float(row[1])
        target_output = float(row[2])

        h_result = h_function(w0, w1, w2, x1, x2)
        g_result = g_function(h_result)

        if g_result <= 0.5:
            actual_output = 0
        else:
            actual_output = 1

        print "Actual o/p: " + str(actual_output)
        error = calculate_error(target_output, actual_output)
        print "Error: " + str(error)

        if error != 0:
            delta_w0 = delta_w(g_result, 1, target_output, actual_output, learning_rate=0.001)
            delta_w1 = delta_w(g_result, x1, target_output, actual_output, learning_rate=0.001)
            delta_w2 = delta_w(g_result, x2, target_output, actual_output, learning_rate=0.001)
            w0 += delta_w0
            w1 += delta_w1
            w2 += delta_w2

        print "w1 is: " + str(w1)
        print "w2 is: " + str(w2)
        # print delta_w1
        # print delta_w2

    iteration += 1
