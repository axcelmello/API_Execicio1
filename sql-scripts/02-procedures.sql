CREATE OR REPLACE FUNCTION InsertPlayer(
    IN p_ID INT,
    IN p_Name VARCHAR(50),
    IN p_UserName VARCHAR(50),
    IN p_Country VARCHAR(2),
    IN p_IDTitle VARCHAR(2),
    IN p_IDStatus VARCHAR(2),
    IN p_RATING INT
)
RETURNS VOID AS
$$
BEGIN
    BEGIN
        -- Attempt to insert into PLAYER
        INSERT INTO PLAYER(IDPLAYER, Name, UserName, Country, IDTitle, IDStatus, RATING)
        VALUES (p_ID, p_Name, p_UserName, p_Country, p_IDTitle, p_IDStatus, p_RATING);
    EXCEPTION
        -- Catch any exception and perform the update
        WHEN OTHERS THEN
            UPDATE PLAYER
            SET IDTITLE = p_IDTitle, IDSTATUS = p_IDStatus, RATING = p_RATING
            WHERE IDPLAYER = p_ID;
    END;
END;
$$
LANGUAGE plpgsql;