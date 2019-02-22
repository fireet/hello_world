import time
import sys

hours_of_day = time.strftime("%H", time.localtime())
hours = int (hours_of_day) // 6

# функция задает параметры аргумента и фразы приветствия
def hello_uni(var1, var2, night, morning, day, evening):
	verse = {var1, var2}	
	times.update ({0:night,1:morning,2:day,3:evening})
	if sys.argv[1] in verse:
		print (times.get(hours))
		exit()
#Проверка параметров
verse = {}
times = {}

	
if __name__ == "__main__":
	if len(sys.argv) > 1:	
		hello_uni('-ru', '-rus', 'Доброй ночи!', 'Доброго утра!', 'Доброго дня!', 'Доброго вечера!')
		hello_uni('-en', '-eng', 'Good night!', 'Good morning!', 'Good day!', 'Good evening!')
		if sys.argv[1] != verse:
			times.update ({0:'Good night!', 1:'Good morning!', 2:'Good day!', 3:'Good evening!'})
			print("такого языка пока не завезли, так что будет English")
			print (times.get(hours))	
		
	else:
		times.update ({0:'Good night!', 1:'Good morning!', 2:'Good day!', 3:'Good evening!'})
		print (times.get(hours))

