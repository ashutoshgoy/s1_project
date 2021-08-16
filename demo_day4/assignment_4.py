text='Fare:$18,369 - $120,379*'
first_number=""
second_number=""
num=""
for txt in text:

    if txt>='0' and txt<='9':
       num=num+txt
    elif txt==',' and len(num)!=0:
       continue
    elif len(num)>=0:
        if len(first_number):
            second_number=num
        else:
            first_number=num
        num=""
    else:
        pass
if len(num):
     second_number=num
if int(first_number)>0 and int(second_number)>0:
    print(f"both {first_number } and {second_number} are greater than zero")
elif int(first_number)>0:
    print(f"{second_number } is less  than zero")
elif int(second_number)>0:
    print(f"{first_number } is less  than zero")
else:
    print(f"both number are less than zero")
