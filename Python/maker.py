# A simple maker file that will make python file for a particular question
# It will webscrape the inital problem format as well as the question name given the problem number

from bs4 import BeautifulSoup
import requests
import re

# Will create a url for the leetcode question
n = input('What is the leetcode problem number? ')
url = 'https://google.com/search?q=LeetCode Problem' + n

# Will make a google search and find the raw url of the first link
google_req = requests.get(url).text
soup = BeautifulSoup(google_req, 'lxml')

# Will collect link and question title from the query
url = soup.find('div', class_='egMi0 kCrYT')
title = re.split('-', url.h3.text, 1)[0]
raw_url = url.a['href']
raw_url = re.split('=', raw_url, 1)[1]
clean_url = re.split('&', raw_url, 1)[0]

# Creates a file with the respective problem name
f = open(n + '.py', 'w')
f.write('# ' + title + '\n')
f.write('# Link: ' + clean_url + '\n')
f.close()

# Opens the leetcode link
problem_url = requests.get(clean_url).text
soup = BeautifulSoup(problem_url, 'lxml')

