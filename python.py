import string
import re
from nltk.corpus import stopwords
f=open("Beyond the Wall of Sleep.txt","r",encoding='utf-8')
text1=f.read()
text1=text1.lower()
part1= text1.split()
part1 = re.split(r'\W+', text1)
table1 = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table1) for w in part1]
stop_words = set(stopwords.words('english'))
part1 = [w for w in part1 if not w in stop_words]
t=open("Pride and Prejudice.txt", "r",encoding='utf-8')
text2=t.read()
text2=text2.lower()
part2 = text2.split()
part2 = re.split(r'\W+', text2)
table2 = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table2) for w in part2]
stop_words = set(stopwords.words('english'))
part2= [w for w in part2 if not w in stop_words]
part1=[w for w in part1 if not w=='']
part2=[w for w in part2 if not w=='']
similarity = [x for x in part2 if x in part1]
sim = set(similarity)
print(part1)
print(part2)
print(sim)
print(len(sim))
