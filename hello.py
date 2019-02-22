import time
import sys

hours_of_day = time.strftime("%H", time.localtime())
hours = int (hours_of_day) // 6


# Русская часть


#Английская часть

def hello_uni(night, morning, day, evening):
		
	times.update ({0:night,1:morning,2:day,3:evening})

#Проверка парамtnhjd
times = {}

rus_verse = {'-ru', '-rus'}
eng_verse = {'-en', '-eng'}
	
if __name__ == "__main__":
	if len(sys.argv) > 1:	
		if sys.argv[1] in rus_verse:
			hello_uni('Доброй ночи!', 'Доброго утра!', 'Доброго дня!', 'Доброго вечера!')
		elif sys.argv[1] in eng_verse:
			hello_uni('Good night!', 'Good morning!', 'Good day!', 'Good evening!')
		else:
			print("Пока не завезли=( так что будет English")
			hello_uni('Good night!', 'Good morning!', 'Good day!', 'Good evening!')
	else:
		hello_uni('Good night!', 'Good morning!', 'Good day!', 'Good evening!')

print (times.get(hours))
