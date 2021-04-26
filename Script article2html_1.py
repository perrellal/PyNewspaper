from newspaper import Article

url = ('https://www.ilpost.it/2021/04/25/governo-draghi-recovery-fund/',
       'https://www.ilpost.it/2021/04/26/vaccinati-stati-uniti-unione-europea-estate-ursula-von-der-leyen/',
       'https://www.ilpost.it/2021/04/26/elezioni-albania-rama-vantaggio/')
body = ''
def WriteArticle(current_url):
    a = Article(current_url)
    a.download()
    a.parse()
    title = a.title
    content = a.text
    date = str(a.publish_date)
    text = '''
    <h1>'''+title+'''</h1>
    <h3> Autore </h3>
    <h4>'''+date+'''</h4>
    <p>''' +content+ '''</p>
    '''    
    return text

for i in range(len(url)):
    current_url=url[i]
    new_text = WriteArticle(current_url)
    body = body + new_text
    
text =   '''
    <html>
        <body>
            '''+body+'''
        </body>
    </html>'''     
file = open("sample.html","w")
file.write(text)
file.close()
