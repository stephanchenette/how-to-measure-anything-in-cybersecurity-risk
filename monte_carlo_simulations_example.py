# Monte Carlo Simulations
# Idea: Use Monte Carlo simulations to quantify uncertainties and model risks.
# Experiment: Python script to run Monte Carlo simulations for a given cybersecurity risk scenario.

import numpy as np

# Define a simple risk scenario: potential financial loss due to a cyber attack
np.random.seed(42)
n_simulations = 10000
potential_losses = np.random.normal(100000, 25000, n_simulations)  # Example losses in dollars

# Calculate statistics
mean_loss = np.mean(potential_losses)
std_loss = np.std(potential_losses)
percentile_95_loss = np.percentile(potential_losses, 95)

print(f"Mean Potential Loss: ${mean_loss:,.2f}")
print(f"Standard Deviation of Loss: ${std_loss:,.2f}")
print(f"95th Percentile Loss: ${percentile_95_loss:,.2f}")
