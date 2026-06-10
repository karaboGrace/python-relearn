birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True :
    print("enter a name(blank to quit)")
    name=input()
    if name == "" :
        break
    if name in birthdays:
        print(birthdays[name] + "is the birthday of" + name)
    else:
        print('I do not have birthday informationfor' + name )
        print('enter birthday information of' + name)
        bday = input()
        birthdays[name] =  bday
        print("birthdays datatbase updated")
        
