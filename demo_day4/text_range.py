text='Fare: $18,369-$120,379*'
text_range=text[6:]
print(text_range)
special_chars='$,*'
new_text_range=''


for value in text_range:
    if value in special_chars:
        continue
    else:
        new_text_range=new_text_range+value
print(new_text_range)
value1=int(new_text_range.split('-')[0])
value2=int(new_text_range.split('-')[1])
if value1 >0  and value2 >0:
  print("Both the price values are greater than 0")
else:
  print("One of the values is not greater than 0")
