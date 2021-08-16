favorites_languages={'ram':['java'],'tim':['c'],'sam':['python','c#','go','java'],'brad':['ruby']}
for key,values in favorites_languages.items():

    if len(values) ==1:
        print(f"{key.title()}'s favorite language is")
        print(f"{values[0].title()}")


    else:
        print(f"{key.title()}'s favorite language  are-")
        for language in values:
            print(f"{language.title()}")


