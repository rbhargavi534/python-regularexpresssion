import re

txt='The rain in spain'

res=re.search("^The.+Spain$",txt)#Match object
#res=re.search("^The.*Rome$",txt) #none

print(res)