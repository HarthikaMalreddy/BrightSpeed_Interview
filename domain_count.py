# def count_domains(domain_list):
#     """
#     Your code goes in this block!!!!
#     """
#     return ""

from collections import Counter

def get_value_count_tuple(values):

    values = [
        x[4:]
        if x.startswith("www.")
        else x
        for x in values
    ]

    # Use Counter to count occurrences of each value
    value_counts = Counter(values)
    
    # Convert the counter dictionary to a list of tuples (value, count)
    value_count_tuples = list(value_counts.items())
    
    # Sort the list of tuples by the count (second element of the tuple)
    sorted_value_count_tuples = sorted(value_count_tuples, key=lambda x: x[1], reverse=True)
    
    return sorted_value_count_tuples
