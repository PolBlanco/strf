USE strf;
DROP PROCEDURE IF EXISTS main;
DELIMITER //
CREATE PROCEDURE main ()
BEGIN
	WHILE TRUE DO
		IF (SELECT key1_ FROM keys_) = 0 AND (SELECT key2_ FROM keys_) = 0 THEN
			IF (SELECT partida_empezada FROM partida_empezada) = false THEN
				UPDATE partida_empezada SET partida_empezada = TRUE;
				WHILE (SELECT chrono FROM chrono) != 0 DO
					IF (SELECT min(life) FROM fight) != 0 THEN
						CALL tiempo();
					ELSE
						CALL passwd(100000000, 99999999, @ps1, @ps2);
						CALL crear_partida(300, @ps1, @ps2);
					END IF;
			END WHILE;
            END IF;
		ELSE IF (SELECT COUNT(*) FROM fight) = 0 THEN
			CALL passwd(100000000, 99999999, @ps1, @ps2);
			CALL crear_partida(300, @ps1, @ps2);
			END IF;
		END IF;
    END WHILE;
END //
DELIMITER ;
#CALL main();