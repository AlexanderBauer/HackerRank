SELECT DISTINCT company_code, founder, COUNT(DISTINCT(lead_manager_code)), COUNT(DISTINCT(senior_manager_code)), COUNT(DISTINCT(manager_code)), COUNT(DISTINCT(employee_code)) 
FROM company INNER JOIN Employee 
USING(company_code) 
GROUP BY company_code, founder 
ORDER BY company_code ASC;