import sys
import time

languages = dict()

def languages_dict(name_file):
	file = open('library/'+ name_file)
	onstring = file.read().split('\n')[:-1]
	for item in onstring:
		key = item.split("	")[0]
		value = item.split("	")[1:]
		languages[key] = value

	file.close()
	return value

	
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
	
languages_dict('languages.txt')
hello_parts = language_type(param.lower())
hours = get_this_time()

print (hello_time (hello_parts, hours))
