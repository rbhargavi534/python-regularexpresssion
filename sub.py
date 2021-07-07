import re

txt='The rain in Spain'

#res=re.sub("\s",'#',txt)
res=re.sub("\s",'#',txt,2) #max no of splits
print(res)