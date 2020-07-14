def update_save():
    print("Please enter the name of every champ you have level 7")
    champs = input(":")
    save_file = open("complete_champs.txt", "a")
    save_file.write(champs)

update_save()
