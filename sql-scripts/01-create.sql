CREATE TABLE PLAYER(
	IDPLAYER INT NOT NULL,
	NAME VARCHAR(50) DEFAULT 'empty',
	USERNAME VARCHAR(50) NOT NULL UNIQUE,
	COUNTRY VARCHAR(2),
	IDTITLE VARCHAR(2),
	IDSTATUS VARCHAR(10),
	RATING INT,
	CONSTRAINT PK_PLAYER PRIMARY KEY(IDPLAYER)
);

CREATE TABLE GAMES(
	IDGAME BIGINT NOT NULL,
	USERWHITEPLAYER VARCHAR(50) NOT NULL,
	USERBLACKPLAYER VARCHAR(50) NOT NULL,
	WHITERATING INT,
	BLACKRATING INT,
	WHITESTATUS VARCHAR(20),
	BLACKSTATUS VARCHAR(20),
	CONSTRAINT PK_GAMES PRIMARY KEY(IDGAME),
	CONSTRAINT FK_GAMEWHITEPLAYER FOREIGN KEY (USERWHITEPLAYER) REFERENCES PLAYER(USERNAME),
	CONSTRAINT FK_GAMEBLACKPLAYER FOREIGN KEY (USERBLACKPLAYER) REFERENCES PLAYER(USERNAME)
);

CREATE TABLE PLAYERSTATS(
	USERNAME VARCHAR(50) NOT NULL,
	WHITEWINS INT,
	BLACKWINS INT,
	TOTALWINS INT GENERATED ALWAYS AS (WHITEWINS + BLACKWINS) STORED,
	LAST_UPDATE DATE,
	CONSTRAINT PK_PLAYERSTATS PRIMARY KEY(USERNAME),
	CONSTRAINT FK_STATSPLAYER FOREIGN KEY(USERNAME) REFERENCES PLAYER(USERNAME)
);
