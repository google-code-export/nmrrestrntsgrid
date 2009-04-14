-- live results from filesystem.
SELECT * FROM OverviewAll 
    into OUTFILE 
	'/Users/jd/Desktop/Werk/NRG_Paper/overviewAll.csv'
	FIELDS TERMINATED BY ',' 
	OPTIONALLY ENCLOSED BY '\"'	
	LINES  TERMINATED BY '\n';
	

