import sys
import time

languages = dict()

def languages_dict(name_file):

	try:
		with open('library/' + name_file + '.txt') as file_lib:
			
			getstring = file_lib.read().split('\n')[:-1]
			
			for item in getstring:
			
				key = item.split("	")[0]
				value = item.split("	")[1:]
				languages[key] = value
				
			return value
	except IOError:
		work_with_IOError()
		

def work_with_IOError():

	print('Файл не найден.')
	new_file = input('Введите название файла txt без расширения  или exit:\n')

	if new_file.lower() == 'exit':
		exit()
	else:
		languages_dict(new_file.lower())



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
		lang_library = sys.argv[2].replace('-','') if len(sys.argv) > 2 else 'languages'
		

languages_dict(lang_library)
hello_parts = language_type(param.lower())
hours = get_this_time()

print (hello_time (hello_parts, hours))
