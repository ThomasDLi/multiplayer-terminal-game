from fastapi import FastAPI

app = FastAPI()

playerinfo = {}

@app.post("/send")
async def send_info(player:str, x: int, y:int):
    print(player, x, y)
    playerinfo.update({player : [x, y]})
    return "ok"

@app.get("/pos")
async def get_info():
    return playerinfo

@app.post("/del")
async def delete_info(player:str):
    playerinfo.pop(player)
    return "ok"