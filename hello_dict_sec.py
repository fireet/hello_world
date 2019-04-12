import re


def mini_name():
	mini = input('Введите сокращение языка(2 буквы):\n')
	if len(mini) != 2:
		print('Вводимая строка должна состоять из 2х символов')
		return mini_name()
	return mini

def new_hello_words():
	space_of_hello = ['good night', 'good morning', 'good day', 'good evening']
	new_hello = []
	new_hello.append(mini_name())
	for item in space_of_hello:
		item = input('Введите {}:\n'.format(item))
		new_hello.append(item)
	return new_hello



def read_language_file(name_file,key):
	try:
		with open(name_file) as f:
			for line in f.readlines():
				if key in line[0:3]:
					print('Нельзя создать')
					return False
	except FileNotFoundError:
		new_language_file(name_file)

def new_language_file(name_file):
	with open(name_file, 'w') as f:
		print('Создан новый файл по адресу {}'.format(name_file))

def to_str(data):
	data = re.sub("[']",'',str(data).strip('[]').replace(' ', ''))+'\n'
	return data
	
		

def wright_language_file(name_file, new_language):
	try:
		with open(name_file, 'a') as f:
			f.write(new_language)
			print('Done')
	except FileNotFoundError:
		new_language_file(name_file)

def new_lang(file_name):
	new = new_hello_words()
	test = read_language_file(file_name,new[0])
	if test != False:
		new = to_str(new)
		wright_language_file(file_name, new)
		print('Готово!')
	else:
		print('увы это сокращение уже есть')

if __name__ == '__main__':
	new_lang('datafile.txt')
else:
	print('модуль импортирован')

