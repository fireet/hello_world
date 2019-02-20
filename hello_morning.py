import time

hours_of_day = time.strftime("%H", time.localtime())
hours_of_day = int (hours_of_day)

#списки приветствий на разных языках
word_rus = ("Доброй ночи", "Доброго утра", "Доброго дня", "Доброго вечера")
word_eng = ("Good night", "Good morning", "Good day", "Good evening") 

def lang_moment(lang):
	if 0 <= hours_of_day < 6:
		moment = lang[0]
	elif 6 <= hours_of_day < 12:
		moment = lang[1]
	elif 12 <= hours_of_day <18:
		moment = lang[2]
	elif 18 <= hours_of_day < 24:
		moment = lang[3]
	message = "%s, Max!"% moment
	print (message)

print("Выберите номер языка\n 1. English\n 2. Русский")
lang =  int(input())

if lang == 1:
	print("Your choise - English")
	lang = word_eng
elif lang == 2:
	print("Вы выбрали - Русский")
	lang = word_rus
else:
	print("Такого языка к нам не завезли, попробуйте через месяцок")
	exit()

lang_moment(lang)







