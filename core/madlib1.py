
nelson_mandela_quote = "The greatest glory in living lies not in never falling, but in rising every time we fall."

steve_jobs_quote = "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking."

oprah_winfrey_quote = "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."

''' Let user choose which quote to practice '''
print ("----Game Begins----")
while (True):
    selection = input ("which quote would you want for the test? e.g. Nelson Mandela (A) / Steve Jobs (B) / Oprah Winfrey (C) \n")
    if (selection not in ["Nelson Mandela", "A", "Steve Jobs", "B", "Oprah Winfrey", "C"]):
        print("You haven't typed in a proper selection. Choose again!")
        print("!!!!!!!!")
    else:
        break

print("----User Selection----")
print("You selected = " + selection) 
''' Each selection will have 4 missing words '''

print("----QUOTE----")
missing_words_list = []

if (selection in ["Nelson Mandela", "A"]):
    print("The greatest __1__ in living __2__ not in never falling, but in __3__ every __4__ we fall.")
    missing_words_list.append("glory")
    missing_words_list.append("lies")
    missing_words_list.append("rising")
    missing_words_list.append("time")
    
elif (selection in ["Steve Jobs", "B"]):
    print("Your time is __1__, so don't waste it __2__ someone else's life. Don't be __3__ by dogma – which is living with the results of other people's __4__.")
    missing_words_list.append("limited")
    missing_words_list.append("living")
    missing_words_list.append("trapped")
    missing_words_list.append("thinking")
    
elif (selection in ["Oprah Winfrey", "C"]):
    print("If you look at what you have in __1__, you'll always have more. If you look at what you __2__ have in __3__, you'll never have __4__.")
    missing_words_list.append("life")
    missing_words_list.append("don't")
    missing_words_list.append("life")
    missing_words_list.append("enough")

print("--------")

#print(missing_words_list)
index_filled_in = []
matchWords = 0

while(True):
    try:
        if (len(index_filled_in) == 4):
            break
        else:
            entry_num = int(input("which blank you want to fill in? 1/2/3/4 -> "))
            entry_word = input("and, the word is? -> ")
    except ValueError:
        print("Warn: Choose a valid blank number to fill in <#>")
    else:
        if("exit" == entry_word):
            break
        if (entry_num in [1,2,3,4]):
            if (entry_num not in index_filled_in):
                index_filled_in.append(entry_num)
            elif (entry_num in index_filled_in):
                print("Warn: Already filled in...Select another blank number")
            
            if(entry_word == missing_words_list[entry_num-1]):
                matchWords += 1
        else:
            print("Warn: Choose a valid blank number to fill in <##>")


if (matchWords == len(missing_words_list)):
    print("Yayyy...YOU WIN!!!")
else:
    print("Sorry...Better luck next time!!!")