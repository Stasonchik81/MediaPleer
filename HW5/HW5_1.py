# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

MyString = 'I love Pythonabc andabc Java'
NotInString = 'abc'

MyString = MyString.replace('abc','')
print(MyString)
