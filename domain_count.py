from collections import defaultdict

def count_domains(domain_list):
    """
    Count occurrences of domains in the given list and return a sorted list of tuples
    with the domain and its count, excluding the 'www.' prefix.

    Parameters:
    domain_list (list): A list of domain strings.

    Returns:
    list: A sorted list of tuples (domain, count) sorted by count in descending order.
    """
    
    # Initialize a defaultdict to count domain occurrences
    counts = defaultdict(int)

    for domain in domain_list:
        if isinstance(domain, str) and domain:  # Check if domain is a non-empty string
            clean_domain = domain[4:] if domain.startswith("www.") else domain  # Remove 'www.' prefix
            counts[clean_domain] += 1  # Increment count

    # Sort the counted domains by count in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_counts
