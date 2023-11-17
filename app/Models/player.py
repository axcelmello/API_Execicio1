import connection
from pydantic import BaseModel

class Player(BaseModel):
    idplayer: int
    name: str
    username: str
    country: str
    idtitle: str
    idstatus: str
    rating: int

    def save(self):
        dbconnection = connection.con
        dbcursor = connection.cur
        dbstring = ("SELECT InsertPlayer( "
                    + str(self.idplayer)
                    + ", '" + self.name + "'"
                    + ", '" + self.username + "'"
                    + ", '" + self.country + "'"
                    + ", '" + self.idtitle + "'"
                    + ", '" + self.idstatus + "'"
                    + ", " + str(self.rating) + " )")
        dbcursor.execute(dbstring)
        dbconnection.commit()

    @classmethod
    def getplayer(cls, idplayer: int):
        dbconnection = connection.con
        dbcursor = connection.cur
        dbstring = ('SELECT * FROM player WHERE idplayer = ' + str(idplayer))
        dbcursor.execute(dbstring)
        player = dbcursor.fetchone()
        dbconnection.commit()

        return cls(
                   idplayer=player[0],
                   name=player[1],
                   username=player[2],
                   country=player[3],
                   idtitle=player[4],
                   idstatus=player[5],
                   rating=player[6]
                    )

    def deleteplayer(idplayer: int):
        dbconnection = connection.con
        dbcursor = connection.cur
        dbstring = ("DELETE FROM public.player WHERE idplayer = " + str(idplayer))
        dbcursor.execute(dbstring)
        dbconnection.commit()