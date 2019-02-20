import time

hours_of_day = time.strftime("%H", time.localtime())
hours_of_day = int (hours_of_day)

hello = "Доброго " #для русской части

if 6 > hours_of_day >= 0 :
	case = "night"
	case_ru = "ночи"
	hello = "Доброй "

elif 12 > hours_of_day >= 6 :
	case = "morning"
	case_ru = "утра"

elif 18 > hours_of_day >= 12 :
	case = "day"
	case_ru = "дня"

elif 24 > hours_of_day >= 18 :
	case = "evening"
	case_ru = "вечера"

massage = "Good " + case + ", Max!"
massage_ru = hello + case_ru + ", Макс!"

print(massage)
print(massage_ru)

