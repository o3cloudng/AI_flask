from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'


#Open connection grabbing the page
uClient = uReq(my_url)

page_html = uClient.read()

#Close the connection
uClient.close()

#HTML Parser
page_soup = soup(page_html, "html.parser")

# print(page_soup.h1)
#Grab each product on the page
containers = page_soup.findAll("div",{"class":"item-container"})

#create a file
filename = "product,csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)


for container in containers:
	#Brand Name
	brand = container.a.img["title"] 

	title_container = container.findAll("a", {"class":"item-title"})
	# Name of product
	product_name = title_container[0].text
	#Shipping
	shipping_container = container.findAll("li", {"class": "price-note"})
	shipping_container.span[0].text.strip()

	print(brand)
	print(product_name)
	pring(shipping_container)

	f.write(brand+ "," + product_name.replace(",","|") + shipping +"\n")

f.close()





# print('Hello Web scraper')