# Instructions

You are being asked to create a python function called `count_domains` found in [domain_count.py](/domain_count.py).

The function will take a list of 'domains'. It returns a list of tuples like (`domain`, `count`) sorted by the count descending. It also replaces `www` from the beginning of all domains (assuming it starts with `www`).

You can view the potential input and output values in the [test_scenarios.py](./test_scenarios.py) file.

Here's one example:

```python
first_domain = [
    "www.example.com", 
    "subdomain.example.org", 
    "test.example.co.uk", 
    "www.docs.example.com",
    "subdomain.example.org",
    "www.docs.example.com",
    "www.docs.example.com",
    "www.docs.example.com",
]

first_expected_output = [
    ('docs.example.com', 4), 
    ('subdomain.example.org', 2), 
    ('example.com', 1), 
    ('test.example.co.uk', 1)
]
```

# Success Criteria

The expecation is that your code be put into a PR into the `main` branch of any repository and the test case run in github actions would succeed. You can find the one [test case here](./.github/workflows/test_domain_function.yml)

Hint: The CI/CD pipeline might be broken!