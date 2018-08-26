from bs4 import BeautifulSoup

with open("index.html") as fp:
    css_soup = BeautifulSoup(fp, 'html.parser')
    #print(soup.prettify())
    for link in css_soup.find_all("a", class_="sister"):
        print(link.get('href'))
   # tag=css_soup.span['name']
   # print (tag)
    #for link in soup.find_all(id='searchlist'):
     #   print(link.get('href'))