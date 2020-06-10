SELECT s.hacker_id, h.name
FROM Submissions AS s
INNER JOIN Challenges AS c ON c.challenge_id        =   s.challenge_id
INNER JOIN Difficulty AS d ON c.difficulty_level    =   d.difficulty_level
INNER JOIN Hackers AS h ON h.hacker_id              =   s.hacker_id
WHERE s.score = d.score
GROUP BY s.hacker_id, h.name
HAVING COUNT(s.hacker_id) > 1
ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC