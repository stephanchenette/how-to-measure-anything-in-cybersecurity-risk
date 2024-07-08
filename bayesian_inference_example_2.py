# Bayesian Inference with Multiple Iterations
# Explanation
# Initial Prior Distribution: The script starts with an initial Beta distribution representing the prior belief about the probability of the event.
# Bayesian Update Function: A function bayesian_update is defined to perform the Bayesian update based on new evidence.
# Iterations: The script processes multiple iterations, each with five new pieces of evidence. For each iteration, the posterior distribution is updated and plotted.
# Plotting: The script plots the prior distribution and the posterior distributions after each iteration to visualize how the beliefs are updated over time.
# Results
# Running this script will print the posterior mean and 95% credible interval after each iteration, showing how the probability estimate is refined as more evidence is incorporated. Additionally, it will generate a plot showing the prior and posterior distributions, allowing you to visually track the updates.
#
# This extended example demonstrates how Bayesian inference can be applied iteratively to update probability estimates as new evidence becomes available, which is particularly useful in dynamic environments like cybersecurity risk assessment.

from scipy.stats import beta
import matplotlib.pyplot as plt

# Function to perform Bayesian update
def bayesian_update(a_prior, b_prior, new_evidence):
    a_posterior = a_prior + sum(new_evidence)
    b_posterior = b_prior + len(new_evidence) - sum(new_evidence)
    return a_posterior, b_posterior

# Initial prior distribution (Beta distribution parameters)
a_prior = 2
b_prior = 2

# Initial prior
prior_distribution = beta(a_prior, b_prior)
iterations = [
    [1, 0, 1, 1, 0],  # Iteration 1
    [1, 1, 0, 0, 1],  # Iteration 2
    [0, 1, 1, 1, 0],  # Iteration 3
    [1, 1, 1, 0, 1],  # Iteration 4
]

# Plot initial prior distribution
x = np.linspace(0, 1, 100)
plt.plot(x, prior_distribution.pdf(x), label='Prior Distribution')

# Perform Bayesian updates for each iteration and plot posterior distributions
for i, new_evidence in enumerate(iterations):
    a_prior, b_prior = bayesian_update(a_prior, b_prior, new_evidence)
    posterior_distribution = beta(a_prior, b_prior)
    plt.plot(x, posterior_distribution.pdf(x), label=f'Posterior after Iteration {i+1}')
    
    # Display the mean and credible interval of the posterior distribution
    mean_posterior = posterior_distribution.mean()
    credible_interval = posterior_distribution.interval(0.95)
    print(f"Iteration {i+1}:")
    print(f"New Evidence: {new_evidence}")
    print(f"Posterior Mean: {mean_posterior:.2f}")
    print(f"95% Credible Interval: {credible_interval}\n")

plt.xlabel('Probability')
plt.ylabel('Density')
plt.legend()
plt.title('Bayesian Inference with Multiple Iterations')
plt.show()
