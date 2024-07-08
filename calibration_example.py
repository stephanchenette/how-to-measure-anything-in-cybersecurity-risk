# Calibration of Estimates
# Idea: Improve the accuracy of subjective estimates by calibrating them.
# Experiment: Python script to help users calibrate their probability estimates. This involves providing feedback on a series of estimation questions to improve accuracy over time.

import numpy as np
import pandas as pd

# Generate a set of true probabilities
np.random.seed(42)
true_probabilities = np.random.rand(10)

# Simulate user estimates
user_estimates = true_probabilities + np.random.normal(0, 0.1, 10)  # Adding some noise

# Calculate the calibration score
calibration_errors = (true_probabilities - user_estimates) ** 2
calibration_score = np.mean(calibration_errors)

# Display results
results = pd.DataFrame({
    'True Probability': true_probabilities,
    'User Estimate': user_estimates,
    'Error': calibration_errors
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Calibration Results", dataframe=results)
print("Calibration Score (mean squared error):", calibration_score)
