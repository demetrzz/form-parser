import requests

url = "http://localhost:8000/get_form/"
params = {
    "lead_email": "kek@mail.com",
    "user_phone": "+7 999 123 22 33",
    "date": "10.10.2010"
}

first_response = requests.post(url, params=params)
print(first_response.json())

params = {
    "test_field1": "kek@mail.com",
    "test_field2": "+7 999 123 22 33",
    "test_field3": "10.10.2010"
}

second_response = requests.post(url, params=params)
print(second_response.json())
