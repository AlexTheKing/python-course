# Запустить это - modularity.py


# pkg - это пакет. На диске - это всего лишь папка с файлом __init__.py
# в пакете находятся модули - самостоятельные .py файлы


from pkg import *  # 

greet.say_hi("Alex")
farewell.say_bye("John")

'''
То же самое

from pkg import greet
from pkg import farewell

greet.say_hi("Alex")
farewell.say_bye("John")



То же самое

from pkg.greet import say_hi
from pkg.farewell import say_bye

say_hi("Alex")
say_bye("John")
'''