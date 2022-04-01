from lib2to3.pgen2 import driver
from selenium import webdriver

path='./webdriver/chromedriver.exe'
driver = webdriver.Chrome(path)
