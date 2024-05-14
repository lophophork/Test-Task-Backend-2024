SELECT
    Department.NAME AS Department,
    COUNT(Users.ID) AS NumberOfEmployees,
    AVG(Users.SALARY) AS AverageSalary
FROM
    Users
JOIN
    Department ON Users.DEPARTMENT_ID = Department.ID
GROUP BY
    Department.NAME;