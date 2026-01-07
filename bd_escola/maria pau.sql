CREATE DATABASE escola;

USE escola;

CREATE TABLE aluno(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE,
    ra INT
);

INSERT INTO aluno(nome, cpf, email) VALUES (
	"João Gay da Silva",
	"12345678901", 
	"souboiola426@hotmail.com");

UPDATE aluno
SET email = "souboiola24@hotmail.com"
WHERE id = 1;

INSERT INTO aluno(nome, cpf, email) VALUES (
	"Maria Pau",
    "98765432112",
    "soualfa157@gmail.com");
    
INSERT INTO aluno(nome, cpf, email) VALUES (
	"Jacinto Pinto",
    "69696969696",
    "mamei@gmail.com");
    
DELETE FROM aluno
WHERE id = 4;

SELECT * FROM aluno;
    

