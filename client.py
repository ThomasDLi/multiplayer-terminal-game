import requests

hosturl = "127.0.0.1:8000"

def send_info(plr, x, y):

    params = {

        "player" : plr,
        "x" : x,
        "y" : y,

    }

    requests.post(f"http://{hosturl}/send", params=params)

def get_info():

    otherpositions = requests.get(f"http://{hosturl}/pos")
    return(otherpositions.json())

area = [

    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]]

]

print("""
Simple Terminal-Based Multiplayer Game

     use W A S D + [enter] to move
     
          E + [enter] to quit
""")

player = input("CHOOSE YOUR CHARACTER [ONE LETTER]: ")[0]

curx = 0
cury = 0

while True:
    area = [

    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]],
    [["."], ["."], ["."], ["."], ["."], ["."]]

]

    send_info(player, curx, cury)
    allpos = get_info()
    pos = allpos.get(player)
    area[pos[1]][pos[0]] = [player]

    for keys in allpos.keys():
        pos = allpos.get(keys)
        area[pos[1]][pos[0]] = [keys]

    for y in range(14):
        print(area[y])
    print()

    wasd = input()

    if wasd == "w":
        cury -= 1
    if wasd == "a":
        curx -= 1
    if wasd == "s":
        cury += 1
    if wasd == "d":
        curx += 1
    if wasd == "e":

        prm = {

        "player" : player

        }
        otherpositions = requests.post(f"http://{hosturl}/del", params=prm)
        quit()
