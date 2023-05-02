import warnings

warnings.filterwarnings("ignore",
                        message="Support for FigureCanvases without a required_interactive_framework attribute was deprecated in Matplotlib 3.6 and will be removed two minor releases later.")
import numpy as np
import matplotlib.pyplot as plt


def sin(x):
    return np.sin(x)


def log(x):
    return np.log(x)


def poly_func(x):
    return np.cos(x) + np.sin(x) + np.exp(x)


def compute_coefficients(x, y):
    x = np.asarray(x).astype(float)
    y = np.asarray(y).astype(float)
    n = len(x)
    coefficients = []
    for i in range(n):
        coefficients.append(y[i])
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = float(coefficients[i] - coefficients[i - 1]) / float(x[i] - x[i - j])
    return np.array(coefficients)


def evaluate_polynomial(coefficients, x, r):
    x = np.asarray(x).astype(float)
    n = len(coefficients) - 1
    result = coefficients[n]
    for i in range(n - 1, -1, -1):
        result = result * (r - x[i]) + coefficients[i]
    return result


def plot_graph(x, coefficients, y, func):
    xnew = np.linspace(np.min(x), np.max(x), 200)
    ynew = [evaluate_polynomial(coefficients, x, i) for i in xnew]
    plt.plot(x, y, 'o', xnew, ynew, label="Interpolation")
    ylist = [func(xData) for xData in xnew]
    plt.plot(xnew, ylist, label="True function")
    plt.grid(True)
    plt.legend()
    plt.show()


def enter_data_points(func):
    x = np.asarray(input("Enter data points: ").split()).astype(int)
    y = np.array([func(x) for x in x])
    coefficients = compute_coefficients(x, y)
    plot_graph(x, coefficients, y, func)


while True:
    chosen_func = str(input("Select a function: \n"
                            "1) sin(x)\n"
                            "2) log(x)\n"
                            "3) cos(x) + sin(x) + e^x\n"
                            "Q) Exit\n"))
    if chosen_func == str(1):
        try:
            enter_data_points(sin)
        except Exception:
            print("Something went wrong")
    elif chosen_func == str(2):
        try:
            enter_data_points(log)
        except Exception:
            print("Something went wrong")
    elif chosen_func == str(3):
        try:
            enter_data_points(poly_func)
        except Exception:
            print("Something went wrong")
    elif chosen_func == "Q":
        break
    else:
        print("Invalid input, please try again")
