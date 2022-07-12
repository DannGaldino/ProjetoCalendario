create database cronogramaDeAulas;

use cronogramaDeAulas;

create table Professor(
email varchar(120) not null primary key,
senha varchar(30) not null,
nome varchar(105) not null
)Engine = InnoDB;

select * from Professor where email = 'daniel@gmail.com';
select * from Professor;

drop table Professor;

create table calendario(
codigo varchar(20) not null primary key,
dia int(2) not null,
mes int(2) not null,
ano int(4) not null,
turno varchar(10) not null,
materia varchar(50) not null,
professor varchar(120) not null
)Engine = InnoDB;

select * from calendario;

delete from calendario where codigo = '2022-05-03noite';

drop table calendario;

create table Administrador(
usuario varchar(120) not null primary key,
senha varchar(30) not null
)Engine = InnoDB;

insert into Administrador(usuario, senha) values('admin','admin963');

select * from Administrador;

create table Aluno(
email varchar(120) not null primary key,
senha varchar(30) not null
)Engine = InnoDB;

insert into Aluno(email, senha) values('aluno@gmail.com','aluno123');

select * from Aluno;