string = " twenty Two fifty two thirty Four and sixty five Fifty four "
string= string.lower()
string = string.split()

string2 = {}
for word in string:
   if word in string2 :
      string2[word]+=1
   else :
      string2[word] = 1
for word, frequency in string2.items():
   print(f"{word}:{frequency}")

