from typing import List
from fastapi import FastAPI
from Models.player import Player

app = FastAPI()

@app.get("/")
def read_root():
    return {"Chess Api": "go to /doc to learn more."}

@app.post("/newplayer", status_code=201)
def insertplayer(players: List[Player]):
    for p in players:
        p.save()

@app.get("/player/{idplayer}", response_model=Player)
def getplayer(idplayer: int):
    return Player.getplayer(idplayer)

@app.delete("/deleteplayer/{idplayer}", status_code=204)
def deleteplayer(idplayer: int):
    Player.deleteplayer(idplayer)


# THIS URL ISN'T WORKING, BECAUSE CHESS.COM IS RETURNING A FORBIDDEN(403) TO PYTHON
# WHY THEY CHANGE FROM ONE DAY TO ANOTHER? DON'T KNOW MAYBE A SHOULD HAVE A BETTER LUCK NEXT TIME
"""
@app.get("/atualizardb")
def atualiza_db():

    dbconnection = connection.con
    dbcursor = connection.cur

    response = requests.get('https://api.chess.com/pub/leaderboards')
    print(response)
    json = response.json()
    print(json)
    for player in json['live_rapid']:
        idplayer = str(player.get('player_id', 'empty'))
        name = str(player.get('name', 'empty'))
        username = str(player.get('username', 'empty'))
        tcountry = str(player.get('country', 'empty'))
        idtitle = str(player.get('title', 'empty'))
        idstatus = str(player.get('status', 'empty'))
        rating = str(player.get('score', 'empty'))
        country = tcountry[-2:]

        dbstring = ("SELECT InsertPlayer( "
                    + str(idplayer)
                    + ", '" + name + "'"
                    + ", '" + username + "'"
                    + ", '" + country + "'"
                    + ", '" + idtitle + "'"
                    + ", '" + idstatus + "'"
                    + ", " + str(rating) + " )")

        dbcursor.execute(dbstring)
        dbconnection.commit()
        
"""