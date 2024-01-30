# Import Counter
from collections import Counter
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


# Leer el contenido del archivo .txt
with open('MountyScene01.txt', 'r', encoding='utf-8') as file:
    article = file.read()

tokens= [w for w in word_tokenize(article.lower())
         if w.isalpha()
         ]
no_stops=[t for t in tokens
           if t not in stopwords.words('English')
           ]
print("Selected Tokens")
print(tokens)            
countedTokesn=Counter(tokens)
countedNoStops=Counter(no_stops).most_common(20)
CommonTk=countedTokesn.most_common(10)
print("Common tokens")
print(CommonTk)
print("No Strops")
print(countedNoStops)
words, counts = zip(*countedNoStops)
# Rotar las etiquetas del eje x en 45 grados
# Añadir etiquetas sobre las columnas
for i, count in enumerate(counts):
    plt.text(i, count + 0.5, str(count), ha='center', va='bottom')
plt.title("Palabras más empleadas en Monty Python and the Holy Grail (O.V.) (Scene 1) ")    
plt.xticks(rotation=45)
plt.bar(words, counts)
plt.xlabel("words")
plt.ylabel("counts")
plt.show()
