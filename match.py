import re

phone=['9550618590','5506185390','78655543','9856342278','3425673221']

for p in phone:
    if re.match(r'[7-9]{1}[0-9]{9}',p) and len(p)==10:
        print(p,'is valid')
    else:
        print(p,'is invalid')