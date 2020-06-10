SELECT IF(
    (SELECT Grade FROM Grades WHERE Marks BETWEEN Min_Mark AND Max_Mark) >= 8,name,NULL), 
    (SELECT Grade FROM Grades WHERE Marks BETWEEN Min_Mark AND Max_Mark) AS Grade, Marks 
FROM Students 
ORDER BY Grade DESC, name ASC;