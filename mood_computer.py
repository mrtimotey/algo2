import  random 
print("Я ощущаю вашу энергетику.  От  моего экрана не скрыто ни одно из  ваших чувств.") 
print("Итaк.  ваше настроение. .. ") 
a  =  random.randint(1, 3) 
if a  ==  1: 
    print(""" 
    |            |
    |    O  O    |
    |            |
    |            |
    |  \______/  |
    """)
elif a  ==  2: 
    print(""" 
    |            |
    |    O  O    |
    |            |
    |   ______   |
    |            |
    """)
elif a  ==  3: 
    print(""" 
    |            |
    |    O  O    |
    |            |
    |    _____   |
    |   /     \  |
    """) 
else:
    print("He бывает такого настроения! (Должно быть, вы совершенно не в себе.)") 
print ("...Но это только сегодня.") 
input("\n\nнажмите Enter, чтобы выйти") 
