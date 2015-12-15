import urllib.request
def replace_page(url):
#     url = 'http://toster.ru/q/11'
#     data = urllib.request.urlopen(url)
#     enc = data.info().get_content_charset() or 'latin1'
#     page = data.read().decode(enc)
    page = open(url,'r').read()


    i1 = page.find('Решения вопроса          <span class="section-header__counter" role="answers_counter">')
    i2 = page.find('Ответы на вопрос          <span class="section-header__counter" role="answers_counter">')
    
    counts = page[i1+68:i1+100]
    counts =  counts.replace('answers_counter','reshenie')
    counts =  counts.replace('/span','end')
    
    counts2 = page[i2+69:i2+100]
    counts2 =  counts2.replace('answers_counter','otvetu')
    counts2 =  counts2.replace('/span','end')
    
    
    
    print(counts)
    print(counts2)
    
    
    
    i1 = page.find('<nav class="question__tags">')
    i2 = page.find(u'title="Подписаться на вопрос"')
    print(i1)
    print(i2)
    
    print(len(page))
    
    new_page = open(url,'w')
    
    write_page = page[i1:i2]+'\n'+counts+'\n'+counts2
    new_page.write(write_page)
