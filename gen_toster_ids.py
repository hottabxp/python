file = open('list.txt','a')
i = 0
while i < 100:
	print(i)
	file.write('http://toster.ru/q/' + str(i)+'\n')
file.close()

# скачать ссылки с помощью wget'a в 5 потоков
# cat list.txt | xargs -P 5 wget {}
