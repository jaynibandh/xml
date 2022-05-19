import re


TEXTO = "Var"
subject = "</Var>jioh"
p="<"+TEXTO+">"
print(p)
print(type(p))
print(type(TEXTO))
y=re.findall(rf"(</{re.escape(TEXTO)}>)", subject, re.IGNORECASE)
print(y)
y=re.findall(rf"\b(?=\w){re.escape(p)}(?!\w)", subject, re.IGNORECASE)
print(y)
i=re.findall(r"\b(?<=\w)%s\b(?!\w)" % p, subject, re.IGNORECASE)
print(i)
m=re.search(r"\b(?<=\w)" + p + "\b(?!\w)", subject, re.IGNORECASE)
print(m)