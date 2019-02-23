import sys
import time

languages = {
	'ru' : ['доброй ночи','доброго утра','доброго дня','доброго вечера'],
	'en' : ['good night', 'good morning', 'good day', 'good night']
	}

	
def language_type(param):
	if param in languages:
		return languages[param]
	else:
		return languages['en']

def get_this_time():
	return int(time.strftime("%H", time.localtime()))//6
	

def hello_time (hello_parts, hours):
	return hello_parts[hours].capitalize()+"!"

if __name__ == "__main__":
	param = sys.argv[1].replace('-','') if len(sys.argv) > 1 else 'en'
	

hello_parts = language_type(param.lower())
hours = get_this_time()
print (hello_time (hello_parts, hours))
