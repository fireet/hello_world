import time
import sys

hours_of_day = time.strftime("%H", time.localtime())
hours = int (hours_of_day)

# Русская часть

def hello_rus():
	
	night = "Доброй ночи!"
	morning = "Доброго утра!"
	day = "Доброго дня!"
	evening = "Доброго вечера!"

	times = {0:night,1:night,2:night,3:night, 4:night, 5:night,
		6:morning, 7:morning, 8:morning, 9:morning, 10:morning, 11:morning,
		12:day, 13:day, 14:day, 15:day, 16:day, 17:day, 
		18:evening, 19:evening, 20:evening, 21:evening, 22:evening, 23:evening}
		
	print (times.get(hours))

#Английская часть

def hello_eng():
	
	night = "Good night!"
	morning = "Good morning!"
	day = "Good day!"
	evening = "Good evening!"
	
	times = {0:night,1:night,2:night,3:night, 4:night, 5:night,
		6:morning, 7:morning, 8:morning, 9:morning, 10:morning, 11:morning,
		12:day, 13:day, 14:day, 15:day, 16:day, 17:day, 
		18:evening, 19:evening, 20:evening, 21:evening, 22:evening, 23:evening}
	
	print (times.get(hours))

#Проверка параметров
rus_verse = {'-ru', '-rus'}
eng_verse = {'-en', '-eng'}
	
if __name__ == "__main__":
	if len(sys.argv) > 1:	
		if sys.argv[1] in rus_verse:
			hello_rus()
		elif sys.argv[1] in eng_verse:
			hello_eng()
		else:
			print("Пока не завезли=( так что будет English")
			hello_eng()
	else:
		hello_eng()

