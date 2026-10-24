-- DROP TABLE IF EXISTS employees;

-- CREATE TABLE employees (
--     id INT PRIMARY KEY IDENTITY,
--     name NVARCHAR(50),
--     surname NVARCHAR(50),
--     position NVARCHAR(50),
--     email NVARCHAR(100),
--     city NVARCHAR(50),
--     salary INT
-- );

-- INSERT INTO employees (name, surname, position, email, city, salary) VALUES
-- ('Alice','Johnson','Manager','alice.johnson@gmail.com','Tashkent',5500),
-- ('Bob','Smith','Developer','bob.smith@yahoo.com','London',4200),
-- ('Charlie','Brown','Designer','charlie.brown@gmail.com','Paris',3800),
-- ('Diana','Miller','Tester','diana.miller@hotmail.com','Berlin',3100),
-- ('Eve','Davis','Developer','eve.davis@outlook.com','Madrid',4500),
-- ('Frank','Wilson','Manager','frank.wilson@gmail.com','New York',6000),
-- ('Grace','Taylor','Analyst','grace.taylor@gmail.com','Tashkent',3900),
-- ('Hank','Anderson','Support','hank.anderson@yahoo.com','Rome',3000),
-- ('Ivy','Thomas','Developer','ivy.thomas@gmail.com','Tokyo',4700),
-- ('Jack','Moore','Designer','jack.moore@outlook.com','Seoul',3400),
-- ('Karen','White','Manager','karen.white@gmail.com','Tashkent',5800),
-- ('Leo','Martin','Developer','leo.martin@yahoo.com','Paris',4200),
-- ('Mia','Garcia','Tester','mia.garcia@gmail.com','London',3100),
-- ('Noah','Clark','Support','noah.clark@gmail.com','Berlin',2900),
-- ('Olivia','Lewis','Analyst','olivia.lewis@outlook.com','Tashkent',4100),
-- ('Paul','Walker','Developer','paul.walker@gmail.com','New York',4600),
-- ('Quinn','Hall','Designer','quinn.hall@yahoo.com','Rome',3600),
-- ('Ryan','Allen','Manager','ryan.allen@gmail.com','Madrid',6200),
-- ('Sophie','Young','Support','sophie.young@gmail.com','Paris',2800),
-- ('Tom','King','Developer','tom.king@outlook.com','Tashkent',4300),
-- ('Uma','Scott','Designer','uma.scott@gmail.com','Seoul',3700),
-- ('Victor','Adams','Manager','victor.adams@gmail.com','London',6100),
-- ('Wendy','Baker','Developer','wendy.baker@yahoo.com','Berlin',4400),
-- ('Xavier','Nelson','Support','xavier.nelson@gmail.com','Madrid',2950),
-- ('Yara','Carter','Analyst','yara.carter@gmail.com','New York',4000),
-- ('Zane','Mitchell','Developer','zane.mitchell@outlook.com','Tashkent',4550),
-- ('Amelia','Perez','Designer','amelia.perez@gmail.com','Paris',3500),
-- ('Ben','Roberts','Manager','ben.roberts@gmail.com','Berlin',6000),
-- ('Chloe','Turner','Support','chloe.turner@yahoo.com','Rome',3100),
-- ('Daniel','Phillips','Developer','daniel.phillips@gmail.com','Tashkent',4200),
-- ('Ella','Campbell','Designer','ella.campbell@outlook.com','London',3600),
-- ('Felix','Parker','Manager','felix.parker@gmail.com','Madrid',5900),
-- ('Georgia','Evans','Support','georgia.evans@gmail.com','Berlin',3050),
-- ('Harry','Edwards','Developer','harry.edwards@yahoo.com','Paris',4700),
-- ('Isla','Collins','Analyst','isla.collins@gmail.com','Rome',3850),
-- ('Jacob','Stewart','Manager','jacob.stewart@outlook.com','New York',6400),
-- ('Katie','Sanchez','Support','katie.sanchez@gmail.com','Seoul',2900),
-- ('Liam','Morris','Developer','liam.morris@gmail.com','Tashkent',4600),
-- ('Megan','Rogers','Designer','megan.rogers@yahoo.com','Paris',3700),
-- ('Nathan','Reed','Manager','nathan.reed@gmail.com','Berlin',6050),
-- ('Olga','Cook','Support','olga.cook@gmail.com','Rome',3000),
-- ('Peter','Morgan','Developer','peter.morgan@gmail.com','Madrid',4300),
-- ('Quincy','Bell','Analyst','quincy.bell@outlook.com','London',3900),
-- ('Ruby','Murphy','Designer','ruby.murphy@gmail.com','Paris',3600),
-- ('Samuel','Bailey','Manager','samuel.bailey@gmail.com','Tashkent',6250),
-- ('Tina','Rivera','Support','tina.rivera@yahoo.com','Berlin',3100),
-- ('Umar','Cooper','Developer','umar.cooper@gmail.com','Rome',4400),
-- ('Vera','Richardson','Designer','vera.richardson@gmail.com','New York',3700),
-- ('William','Cox','Manager','william.cox@gmail.com','Paris',6300),
-- ('Xenia','Howard','Support','xenia.howard@gmail.com','London',2850),
-- ('Yusuf','Ward','Developer','yusuf.ward@gmail.com','Tashkent',4500),
-- ('Zara','Torres','Analyst','zara.torres@outlook.com','Berlin',4100),
-- ('Adam','Peterson','Developer','adam.peterson@gmail.com','Rome',4350),
-- ('Bella','Gray','Designer','bella.gray@gmail.com','Madrid',3550),
-- ('Caleb','Ramirez','Manager','caleb.ramirez@yahoo.com','Paris',6000),
-- ('Daisy','James','Support','daisy.james@gmail.com','Seoul',3100),
-- ('Ethan','Watson','Developer','ethan.watson@gmail.com','London',4600),
-- ('Faith','Brooks','Analyst','faith.brooks@outlook.com','Tashkent',3950),
-- ('George','Kelly','Manager','george.kelly@gmail.com','New York',6400),
-- ('Hannah','Sanders','Support','hannah.sanders@gmail.com','Paris',3200),
-- ('Ian','Price','Developer','ian.price@outlook.com','Berlin',4500),
-- ('Julia','Bennett','Designer','julia.bennett@gmail.com','Madrid',3650),
-- ('Kyle','Wood','Manager','kyle.wood@gmail.com','Rome',6150),
-- ('Laura','Barnes','Support','laura.barnes@gmail.com','Tashkent',3050),
-- ('Mason','Ross','Developer','mason.ross@gmail.com','Paris',4700),
-- ('Nina','Henderson','Analyst','nina.henderson@outlook.com','London',4000),
-- ('Owen','Coleman','Manager','owen.coleman@gmail.com','Berlin',6200),
-- ('Paula','Jenkins','Support','paula.jenkins@gmail.com','Madrid',2900),
-- ('Rey','Perry','Developer','rey.perry@gmail.com','Tashkent',4600),
-- ('Sara','Powell','Designer','sara.powell@outlook.com','Paris',3800),
-- ('Theo','Long','Manager','theo.long@gmail.com','Rome',6400),
-- ('Ula','Patterson','Support','ula.patterson@yahoo.com','London',3150),
-- ('Viktor','Hughes','Developer','viktor.hughes@gmail.com','Berlin',4500),
-- ('Willa','Flores','Designer','willa.flores@gmail.com','Madrid',3750),
-- ('Xander','Washington','Manager','xander.washington@gmail.com','New York',6500),
-- ('Yasmin','Butler','Support','yasmin.butler@gmail.com','Paris',3000),
-- ('Zion','Simmons','Developer','zion.simmons@outlook.com','Tashkent',4550),
-- ('Ariana','Foster','Designer','ariana.foster@gmail.com','London',3700),
-- ('Blake','Gonzalez','Manager','blake.gonzalez@gmail.com','Berlin',6000),
-- ('Cora','Bryant','Support','cora.bryant@gmail.com','Rome',3100),
-- ('Dylan','Alexander','Developer','dylan.alexander@gmail.com','Madrid',4400),
-- ('Ella','Russell','Analyst','ella.russell@outlook.com','Paris',3950),
-- ('Finn','Griffin','Manager','finn.griffin@gmail.com','Tashkent',6300),
-- ('Gina','Diaz','Support','gina.diaz@gmail.com','London',2900),
-- ('Henry','Hayes','Developer','henry.hayes@gmail.com','Berlin',4650),
-- ('Isabel','Myers','Designer','isabel.myers@outlook.com','Paris',3650),
-- ('Jason','Ford','Manager','jason.ford@gmail.com','Madrid',6200),
-- ('Kylie','Hamilton','Support','kylie.hamilton@gmail.com','Rome',3100),
-- ('Logan','Graham','Developer','logan.graham@gmail.com','New York',4700),
-- ('Mila','Sullivan','Designer','mila.sullivan@gmail.com','Tashkent',3600),
-- ('Noel','Wallace','Manager','noel.wallace@gmail.com','Paris',6100),
-- ('Oli','Cole','Support','oli.cole@yahoo.com','London',2950),
-- ('Pia','West','Developer','pia.west@gmail.com','Berlin',4300),
-- ('Quinn','Stone','Analyst','quinn.stone@outlook.com','Rome',4100),
-- ('Riley','Curtis','Manager','riley.curtis@gmail.com','Madrid',6000),
-- ('Sasha','Payne','Support','sasha.payne@gmail.com','Tashkent',3000),
-- ('Toby','Jordan','Developer','toby.jordan@gmail.com','Paris',4550),
-- ('Una','Mendoza','Designer','una.mendoza@gmail.com','London',3550),
-- ('Victor','Reyes','Manager','victor.reyes@gmail.com','Berlin',6400),
-- ('Wendy','Ortiz','Support','wendy.ortiz@gmail.com','Rome',3200),
-- ('Ximena','Harper','Developer','ximena.harper@gmail.com','Tashkent',4500),
-- ('Yuri','Craig','Analyst','yuri.craig@outlook.com','Paris',4050),
-- ('Zoe','Ramsey','Manager','zoe.ramsey@gmail.com','New York',6300);


SELECT name, position, salary FROM employees;

SELECT COUNT(DISTINCT position) AS COUNT_POSITION FROM employees;

SELECT * FROM employees
WHERE salary > 4000;

SELECT * FROM employees
ORDER BY salary DESC;

SELECT * FROM employees
WHERE (position = 'Developer' OR salary > 4500); --bonus yoq table da

-- 5 6 7 8 togri kelmaydi table ga

DELETE FROM employees
WHERE position = 'Intern';
SELECT * FROM employees;


SELECT TOP 3 * FROM employees
ORDER BY salary DESC;

SELECT AVG(salary) AS AvgSalary FROM employees;  

SELECT MAX(salary), MIN(salary) FROM employees;

SELECT COUNT(name) FROM employees;

--14 table togri kelmaydi

SELECT AVG(salary) AS AvgSalary, position FROM employees
GROUP BY position;

SELECT * FROM employees
WHERE name LIKE 'A%';

SELECT * FROM employees
WHERE surname LIKE '%n';

SELECT * FROM employees
WHERE position IN ('Developer','Manager','Designer');

SELECT * FROM employees
WHERE salary BETWEEN 3000 AND 4500;

SELECT salary AS [Monthly Salary] FROM employees;