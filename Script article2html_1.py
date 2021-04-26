from newspaper import Article

url = ('articles links')
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
