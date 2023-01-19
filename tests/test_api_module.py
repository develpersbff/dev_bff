import pytest
import openai
from src.api_module import api_call
import os
from dotenv import load_dotenv

sample_text = "The sea otter (Enhydra lutris) is a marine mammal native to the coasts of the northern and eastern North Pacific Ocean. Adult sea otters typically weigh between 14 and 45 kg (30 and 100 lb), making them the heaviest members of the weasel family, but among the smallest marine mammals. Unlike most marine mammals, the sea otter’s primary form of insulation is an exceptionally thick coat of fur, the densest in the animal kingdom. Although it can walk on land, the sea otter is capable of living exclusively in the ocean."

more_sample_text = "Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements."


load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')


# Test to make sure that API call is working and that our API key is valid
# @pytest.mark.skip("TODO")
def test_api_module_api_call_works():
    actual = api_call(sample_text)
    expected = True
    assert bool(actual) == expected


# Another test to check to see if the API call is working and our API key is valid
# @pytest.mark.skip("TODO")
def test_api_module_api_call_works_2():
    actual = api_call(more_sample_text)
    expected = True
    assert bool(actual) == expected


# Test makes an API call and checks to see if the summarized length of the article is between 800 and 1500 characters long.
# @pytest.mark.skip("TODO")
def test_api_module_api_result_length():
    actual = api_call("https://www.geeksforgeeks.org/queue-in-python/")
    expected = len(actual) >= 800 and len(actual) <= 1500
    assert expected == True


# Test makes another API call to check to see if the summarized length of the article is between 800 and 1500 characters long
# @pytest.mark.skip("TODO")
def test_api_module_api_result_length_2():
    actual = api_call("https://realpython.com/linked-lists-python/")
    expected = len(actual) >= 800 and len(actual) <= 1500
    assert expected == True
