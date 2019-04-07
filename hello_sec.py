import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--lang', type = str, default = 'en')
parser.add_argument('-d','--dict', type = str, default = 'library/languages.txt')
args = parser.parse_args()


def get_time():
		'''Возвращает текущее время компьютера'''
		return int(time.strftime('%H', time.localtime()))//6


def counter(func,count_max = 5):
	def wrapped(key):
		count = 0
		while count < count_max:
			count +=1
			if key == 'exit':
				return
			elif func(key) == None:
				return
			elif type(func(key)) is str:	
				key = get_key_or_exit(func(key))
			else:
				return func(key)
	return wrapped


@counter
def languages_hello(name_file):
	'''Принимает путь к файлу с словарём.
		Разбирает файл и возвращает словарь'''	
	try:
		with open(name_file.rstrip(' '), 'r') as read_file:	
			data = {}			
			for item in read_file.readlines():
				space = item.strip('\n').split(',')					
				key, *value = space
				data[key] = value	
			return data
	except (FileNotFoundError, AttributeError):
		return 'Введите другой адрес словаря'


@counter
def find_lang(key):
	'''выполняет поиск нужного языка по ключу.
		возвращает значения приветсвий'''
	try:		
		if result == None:
			return
		else:
			return result[key]
	except KeyError:
		return 'Введите другой язык'



def get_key_or_exit(message):
	'''	просит ввести верное значение.
		возвращает ввод или выходит'''
	key = input(message + ' или exit:\n')
	if key.lower == 'exit':
		return 'exit'
	elif not key:
		print("Введено пустое значение")
		return
	else:
		return key

key = get_time()
result = languages_hello(args.dict)
data = find_lang(args.lang)

if __name__ == '__main__':
	if result and data != None:
		print("{}!".format(data[key].capitalize()))
	else:
		print('Выходим') 


		
		
