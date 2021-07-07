import re


text='$100 $200 $300 $400'

print(re.findall(r'\$',text))

t2='The quick brown fox jumps over the little lazy dog'

print(re.findall(r'\b...\b',t2))

res=re.findall(r'fox|dog|bear',t2)
print(res)

res=re.findall(r'[aeiou]',t2)
print(res)