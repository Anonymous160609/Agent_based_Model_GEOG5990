import requests 
import bs4

r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text

#instancize soup
soup = bs4.BeautifulSoup(content, 'html.parser') 

#Getting elements by ID or other attributes:
table = soup.find(id="yxz")
#tds = soup.find_all(attrs={"class" : "y"})
#print(tds)

#Getting all elements of a specific tag:
trs = table.find_all('tr')
del trs[0]
print(trs)

cds = []
for tr in trs:
    print(tr.text)
    m = tr.text[0] + tr.text[1]
    n = tr.text[2] + tr.text[3]
    cd = (float(m),float(n))
    cds.append(cd)
    
coords = []
for tr in trs:
    coord = []
    x = float(list(filter(str.isdigit,tr.find(attrs={"class" : "x"})))[0])
    y = float(list(filter(str.isdigit,tr.find(attrs={"class" : "y"})))[0])
    coord = (y,x)
    coords.append(coord)

