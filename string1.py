phrase='зима 32нео крестьянин торжествуя 42на на'
# надо оставить только те слова в которых нет чисел 
# разбить по словам метод split список слов
#  for word in phrase:
#    for letter in word:

new_phrase= ''.join((symbol for symbol in phrase if symbol.isalpha() or symbol==" "))
# print(new_phrase) #убрали числа
new= new_phrase.replace("нео"," ")   # заменили лишнее 1 слово
new1=new[0:28].capitalize()          # по индексу выбрали необходимый интервал и с заглавной буквы
print(new1)

# как можно удалить по индексу слова?
# как заменить несколько разных слов в одной строке?


