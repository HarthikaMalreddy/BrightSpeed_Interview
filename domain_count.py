from collections import defaultdict
def count_domains(domain_list):
    # A defaultdict to count domain occurrences
    counts = defaultdict(int)

    for domain in domain_list:
        if isinstance (domain, str) and domain: #Check if domain is a non-empty string
            # Remove "www." if exists
            clean_domain = domain[4:] if domain.startswith("www.") else domain
            counts[clean_domain] += 1 # Increment count
    # sort the counted domains by count in desc order
    sorted_count = sorted(counts.items(), key = lambda x : x[1], reverse = True)
    return sorted_count

   
