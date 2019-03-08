import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--lang', type = str, default = 'en')
parser.add_argument('-d','--dict', type = str, default = 'library/languages.txt')
args = parser.parse_args()

def get_time():

	'''Возвращает текущее время компьютера'''

	return int(time.strftime('%H', time.localtime()))//6


def languages_hello(name_file,keys):

	'''Принимает путь к файлу с словарём и сокращение языка.
		Разбирает файл словаря.
		Возвращает варианты ответов на выбраном языке.'''
	while name_file and keys != None:
		try:	
			with open(name_file.rstrip(' '), 'r') as read_file:
				for item in read_file.readlines():
					data = item.strip('\n').split(',')
					if keys in data[0]:
						return data[1:]
				keys = get_key_or_exit('Введите другой язык')
				return languages_hello(name_file,keys)

		except FileNotFoundError:
			name_file = get_key_or_exit('Введите правильный путь словаря')
			return languages_hello(name_file, keys)

def get_key_or_exit(message):

	'''	просит ввести верное значение.
		возвращает ввод или выходит'''

	key = input(message+' или exit:\n')
	if not key:
		print("Введено пустое значение")
		return get_key_or_exit(message)
	elif key == 'exit':
		print('Пока-пока')
		return
	else:
		return key

data = languages_hello(args.dict,args.lang)
key = get_time()

if __name__ == '__main__':
	while data and key != None:
		print("{}!".format(data[key].capitalize()))
		break
		
