SELECT *
FROM dojos;

SELECT *
FROM ninjas;

SELECT * FROM dojos WHERE id = 1;
SELECT * FROM ninjas WHERE id =18;
SELECT n.id, first_name,last_name,age, d.id 
FROM dojos d 
LEFT JOIN ninjas n 
ON d.id = n.dojo_id
WHERE d.id = 2;

SELECT * 
FROM dojos 
LEFT JOIN ninjas 
ON dojos.id = ninjas.dojo_id; 

SELECT n.first_name,n.last_name,n.age 
FROM dojos d 
LEFT JOIN ninjas n 
ON d.id =n.dojo_id 
WHERE d.id =1;

SELECT * FROM dojos WHERE id = 1;