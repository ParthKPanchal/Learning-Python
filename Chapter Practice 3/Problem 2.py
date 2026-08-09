Letter = '''Dear <|Name|>
You are selected!
<|Date|>
            '''

name=input("Enter your name")
date=input("Enter todays date")
print(Letter.replace("<|Name|>",name).replace("<|Date|>",date))