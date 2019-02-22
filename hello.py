import sys
import time

languages = {
	'ru' : ['доброй ночи','доброго утра','доброго дня','доброго вечера'],
	'en' : ['good night', 'good morning', 'good day', 'good night']
	}

	
def language_type():
	if param in languages:
		hello_parts = languages[param]
		return hello_parts
	else:
		print('Данный язык недоступен.\nпока что будет English')
		hello_parts = languages['en']
		return hello_parts

def get_this_time():
	hours = int(time.strftime("%H", time.localtime()))//6
	return hours

def hello_time_print():
	massege = hello_parts[hours]
	print (massege.capitalize()+"!")

if __name__ == "__main__":
	if len(sys.argv) > 1:	
		param = sys.argv[1]			
		param = param.replace('-','')
		
	else:
		param = 'en'

hello_parts = language_type()
hours = get_this_time()
hello_time_print()
