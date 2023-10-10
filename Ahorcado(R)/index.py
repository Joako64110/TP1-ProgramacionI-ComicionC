#Importo los elementos necesarios para la ejecución del programa
import random
import fuctions

#Defino todas las variables que necesito
get_out= False
lifes= 6
word_guess= ""
words= ["pantalla", "bucle", "recursion", "disco rigido", "github", "windows", "internet", "teclado", "hardware", "software", "computadora", "sistema operativo", "lenguaje de programacion", "sentencia", "videojuegos", "aplicacion", "libreria", "mate"]

#Selecciono una palabra al azar dentro de la lista previamente establecida
word= random.choice(words)

#Preparo la variable de la palabra a adivinar para ser almacenada correctamente
word_guess= fuctions.fill_word_to_guess(word, word_guess)

#Cuerpo central del juego
while (lifes != 0 and get_out == False):
    #Verifico que aún queden letras por adivinar
    if "_" in word_guess:
        print(f"Vidas restantes: {lifes}     Palabra: {word_guess}")
        letter= input("Ingrese una letra: ").lower()

        #Verifico lo que el usuario ingresó
        if (fuctions.verification(letter, word, word_guess) == False):
            #(Caso en que lo que sea ingresado por el usuario no sea una letra o palabra:)
            print("-----<¡¡Ingrese SOLO una letra o palabra/as!!>-----")
        elif (fuctions.verification(letter, word, word_guess) == True):
            #(Caso en que la letra o palabra ingresada no coincida con la palabra a adivinar:)
            lifes, get_out= fuctions.wrong_letter_handler(lifes, get_out)
        else:
            #(Caso en que la letra o palabra ingresada concida con la palabra a adivinar:)
            word_guess= fuctions.verification(letter, word, word_guess)
    else:
        get_out= True

#Informo al usuario los resultados de sus intentos
fuctions.endgame(lifes, word_guess, word)