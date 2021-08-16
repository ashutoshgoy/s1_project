word='banana'
#a-3
#n-2
for i in range(0,len(word)):
    count=1
    for j in range(i+1,len(word)):
        if word[i]==word[j]:
          count=count+1
          word=word[:j]+'0'+word[j+1:]




    if count >1 and word[i]!='0':
      print(f"{word[i]} count is {count}")



word='banana'
#1 -set it does not count duplicate values

#count


for char in set(word):
  count=word.count(char)
  if count > 1:
      print(char,":",count)



