from bs4 import BeautifulSoup 

with open("../Wk 2/carviewer.lab02.html") as fp:
	soup = BeautifulSoup(fp,'html.parser')
	
print (soup.prettify())