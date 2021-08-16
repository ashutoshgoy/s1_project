word='racecar'

n=len(word)
s="true"
for i in range(int(len(word)/2)):
    if word[i]!=word[n-1-i]:
        s="false"
        break
if s=="true":
    print(f"{word} is   palindrome")
else:
    print(f"{word} is not a palindrome")
# list and reverse

word_to_list=list(word)
word_to_list.reverse()
if list(word)==word_to_list:
    print(f"{word} is a palindrome")
else:
    print(f"it is not a palindrome")