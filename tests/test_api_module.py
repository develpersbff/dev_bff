import pytest
import openai
from src.api_module import api_call
import os
from dotenv import load_dotenv

sample_text = "The sea otter (Enhydra lutris) is a marine mammal native to the coasts of the northern and eastern North Pacific Ocean. Adult sea otters typically weigh between 14 and 45 kg (30 and 100 lb), making them the heaviest members of the weasel family, but among the smallest marine mammals. Unlike most marine mammals, the sea otter’s primary form of insulation is an exceptionally thick coat of fur, the densest in the animal kingdom. Although it can walk on land, the sea otter is capable of living exclusively in the ocean."



load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')


# Test to make sure that API call is working and that our API key is valid
def test_api_module_api_call_works():
    actual = api_call(sample_text)
    expected = True
    assert bool(actual) == expected

# Test makes an API call and checks to see if the summarized length of the article is between 1000 and 1500 characters long.
def test_api_module_api_result_length():
    actual = api_call("https://www.geeksforgeeks.org/queue-in-python/")
    expected = len(actual) >= 1000 and len(actual) <= 1500
    print(actual)
    print(len(actual))
    assert expected == True
