def approximate_pi(n_terms):
    pi_over_4_sum = 0.0
    
    for k in range(n_terms):
        # Calculate the k-th term: (-1)^k / (2k + 1)
        term = ((-1)**k) / (2 * k + 1)
        
        # Add the term to the running sum
        pi_over_4_sum += term
    
    # Multiply the sum by 4 to get the approximation of pi
    pi_approximation = 4 * pi_over_4_sum
    
    return pi_approximation
