import re

# Рейзит тайп эрор если в строке есть буквы не из укр алфавита
user_str = input('Enter some ukrainian str:')
pattern = re.compile(r'[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ`1-9, .]+')
result = ''.join(pattern.findall(user_str))
if result != user_str:
    raise TypeError


# Рейзит тайп эрор если в строке есть буквы не из англ алфавита
# user_str = input('Enter english str:')
# pattern = re.compile(r'[a-zA-Z1-9, \.]+')
# result = ''.join(pattern.findall(user_str))
# if result != user_str:
#     raise TypeError
