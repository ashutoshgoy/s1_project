
import re
text_value="Today is Monday while it was sunday yesterday"

value=re.search("day",text_value)
if value:
    print("Yes there is a match")
else:
    print("no match")

value=re.findall('day',text_value)
print(len(value))
print(value)
#to check the code



