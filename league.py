def uncomplete_champ_list():
    champion_file = open("uncomplete_champs.txt", 'r')
    temp_file = champion_file.read()
    return(temp_file.split(','))
def complete_champ_list():
    champion_file = open("complete_champs.txt", 'r')
    temp_file = champion_file.read()
    return(temp_file.split(','))



def disparity_check():
    temp1 = ''
    temp2 = ''
    complete_champs = complete_champ_list()
    uncomplete_champs = uncomplete_champ_list()
    for i in complete_champs:
        temp1 = i
        for i in uncomplete_champs:
            temp2 = i
            if temp1 == temp2:
                print(f"Removing {temp1} from completed champs list")
                uncomplete_champs.remove(temp2)
    champion_file = open("uncomplete_champs.txt", "w+")

    temp_string = ','.join(uncomplete_champs)
    champion_file.write(temp_string)


def champ_eternals():
    
#print(uncomplete_champ_list())
#print(complete_champ_list())
disparity_check()
