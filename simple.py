from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

## ul - unoredered list li = list item

simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')

print(simple_soup.find('h1').string)

def find_list():
    list_content =simple_soup.find_all('li') 
    list_items = [e.string for e in list_content]
    print(list_items)

def find_paragraph():
    para = simple_soup.find('p',{'class':'subtitle'}) 
    print(para.string)

def find_other():
    other = simple_soup.find_all('p')
    otherp = [ p for p in other if 'subtitle' not in p.attrs.get('class',[])]
    print(otherp[0].string)

find_list()
find_paragraph()
find_other()
