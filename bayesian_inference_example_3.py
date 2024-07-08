# Bayesian Inference for Multiple Capabilities
# Explanation
# Initial Prior Distribution: The script starts with initial Beta distributions for each capability (prevention, detection, alerting, logging).
# Bayesian Update Function: A function bayesian_update is defined to perform the Bayesian update based on new evidence. Each piece of evidence is a binary outcome (1 for success, 0 for failure) for each capability.
# Iterations: The script processes multiple iterations, each with new pieces of evidence for each capability. For each iteration, the posterior distribution for each capability is updated and plotted.
# Plotting: The script plots the prior distribution and the posterior distributions after each iteration for each capability to visualize how the probability estimates are updated over time.
# Results
# Running this script will print the posterior mean and 95% credible interval for each capability after each iteration, showing how the probability estimates of the system's capabilities are refined as more evidence is incorporated. Additionally, it will generate a plot showing the prior and posterior distributions for each capability, allowing you to visually track the updates.
#
# This approach helps in continuously updating the probability estimates of multiple capabilities (prevention, detection, alerting, logging) based on new evidence, making it a powerful tool for comprehensive cybersecurity risk assessment and improvement.

from scipy.stats import beta
import matplotlib.pyplot as plt

# Function to perform Bayesian update for each capability
def bayesian_update(a_prior, b_prior, new_evidence):
    a_posterior = a_prior + sum(new_evidence)
    b_posterior = b_prior + len(new_evidence) - sum(new_evidence)
    return a_posterior, b_posterior

# Initial prior distribution (Beta distribution parameters) for each capability
priors = {
    'prevention': {'a': 2, 'b': 2},
    'detection': {'a': 2, 'b': 2},
    'alerting': {'a': 2, 'b': 2},
    'logging': {'a': 2, 'b': 2}
}

# New evidence for each iteration (1 for success, 0 for failure)
iterations = [
    {'prevention': [1, 0, 1, 1, 0], 'detection': [1, 1, 0, 0, 1], 'alerting': [0, 1, 1, 1, 0], 'logging': [1, 1, 1, 0, 1]},
    {'prevention': [1, 1, 1, 0, 0], 'detection': [1, 0, 0, 1, 1], 'alerting': [1, 0, 1, 1, 0], 'logging': [1, 0, 0, 1, 1]},
    {'prevention': [0, 1, 0, 1, 1], 'detection': [1, 1, 1, 0, 0], 'alerting': [1, 1, 0, 0, 1], 'logging': [0, 1, 1, 1, 0]},
    {'prevention': [1, 0, 1, 0, 1], 'detection': [0, 1, 1, 1, 1], 'alerting': [0, 0, 1, 1, 1], 'logging': [1, 1, 0, 0, 1]},
]

# Plot initial prior distributions
x = np.linspace(0, 1, 100)
plt.figure(figsize=(12, 8))
for capability, params in priors.items():
    prior_distribution = beta(params['a'], params['b'])
    plt.plot(x, prior_distribution.pdf(x), label=f'{capability.capitalize()} Prior')

# Perform Bayesian updates for each capability and plot posterior distributions
for i, new_evidence in enumerate(iterations):
    for capability, evidence in new_evidence.items():
        a_prior = priors[capability]['a']
        b_prior = priors[capability]['b']
        a_posterior, b_posterior = bayesian_update(a_prior, b_prior, evidence)
        priors[capability]['a'] = a_posterior
        priors[capability]['b'] = b_posterior
        
        posterior_distribution = beta(a_posterior, b_posterior)
        plt.plot(x, posterior_distribution.pdf(x), label=f'{capability.capitalize()} Posterior after Iteration {i+1}')
        
        # Display the mean and credible interval of the posterior distribution
        mean_posterior = posterior_distribution.mean()
        credible_interval = posterior_distribution.interval(0.95)
        print(f"Iteration {i+1} - {capability.capitalize()}:")
        print(f"New Evidence: {evidence}")
        print(f"Posterior Mean: {mean_posterior:.2f}")
        print(f"95% Credible Interval: {credible_interval}\n")

plt.xlabel('Probability')
plt.ylabel('Density')
plt.legend()
plt.title('Bayesian Inference for Multiple Capabilities')
plt.show()
