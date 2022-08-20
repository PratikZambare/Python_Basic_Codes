khaana = ["Roti", "Pizza", "Sabji", "Chawal", "Burger"]
print(f'List items is {khaana} ')
user = input('Enter the choice you wanna search')

for item in khaana:
    if item == "Pizza":
        print('Your item is available in the list')
        break

else:
    print('Your item is not in the list')