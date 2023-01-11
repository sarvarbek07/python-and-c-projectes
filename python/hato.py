def game (n):
    if int(n)%2==0:
        return 'juft'
    return 'toq'
while True:
    j=input("raqam: ")
    if j=="stop":
        break
    
    print(game(j))