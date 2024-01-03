import numpy as np
import matplotlib.pyplot as plt

# Generate random data for demonstration
np.random.seed(42)
x_data = np.random.rand(100)
y_data = 2 * x_data + 1 + 0.1 * np.random.randn(100)  # Linear relationship with some noise

# Create subplots for 15 scatter plots (C_6^2 = 15 pairs)
fig, axes = plt.subplots(3, 5, figsize=(15, 9))
fig.suptitle('Scatter Plots with Linear Regression Lines', fontsize=16)

# Flatten the 3x5 axes array to simplify indexing
axes = axes.flatten()

# Define a function to plot a linear regression line
def plot_linear_regression(ax, x, y):
    # Calculate the coefficients of the linear regression line (y = mx + b)
    m, b = np.polyfit(x, y, 1)
    
    # Plot the scatter plot
    ax.scatter(x, y, label='Data')
    
    # Plot the linear regression line
    ax.plot(x, m*x + b, color='red', label=f'Linear Fit: y = {m:.2f}x + {b:.2f}')
    
    # Set labels and legend
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()

# Loop through the axes and plot the scatter plots with linear regression lines
for i in range(15):
    x_subset = np.random.rand(100)  # Replace with your actual data
    y_subset = 2 * x_subset + 1 + 0.1 * np.random.randn(100)  # Replace with your actual data
    plot_linear_regression(axes[i], x_subset, y_subset)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plots
plt.show()