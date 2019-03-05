import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--lang', type = str, default = 'en')
parser.add_argument('-d','--dict', type = str, default = 'library/languages.txt')
args = parser.parse_args()

def get_time():

	'''Возвращает текущее время компьютера'''

	return int(time.strftime('%H', time.localtime()))//6


def lang_open_file(name_file,keys):

	'''Принимает путь к файлу с словарём и сокращение языка.
		Разбирает файл словаря.
		Возвращает варианты ответов на выбраном языке.'''

	try:

		with open(name_file.rstrip(' '), 'r') as read_file:
			for item in read_file.readlines():
				pul = item.strip(r'\n').split(',')
				if keys in pul[0]:
					return pul[1:]
			keys = get_key_or_exit('Введите другой язык')
			return lang_open_file(name_file,keys)

	except FileNotFoundError:
		name_file = get_key_or_exit('Введите правильный путь словаря')
		return lang_open_file(name_file ,keys)
	
		
def get_key_or_exit(message):

	'''	просит ввести верное значение.
		возвращает ввод или выходит'''

	key = input(message+' или exit:\n')
	if key.lower() == 'exit' or not key:
		print('До свидания!')
		exit()
	else:
		return key


def hello(func1,func2):

	'''возвращает приветствие.
		func1 - функция с списком значений,
		func2 - функция с индексом'''

	return func1[func2].capitalize()+'!'

if __name__ == '__main__':
	print(hello(
				func2 = get_time(),
				func1 = lang_open_file(args.dict,args.lang)
				))
