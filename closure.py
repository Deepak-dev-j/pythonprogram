#closure is a function having a acces in the to the scope of 
# its paretn function after the parent function has the return
def parent(person):
    coins=3
    def playgame():
        nonlocal coins
        coins -=1 

        if coins>1:
            print(f"{person} has {coins} coins")
        elif coins ==1:
            print(f"{person} has {coins} coin")
        else:
            print(f"{person} is out o coins")
    return playgame
joe = parent("joe")
jenny=parent("jenny")

joe()
joe()
joe()
joe()