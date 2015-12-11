#/usr/bin/env python3
file = open('5', 'r')
text = file.read()

#filew = open('1.html','w')
#filew.write(text[0:text.find('div class="section section_form-answers">')])
#filew.close()
#print(len(text))
#print(len(newtext))

'''
Переменные:
1) id - id вопроса
2) question - заголовок вопроса
3) viewers - количество просмотров
4) answers - количество ответов
5) resolved - количество решений
6) subscribers - количество подписчиков
7) date - дата вопроса
8)
'''

# <meta property="og:url" content="https://toster.ru/q/274164">

#id = text[len('<meta property="og:url" content="https://toster.ru/q/'):len('<meta name="twitter:card"')]
id = text[text.find('<meta property="og:url" content="https://toster.ru/q/')+53:text.find('<meta name="twitter:card"')-3]
question = text[text.find('<meta property="og:title" content="')+35:text.find('<meta property="og:description"')-3]
viewers = text[text.find('<span class="question__views-count question__views-count_full">')+142:text.find('<div class="question__comments-link">')-91]
answers = text[text.find('<div class="section section_answers " id="answers" role="answers_section ">')+120:text.find('<ul class="content-list content-list_answers" id="answers_list">')-230]

#resolved = text[text.find(''):text.find('')]

#subscribers = text[text.find('subscribers_count'):text.find('</span',[text.find('subscribers_count')])]

i = text.find('subscribers_count')
i2 = text.find('</span>',i)
subscribers = text[i+101:i2-6]

i = text.find('Решения вопроса          <span class="section-header__counter" role="answers_counter">')
i2 = text.find('</span>',i)
resolved = text[i+86:i2]

date = text[text.find('time pubdate="" itemprop="dateCreated" datetime="')+49:text.find('time pubdate="" itemprop="dateCreated" datetime="')+68]


print("ID вопроса: 	["+id+"]")
print("Вопрос: 		["+question+"]")
print("Просмотры: 	["+viewers+"]")
print("Ответы: 		["+answers+"]")
print("Решения:		["+resolved+"]")
print("Подписчики: 	["+subscribers+"]")
print("Дата: 		["+date+"]")



#print(id)
#print("It's work!")
#print(text.find('<meta property="og:url" content="https://toster.ru/q/'))
#print(text.find('<meta name="twitter:card"'))
#print(text[1069:1131])
