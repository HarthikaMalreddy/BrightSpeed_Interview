from test_scenarios import (
    first_domain, 
    first_expected_output, 
    second_domain,
    second_expected_output, 
    third_domain,
    third_expected_output
)

from domain_count import count_domains

setup_values = [
    (first_domain, first_expected_output),
    (second_domain, second_expected_output),
    (third_domain, third_expected_output)
]

def test_domain():
    for domain, outcome in setup_values:
        output = count_domains(domain)

        print(f"Domain : {domain}, Output : {output}, Expected : {outcome}")

        assert output == outcome, f"Sorry, you provided {output} expected {outcome}"
       