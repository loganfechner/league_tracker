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

def champ_tokens6():
    token_file = open("champ_tokens6.txt", 'r')
    temp_file = token_file.read()
    token_list = temp_file.split(',')
    return(token_list)

def champ_tokens7():
    token_file = open("champ_tokens7.txt", 'r')
    temp_file = token_file.read()
    token_list = temp_file.split(',')
    return(token_list)



def champ_eternals():
    return()

def main():
    lvl7count = 0
    for i in complete_champ_list():
        lvl7count += 1

    lvl7tokens = 0
    for i in champ_tokens7():
        lvl7tokens += 1
    lvl6tokens = 0
    for i in champ_tokens6():
        lvl6tokens += 1

    print(f"You currently have {lvl7count} champions level 7.")
    print(f"You currently have {lvl6tokens} mastery 6 champion tokens")
    print("You need to play:")
    lvl6tokensnodup = champ_tokens6()
    lvl6tokensnodup = list(dict.fromkeys(lvl6tokensnodup))
    for i in lvl6tokensnodup:
        print(i)
    print(f"You currently have {lvl7tokens} mastery 7 champion tokens.")
    print("You need to play:")
    lvl7tokensnodup = champ_tokens7()
    lvl7tokensnodup = list(dict.fromkeys(lvl7tokensnodup))
    for i in lvl7tokensnodup:
        print(i)




main()
