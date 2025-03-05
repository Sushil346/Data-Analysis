import math
import numpy as np
import matplotlib.pyplot as plt

# Load our data set
x_train = np.array([1.0, 2.0])   # features
y_train = np.array([300.0, 500.0])   # target value

# Function to calculate the cost
def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = cost + (f_wb - y[i])**2
    total_cost = 1 / (2 * m) * cost
    return total_cost

# Function to compute gradients
def compute_gradient(x, y, w, b): 
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0
    for i in range(m):  
        f_wb = w * x[i] + b
        dj_dw_i = (f_wb - y[i]) * x[i] 
        dj_db_i = f_wb - y[i]
        dj_db += dj_db_i
        dj_dw += dj_dw_i
    dj_dw = dj_dw / m
    dj_db = dj_db / m
    return dj_dw, dj_db

# Gradient descent function
def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function): 
    J_history = []
    P_history = []
    w = w_in
    b = b_in

    for i in range(num_iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)
        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        if i < 100000:   
            J_history.append(cost_function(x, y, w, b))

        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]:8.2f}   ")
        
    return w, b, J_history, P_history

# Initial values
initial_w = 0
initial_b = 0.0
iterations = 1000
alpha = 1.0e-2

# Running gradient descent
wfinal, bfinal, J_hist, P_hist = gradient_descent(x_train, y_train, initial_b, initial_w, alpha, iterations, compute_cost, compute_gradient)
print(f"(w,b) found by gradient descent: ({wfinal:8.4f},{bfinal:8.4f})")

# Plot cost versus iteration
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, figsize=(12,4))
ax1.plot(J_hist[:100])
ax2.plot(1000 + np.arange(len(J_hist[1000:])), J_hist[1000:])
ax1.set_title("Cost vs. iteration(start)")
ax2.set_title("Cost vs. iteration (end)")
ax1.set_ylabel('Cost')
ax2.set_ylabel('Cost') 
ax1.set_xlabel('iteration step')
ax2.set_xlabel('iteration step') 
plt.show()
