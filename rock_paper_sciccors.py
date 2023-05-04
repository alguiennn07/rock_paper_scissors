from random import choice,shuffle
def juego(eleccion):
    options=["rock", "paper", "sciccors"]
    
    while True: 
        game=choice(options)
        if eleccion=="paper":
            game=choice(options)
            inp1=input("Press enter to play or write 'choose' to choose your option ")    
            print("I've chosen",game,end=". ")   
            if game==options[0]:
                print("I win because",eleccion,"beats",game) 
            if game== options[1]:
                print("Draw") 
            if game==options[2]:
                print("You win because",game,"beats",eleccion)
            elif "choose" in inp1:
                break
    
        elif eleccion=="rock":
            game=choice(options)
            inp2=input("Press enter to play or write 'choose' to choose your option ")
            print("I've chosen",game,end=". ")        
            if game==options[0]:
                print("Draw") 
            elif game== options[1]:
                print("You win because",game,"beats",eleccion) 
            elif game==options[2]:
                print("I win because",eleccion,"beats",game)
            elif "choose" in inp2:
                break
        elif eleccion=="scissors":
            game=choice(options)
            inp3=input("Press enter to play or write 'choose' to choose your option  ")

            print("I've chosen",game,end=". ")        
            if game==options[0]:
                print("I win because",eleccion,"beats",game) 
            elif game== options[1]:
                print("You win because",game,"beats",eleccion)
            elif game==options[2]:
                print("Draw")
            elif "choose" in inp3:
                break
        
        elif eleccion=="random":
            eleccion=choice(options)
            inp4=input("Press enter to play or write 'choose' to choose your option  ")
            print("I've chosen",game,end=". ")     
               
            
            if game==options[0] and eleccion== options[0]:
                print("Draw") 
            elif game== options[1] and eleccion==options[0]:
                print("I win because",eleccion,"beats",game) 
            elif game==options[2] and eleccion == options[0]:
                print("You win because",game,"beats",eleccion)
            elif "choose" in inp4:
                break
            
            if game==options[0] and eleccion== options[1]:
                print("I win because",eleccion,"beats",game) 
            elif game== options[1] and eleccion==options[1]:
                print("Draw") 
            elif game==options[2] and eleccion == options[1]:
                print("You win because",game,"beats",eleccion)
            
            if game==options[0] and eleccion== options[2]:
                print("You win because",game,"beats",eleccion) 
            elif game== options[1] and eleccion==options[2]:
                print("I win because",eleccion,"beats",game) 
            elif game==options[2] and eleccion == options[2]:
                print("Draw")
            
        else:
            print("Not available")
                
        
while True:
    juego(input("Choose: "))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
print("fdf")
if True:
    print("Dvxs")