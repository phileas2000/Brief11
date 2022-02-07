import pytest

import requests
from bs4 import BeautifulSoup




@pytest.fixture
def soup(request):
    r=request.text
    return BeautifulSoup(r, 'html.parser')