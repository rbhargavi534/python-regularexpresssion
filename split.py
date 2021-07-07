import re

txt='The rain in Spain'

res=re.split("\s",txt)
#res=re.split("\s",txt,1) #max no of splits
print(res)