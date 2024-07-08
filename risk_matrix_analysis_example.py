# Risk Matrix Analysis
# Idea: Translate qualitative risk assessments into quantitative measures using a risk matrix.
# Experiment: Python script to convert a qualitative risk matrix into quantitative values and analyze the overall risk.

import numpy as np
import pandas as pd

# Define risk levels and probabilities
risks = ['Low', 'Medium', 'High']
probabilities = [0.1, 0.5, 0.9]

# Define impact levels (in dollars)
impacts = [10000, 50000, 100000]

# Create a risk matrix
risk_matrix = pd.DataFrame({
    'Risk Level': risks,
    'Probability': probabilities,
    'Impact': impacts
})

# Calculate expected loss
risk_matrix['Expected Loss'] = risk_matrix['Probability'] * risk_matrix['Impact']

# Display risk matrix with expected losses
import ace_tools as tools; tools.display_dataframe_to_user(name="Risk Matrix", dataframe=risk_matrix)
print(risk_matrix)
