def approximate_pi(n_terms):
    """
    Approximates the value of pi using the Leibniz formula 
    (Madhava-Leibniz Series) up to n_terms terms.
    """
    # Initialize the sum for pi/4
    pi_over_4_sum = 0.0
    
    # The series uses terms starting from k=0 up to k=n_terms-1
    for k in range(n_terms):
        # Calculate the k-th term: (-1)^k / (2k + 1)
        term = ((-1)**k) / (2 * k + 1)
        
        # Add the term to the running sum
        pi_over_4_sum += term
    
    # Multiply the sum by 4 to get the approximation of pi
    pi_approximation = 4 * pi_over_4_sum
    
    return pi_approximation
