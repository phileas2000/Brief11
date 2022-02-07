
from bs4 import BeautifulSoup
from flask import Flask
import requests
import pytest
import time

url = 'http://localhost:5000/'



def soup(request):
    r=request.text
    return BeautifulSoup(r, 'html.parser')




def test_should_status_code_ok():
	
	response = requests.get(url)
	assert response.status_code == 200

def test_should_return_html():
	response = requests.get(url)
	data = response.text#Permet de décoder la data dans la requête
	print(data)
	assert "<form method=\"post\" action=\"/\" enctype=\"multipart/form-data\">" in data

def test_should_return_hand():
	username = 'testUser'
	password = 'testPassword'
	file =open("000000.jpeg","rb")
	response = requests.post(url,file.read())

	time.sleep(3) 
	s=soup(response)
	res=s.find(id="prediction")
	assert 'Hand'in res




test_should_status_code_ok()
test_should_return_html()
test_should_return_hand()