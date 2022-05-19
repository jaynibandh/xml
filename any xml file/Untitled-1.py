import re
a="<DOCUMENT file=\"FAMPAT\">"
#print(a)
a=['<DOCUMENT file=\"FAMPAT\">','gbjkga','<']
b="<docum></docum> )<DOCUMENT file=\"FAMPAT\">  gjriowrgiohrio"
c="gjriowrgiohrio"
patent_begin_pos = re.findall(a[2],b)
#print(patent_begin_pos)
import re
s = b
print (s)
var_name = 'docum'
result = re.findall(rf"\b(?=\w)(<){var_name}(>)\b(?!\w)",s)
print (result)
result = re.findall('<docum>',s)
print(result)
var_name = ' b'
s2 = 'I hate books'
result = re.findall('(.+)'+var_name+'(.+)',s2)
#print (result)