from functions import blocks_world, water_jug, menu

while True:
    menu()
    choice = input("Εισάγετε την επιλογή σας [1-3]: ")
    if choice == '1':
        blocks_world()
    elif choice == '2':
        water_jug()
    elif choice == '3':
        break
    else:
        print('Εισάγετε ένα αριθμό από το 1 έως το 3')
