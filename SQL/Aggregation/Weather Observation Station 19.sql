SELECT ROUND(
            SQRT(
                POWER(  ABS(MAX(LAT_N)  - MIN(LAT_N)),2)
                +POWER( ABS(MAX(LONG_W) - MIN(LONG_W)),2)
            )
        ,4) 
FROM STATION;