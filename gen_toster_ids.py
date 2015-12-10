file = open('list.txt','a')
i = 0
while i < 100:
	print(i)
	file.write('http://toster.ru/q/' + str(i)+'\n')
file.close()
