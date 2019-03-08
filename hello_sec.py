import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--lang', type = str, default = 'en')
parser.add_argument('-d','--dict', type = str, default = 'library/languages.txt')
args = parser.parse_args()


def get_time():

		'''Возвращает текущее время компьютера'''

		return int(time.strftime('%H', time.localtime()))//6
	
	
def languages_hello(name_file):
	'''Принимает путь к файлу с словарём.
		Разбирает файл и возвращает словарь'''
	count = 0

	while count < count_max:
		if name_file != "exit":
			count +=1		
			try:	
				with open(name_file.rstrip(' '), 'r') as read_file:	
					data = {}			
					for item in read_file.readlines():
						space = item.strip('\n').split(',')					
						key = space[0]
						value = space[1:]
						data[key] = value	
					return data
			except FileNotFoundError:
				name_file = get_key_or_exit('Введите правильный путь словаря')
		else:
			return


def find_lang(data,key):
	'''выполняет аоиск нужного языка по ключу.
		возвращает значения приветсвий'''
	count = 0
	while count < count_max:
		if data and key != "exit":
			count +=1
			try:
				return data[key]
			except KeyError:
				key = get_key_or_exit("введите другой язык")
		else:
			return


def get_key_or_exit(message):
	'''	просит ввести верное значение.
		возвращает ввод или выходит'''
	while True:
		key = input(message+' или exit:\n')
		if key.lower == 'exit':
			return 'exit'
		elif not key:
			print("Введено пустое значение")
			return
		else:
			return key

count_max = 5
data = languages_hello(args.dict)
result = find_lang(data,args.lang)
key = get_time()


if __name__ == '__main__':
	
	if result and key != None:
		print("{}!".format(result[key].capitalize()))
	else:
		print("ну, может в другой раз")
		
		
