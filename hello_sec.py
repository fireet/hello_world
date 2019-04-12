
import time
import argparse
import hello_dict_sec

parser = argparse.ArgumentParser()
parser.add_argument('-l','--lang', type = str, default = 'en')
parser.add_argument('-d','--dict', type = str, default = 'library/languages.txt')
args = parser.parse_args()


def get_time():
	'''Возвращает текущее время компьютера'''
	return int(time.strftime('%H', time.localtime()))//6

def exit_deko(func):
	"""Декоратор проверяющий значение ключа,
	если ключа нет - пропускает функцию"""
	def wrap(key):
		if key != None:
			try:
				return func(key)
			except TypeError:
				return
	return wrap
	
def counter(func,count_max = 5):
	"""Декоратор отвечающий за проверку введенных данных, 
	при введении 'exit' или 
	превышении количества попыток - возвращает'None'"""
	def wrapped(key):
		count = 0
		while count < count_max:
			count +=1
			if key == 'exit':
				return
			elif type(func(key)) == list:
				return func(key)	
			else:
				key = get_key_or_exit(func(key))
	return wrapped
	


@counter
def read_file(name_file):
	"""Функция отвечает за правильное чтение файла"""
	try:
		with open(name_file.rstrip(' '), 'r') as read_file:
			space = read_file.readlines()
			return space
	except (FileNotFoundError, AttributeError):
		return 'Введите другой адрес словаря'


@exit_deko #если файл так и не найден, функцию пропускаем
def languages_hello(space_file):
	'''Функция разбирает файл и возвращает словарь'''	
	data = {}			
	for item in space_file:
		space = item.strip('\n').split(',')					
		key, *value = space
		data[key] = value	
	return data
	

@exit_deko
@counter
def find_lang(key):
	'''выполняет поиск нужного языка по ключу.
		возвращает значения приветсвий'''
	try:		
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


def prepare_to_print():
	"""Функция форматирует данные перед печатью"""
	result = '{}!'.format(data[key].capitalize())
	return result

def help_to_us():
	answer = input("вы хотите добавить новый язык? y/n\n")
	if answer.lower() == 'y':
		hello_dict_sec.new_lang(input('Введите путь словаря:\n'))

file_name  = read_file(args.dict)
result = languages_hello(file_name)
data = find_lang(args.lang)
key = get_time()

if __name__ == '__main__':
	
	if data and key != None:
		message = prepare_to_print()
		print(message)
		help_to_us()
	else:
		print('Выходим') 
