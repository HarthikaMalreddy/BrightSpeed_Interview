
### this is the first batch of scenarios for testing
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

# this is the second batch of scenarios for testing
second_domain  = [
    "www.example1@gmail.com",
    "www.example1@gmail.com",
    "example1@gmail.com",
    "www.example1@gmail.com",
    "example2@yahoo.com",
    "example2@yahoo.com",
    "www.example2@yahoo.com",
    "www.example3@outlook.com",
    "example3@outlook.com",
    "www.example3@outlook.com"
]

second_expected_output = [
    ('example1@gmail.com', 4), 
    ('example2@yahoo.com', 3), 
    ('example3@outlook.com', 3)
]

# this is the thrid batch of scenarios for testing

third_domain  = [
    "www.some-fake-domain@yougotthis.com",
]

third_expected_output = [('some-fake-domain@yougotthis.com', 1)]