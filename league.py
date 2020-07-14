#reads the text file to detrmine which champs are not lvl 7 and outputs as a list
def uncomplete_champ_list():
    champion_file = open("uncomplete_champs.txt", 'r')
    temp_file = champion_file.read()
    return(temp_file.split(','))
#reads the text file to detrmine which champs are lvl 7 and outputs as a list
def complete_champ_list():
    champion_file = open("complete_champs.txt", 'r')
    temp_file = champion_file.read()
    return(temp_file.split(','))


#takes the two lists from above and compares them against one another to see which champions need to be removed from the uncompleted champions list this then writes to the uncompleted champions file and updates it
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

#creates a list of level 6 mastery tokens
def champ_tokens6():
    token_file = open("champ_tokens6.txt", 'r')
    temp_file = token_file.read()
    token_list = temp_file.split(',')
    return(token_list)
#creates a list of level 7 mastery tokens
def champ_tokens7():
    token_file = open("champ_tokens7.txt", 'r')
    temp_file = token_file.read()
    token_list = temp_file.split(',')
    return(token_list)

## IDEA: track eternals
def champ_eternals():
    return()


#main function that will output all of the data in a readable understandble manner
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



#calls the main function
main()
