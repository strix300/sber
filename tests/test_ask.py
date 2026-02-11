import pytest
from agent import ask
from models import Prompt

def test_ask():
    test_text = "ssss sssssdffd gitlab sdsds, gitlab, gitlab, gitlab"
    result = ask(test_text)
    assert result == "ssss sssssdffd github sdsds, github, github, github"