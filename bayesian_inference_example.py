# Bayesian Inference
# Idea: Apply Bayesian methods to update the probability of a cybersecurity event as new evidence is obtained.
# Experiment: Python script to perform Bayesian updating for a given cybersecurity event.

from scipy.stats import beta

# Prior distribution (Beta distribution parameters)
a_prior = 2
b_prior = 2

# Likelihood (new evidence)
new_evidence = [1, 0, 1, 1, 0, 1]  # 1 for occurrence, 0 for non-occurrence

# Update parameters based on new evidence
a_posterior = a_prior + sum(new_evidence)
b_posterior = b_prior + len(new_evidence) - sum(new_evidence)

# Posterior distribution
posterior_distribution = beta(a_posterior, b_posterior)

# Display the mean and credible interval of the posterior distribution
mean_posterior = posterior_distribution.mean()
credible_interval = posterior_distribution.interval(0.95)

print(f"Posterior Mean: {mean_posterior:.2f}")
print(f"95% Credible Interval: {credible_interval}")
