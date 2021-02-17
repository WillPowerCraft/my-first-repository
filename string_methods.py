# count
# count(<sub>, <start>, <end>)
# считает количество непересекающихся вхождений подстроки <sub> в исходную строку
s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ


# startswith()
# startswith(<suffix>, <start>, <end>)
# определяет начинается ли исходная строка подстрокой <suffix>.
# Если исходная строка начинается с подстроки <suffix>,
# метод возвращает значение True, а если нет, то  False
s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('baz'))


# endswith()
# endswith(<suffix>, <start>, <end>)
# определяет оканчивается ли исходная строка подстрокой <suffix>.
# Метод возвращает значение True если исходная строка
# оканчивается на подстроку <suffix> и False в противном случае.
s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))


# find(), rfind()
# find(<sub>, <start>, <end>)
# находит индекс первого вхождения подстроки <sub> в исходной строке.
# Если строка не содержит подстроки <sub>, то метод возвращает значение -1.
# Мы можем использовать данный метод наравне с оператором in для проверки:
# содержит ли заданная строка некоторую подстроку или нет.
# Метод rfind(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>),
# за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки.
# find - ищет слева направо, rfind - справа налево.
s = 'foo bar foo baz foo qux'
print(s.rfind('foo'))
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))


# index(), rindex()
# index(<sub>, <start>, <end>)
# идентичен методу find(<sub>, <start>, <end>), за тем исключением,
# что он вызывает ошибку  ValueError: substring not found
# во время выполнения программы, если подстрока <sub> не найдена.
#
# rindex(<sub>, <start>, <end>)
# идентичен методу index(<sub>, <start>, <end>), за тем исключением,
# что он ищет первое вхождение подстроки <sub> начиная с конца строки.
#
# Нафига они вообще нужны? Просто скипаю и юзаю find rfind пока кто-нибудь не объяснит.


# strip()
# возвращает копию строки, у которой удалены все пробелы в начале и конце строки.
s = '     foo bar foo baz foo qux      '
print(s.strip())
# lstrip() - тоже самое, но только в начале строки.
# rstrip() - тоже самое, но только в конце строки.
# Необязательный аргумент <chars> – это строка, которая определяет набор символов для удаления.
print(s.strip(' foo'))

# replace()
# replace(<old>, <new>)
# возвращает копию сроки со всеми вхождениями подстроки <old>, замененными на <new>.
s = 'foo bar foo baz foo qux'
print(s)
print(s.replace('foo', 'grault'))
# может принимать опциональный третий аргумент <count>, который определяет количество замен.
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))


# isalnum()
# определяет, состоит ли исходная строка из буквенно-цифровых символов.
# Метод возвращает значение True если исходная строка является непустой
# и состоит только из буквенно-цифровых символов и False в противном случае.
s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
# isalpha() - только буквы
# isdigit() - только цифры
# islower() - только строчные буквы, другие символы в игнор
# isupper() - только заглавные буквы, другие символы в игнор
# isspace() - только пробелы


# ФОРМАТИРОВАНИЕ СТРОК, примеры

# Этот кусок кода приведет к ошибке:

# age = 27
# txt = 'My name is Timur, I am ' + age
# print(txt)

# А этот кусок кода не приведет к ошибке, но это говнокод:
# age = 27
# txt = 'My name is Timur, I am ' + str(age)
# print(txt)

# Вот так запишут эту инфу питонеры:
# age = 27
# txt = 'My name is Timur, I am {}'.format(age)
# print(txt)
# пока нихера не понятно, но дальше нам всё объяснят (наверно)

# С помощью format разрабы пишут описание способностей и артефактов в дотке, подставляя значения переменных прям как в этом примере:
age = 27
name = 'Timur'
profession = 'math teacher'
# txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
# print(txt)

# Для удобства можно юзать порядковые номера в фигурных скобках начиная с 0:
# txt = 'My name is {0}, I am {1}, I work as a {2}'.format(name, age, profession)
# print(txt)
# Порядковые номера можно использовать повторно, если какую-то переменную нужно использовать несколько раз:
txt = 'My name is {0}, I am {1}, I work as a {2} {0} {1} {2} {0}'.format(name, age, profession)
print(txt)

# Еще более наглядный и понятный способ использовать переменные в выводимом тексте это f-строки
# написал перед строкой f - и всё, теперь в фигурных скобках можно писать код или переменные
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}. You are {age + 3}. You are a {profession}. You were a member of {affiliation}')


# Function ord - order - порядок
# позволяет определить код некоторого символа в таблице символов Unicode.
# Аргументом данной функции является одиночный символ.
num1 = ord('A')
num2 = ord('B')
num3 = ord('a')
print(num1, num2, num3)


# Function chr - char - символ
# позволяет определить по коду символа сам символ.
# Аргументом данной функции является численный код.
chr1 = chr(65)
chr2 = chr(75)
chr3 = chr(110)
print(chr1, chr2, chr3)

# Функции ord и chr взаимнообратными и для них справедливо равенство:
# chr(ord('A')) = 'A', ord(chr(65)) = 65

