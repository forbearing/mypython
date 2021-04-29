#!/usr/bin/env python3

# from bs4 import BeautifulSoup

# html = '''
    # <html><head><title>The Document's story</title></head>
    # <body>
    # <p class="title" name="dromouse"><b>The hybfkuf's storage</b></p>
    # <p class="story">Once upon a time there were three title sistes
    # <a href="http://www.hybfkuf.com/wokao" id="link1"</a>
    # <a href="http://www.hybfkuf.com/hello" id="link2"</a>
    # <a href="http://www.hybfkuf.com/linux" id="link3"</a>
    # and they lived at the botton of a weel</p>
    # <p class="python">...</p>
# '''

# soup = BeautifulSoup(html, 'lxml')
# print(soup.p)
# print(soup.p['name'])
# print(soup.p['class'])
# print(soup.p.string)


html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class='list' id='list-1'>
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

# from bs4 import BeautifulSoup
# soup =  BeautifulSoup(html, 'lxml')
# #print(soup.find_all('ul'))
# print(soup.find_all('ul')[0])
# print(type(soup.find_all('ul')[0]))

# from bs4 import  BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.find_all('ul'):
    # print(ul.find_all('li'))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text='Foo'))

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('li'):
    print(ul.get_text())
