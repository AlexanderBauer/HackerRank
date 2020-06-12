SELECT s.Name
FROM Students AS s 
INNER JOIN Friends AS f ON s.ID = f.ID
INNER JOIN Packages AS p ON s.ID = p.ID
WHERE p.Salary < (SELECT Salary FROM Packages WHERE ID=f.Friend_id)
ORDER BY (SELECT Salary FROM Packages WHERE ID=f.Friend_id)