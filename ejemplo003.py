import string
from nltk.corpus import stopwords

# print(string.punctuation)
stopword=stopwords.words('spanish')
print(type(stopword))
print(stopword.index('pueden'))
# listaStop=list(stopword)
# print(type(listaStop))
# print(listaStop.index('como'))
# # print('a' in stopword)
# for stp in stopword:
#     print(stp)
# print(stopword.index('son'))
# # print(type(listaStop))
# # print(listaStop.index('tengas'))

# print('de' in stopword)