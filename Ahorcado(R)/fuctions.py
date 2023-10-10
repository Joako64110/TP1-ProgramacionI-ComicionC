#Funcion que rellena la variable "word_guess"

def fill_word_to_guess (word, word_guess):
    word= list(word)
    for i in word:
        if i.isalpha() == True:
            word_guess+= "_ "
        else:
            word_guess+= "  "
    return word_guess


#Funcion que compara lo ingresado por el usuario con lo que tiene que adivinar

def verification (letter, word, word_guess):
    if (letter.isalpha() == True):
        if len(letter) == 1:
            if letter in word:
                return editor(letter, word_guess, word)
            else:
                return True
        elif letter == word:
            word_guess= letter
            return word_guess
        else:
            return True
    else:
        return False


#Funcion que efectua cambios en la variable a adivinar

def editor (letter, word_guess, word):
    word_guess= list(word_guess)
    for i in range(len(word)):
        if letter == word[i]:
            if i == 0:
                word_guess[i]= letter
            elif i == 1:
                word_guess[2]= letter
            else:
                word_guess[i * 2]= letter
    word_guess= "".join(word_guess)
    return word_guess


#Funcion que maneja el error de letra

def wrong_letter_handler (lifes, get_out):
    lifes-= 1
    if lifes > 0:
        print("Esa letra no se encuentra en ésta palabra; -1 vida")
    else:
        get_out= True
    return lifes, get_out


#Funcion que imprime el resultado final del juego

def endgame (lifes, word_guess, word):
    if lifes > 0:
        print(f"<<<!!!ENHORABUENA!!!>>>")
        print(f"¡¡La palabra fue encontrada!!")
        print(f"Palabra: {word}")
    else:
        print(f"<<<SIN VIDAS RESTANTES>>>")
        print(f"Se ha quedado sin vidas para seguir intentando :(")
        print(f"Palabra: {word}")