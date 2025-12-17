-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- A - SELECT
-- U - UPDATE
-- D - DELETE

-- INSERT
insert into alumno (nro_documento, nombre) values
('100', 'Ernesto Castro')

-- INSERTAR VARIOS REGISTROS
insert into alumno (nro_documento, nombre) values
('200', 'Ana Perez'),
('300', 'Luis Gomez'),
('400', 'Maria Rodriguez'),
('500', 'Carlos Sanchez'),
('600', 'Sofia Fernandez'),
('700', 'Jorge Ramirez'),
('800', 'Lucia Torres'),
('900', 'Diego Flores'),
('1000', 'Elena Morales');

-- ACTUALIZAR REGISTROS
update alumno SET
email = "codigo@gmail.com";

-- UPDATE CON WHERE
update alumno SET
email = "ernesto@gmail.com" WHERE id = 1;

-- UDPATE CON FUNCIONES
update alumno SET
email = CONCAT(LOWER(REPLACE(nombre, " ", ".")), "@gmail.com") WHERE id >= 1;

-- SELECT
select * from alumno;

select nombre, email from alumno;

select nombre from alumno WHERE id > 5;

select * from alumno order by nombre asc;

-- DELETE
delete FROM alumno WHERE id = 9;