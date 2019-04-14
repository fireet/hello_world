import re


"""работает только импортированным"""

def __read_language_file(name_file):
	'''читает файл построчно, возвращает файл в переменную'''
	with open(name_file) as f:
		return f.readlines()


def __wright_language_file(name_file, new_language):
	'''записывает новые данные в словарь'''
	with open(name_file, 'a') as f:
		f.write(new_language)
		print('Запись заверешена, Спасибо')


def __mini_name():
	'''запрашивает ввод сокращения'''

	print('Вводимая строка должна состоять из 2х символов')
	mini = input('Введите сокращение языка:\n')
	if len(mini)>2:
		mini = mini[:2]
		print('выбрано сокращение',mini)
	return mini


def __find_mini(name_file, mini_name):
	'''функция проверяет значение сокращения в файле словаря'''
	for line in name_file:
		if mini_name in line[:2]:
			print('сокращение уже есть')
			return ''
		else:
			return 

def __new_hello_words(mini_name):
	'''Функция принимает ввод 4х приветствий''' 
	space_of_hello = ['good night', 'good morning', 'good day', 'good evening']
	new_hello = []
	new_hello.append(mini_name)
	for item in space_of_hello:
		item = input('Введите {}:\n'.format(item))
		new_hello.append(item)
	return new_hello


def __to_str(data):
	'''Функция преобразует данные нового словаря в строку'''
	data = re.sub("[']",'',str(data).strip('[]').replace(' ', ''))+'\n'
	return data
	
		
def new_lang(file_name):
	'''функция для вызова в основной программе
		!требует рефракторинга!'''
	lang_file = __read_language_file(file_name)
	count = 0
	while True:
		count+=1
		mini = __mini_name()
		if __find_mini(lang_file, mini) == None:
			break
		elif count >= 5:
			print('not now')
			return
	new = __new_hello_words(mini)
	new = __to_str(new)
	__wright_language_file(file_name, new)
	print('Готово!')




if __name__ == '__main__':
	print('работает только из hello_sec.py')

	
		
