import random

def createBoard(lebar, tinggi):
    return [[' - ' for _ in range(lebar)] for _ in range(tinggi)]

# val = createBoard(5,5)
# print(val)

def gen_random(lebar, tinggi):
    attempts = 0
    while attempts < 3:
        yield (random.randint(0, lebar - 1), random.randint(0, tinggi - 1))
        attempts += 1
        
# val = gen_random(5,5)
# print(val)

def move(pos, step, lebar, tinggi):
    x, y = pos
    # print("x:"+str(x)+"-y:"+str(y))    #debug
    if step == "a" and x > 0: x -= 1
    if step == "d" and x < lebar-1 : x += 1
    if step == "w" and y > 0: y -= 1
    if step == "s" and y < tinggi-1 : y += 1
    return (x,y)
    
def main():
    print("~~ Selamat datang dipermainan board game pemrograman fungsional ~~")
    print("-------------------------------------------------------------------------")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)")
    print("Gunakan keyboard ASDW untuk bergerak")
    print("-------------------------------------------------------------------------")
    print("~~ Selamat Bermain ~~")
    
    lebar = int(input("Enter the board width : "))
    tinggi = int(input("Enter the board height : "))
    
    while True:
        regen = 'y'
        while regen == 'y':
            
            board = createBoard(lebar, tinggi)
            potition = gen_random(lebar, tinggi)
            # print("random generate : "+str(potition))             #debug
            bidak = next(potition)
            # print("bidak potition"+str(bidak))              #debug
            goal = next(potition)
            # print("goal potition"+str(goal))              #debug
            while bidak == goal:
                goal = next(potition)
                # print("goal potition"+str(goal))              #debug

                
            # print("bidak = "+str(bidak[1])+" , "+str(bidak[0])) #debug
            # print("goal = "+str(goal[1])+" , "+str(goal[0]))    #debug
            
            board[bidak[1]][bidak[2]] = ' A '
            board[goal[1]][goal[2]] = ' O '
            
            print("Let's play... This is your game board")
            for row in board:
                print(' '.join(row))
                
            regen = input("New possition (Y/N)? ").lower()

        steps = input("what is your move = ")
        # for idx, step in enumerate(steps):                  #mode 2(non-catch)
        for step in steps:
            board[bidak[1]][bidak[0]] = ' - ' 
            # print("bidak potition"+str(bidak))            #debug
            bidak = move(bidak, step, lebar, tinggi)
            # print("bidak potition"+str(bidak))             #debug
            board[bidak[1]][bidak[0]] = ' A '
            
            # if bidak == goal and idx == len(steps)-1:           #mode 2(non-catch)
            if bidak == goal:
                break
            
        for row in board:
            print(' '.join(row))
            
        if bidak == goal:
            print("you Win")    
        else:
            print("You lose")
            
        user = input("Wanna try again? (y/n)").lower()
        if user != 'y':
            print("See you again...")
            break
        
if __name__ == "__main__":
    main()