#MINI PROJECT
#DICTIONARY 
#program that manages a dictionary of word meanings.
#Functions in the program are 1.add a word 2.search a meaning 3. display all words 4.update meaning 5.delete word

dictionary = {

}
while True:
    print(" DICTIONARY  ")
    print("1.ADD A WORD" )
    print("2.SEARCH FOR MEANING")
    print("3.DISPLAY ALL WORDS")
    print("4.UPDATE MEANING")
    print("5.DELETE WORD")
    print("6.EXIT")

    option = int(input("ENTER THE OPTION TO ACCESS THE DICTIONARY: "))

    if option == 1:
        word = input("enter the word : ")
        meaning = input("enter the meaning of the word: ")
        dictionary.update({word:meaning})
        print("you have added a word and its meaning to the dictionary")
        print(dictionary)  
    elif option == 2:
        word = input("enter the word wanted to search ")
        if word in dictionary:
            print(f"MEANING OF THE WORD {word} is",dictionary.get(word))
        else:
            print(f"the word {word} not found")
    elif option == 3:
        print(f"the dictionary has following words and meaning : {dictionary}")
    elif option == 4:  
        word = input("enter the word to be updated : ")
        if word in dictionary:
            meaning = input("the meaning is : ")
            dictionary[word] = meaning
            print(f"the meaning of {word} is {meaning}")
        else:
            print("the entered word is not found")
    elif option == 5:
        word = input("enter the word which you want to delete in the dictionary : ")
        if word in dictionary:
            dictionary.pop(word)
            print(f"the word {word} is deleted from your dictionary")
        else:
            print(f"the word {word} is not found in the dictionary so enter the correct word to delete : ")
    elif option == 6:
        print("exiting from dictionary")
        break
    else:
        print("Invalid choice! Please enter a valid option.")         
    
    
    
    
    
   