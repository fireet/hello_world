import sys
import time


def languages_dict(name_file, keys):
	
		with open(name_file.replace(' ', '')) as file_lib:	
				
			for item in file_lib.read().split('\n')[:-1]:
				languages = {}	
				key = item.split(",")[0]
				value = item.split(",")[1:]
				languages[key] = value
				if key == keys:
					return value			
				
def get_this_time():

	return int(time.strftime("%H", time.localtime()))//6


def hello_time (hours, hello_parts):
	 
		return hello_parts[hours].capitalize()+"!"
	

if __name__ == "__main__":

	param = sys.argv[1].replace('-','') if len(sys.argv) > 1 else 'en'
	lang_lib = sys.argv[2].replace('-','') if len(sys.argv) > 2 else 'library/languages.txt'

hours = get_this_time()
hello_parts = languages_dict(lang_lib, param)

print (hello_time (hours, hello_parts))


