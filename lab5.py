
#1
'''
import re
txt = input()
result = re.search(r'ab*', txt)

print(result)
'''
#2
'''
import re
txt = input()
result = re.search(r'ab{2,3}', txt)

print(result)
'''
#3
'''
import re
txt = input()
result = re.findall(r'\b[a-z]+_[a-z]+\b', txt)

print(result)
'''
#4
'''
import re
txt = input()
final = re.findall(r'\b[A-Z]{1}[a-z]+\b', txt)
print(final)
#5
import re
txt = input()
final = re.findall(r'a.*b$', txt)
print(final)'''
#6
'''
import re
txt = input()
final = re.sub(r'\s|\,|\.',':', txt)
print(final)'''
#7

import re
txt = input()

final = re.sub(r'_([a-z]){1}',lambda match: match.group(1).upper(), txt)
print(final)
#8
'''
import re
txt = input()
final = re.split('[A-Z]', txt)
print(final)

#9
import re
txt = input()
final = re.sub('[A-Z]',' ', txt)
print(final)'''
#10
import re
text = input()
res = re.sub(r'([A-Z]){1}', lambda match: "_" + match.group(1).lower(), text).lstrip('_')
print(res)