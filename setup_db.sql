-- Create your tables and insert initial data here.

create table movies(
tmdb_id int primary key,
title text,
rating decimal(10,2)
);

create table people(
tmdb_id int primary key,
name text
);

create table movies_people(
movie_id int,
people_id int,
role_id int
);

create table `roles`(
role_id int auto_increment primary key,
`role` text
);

insert into `roles`(role) values("Actor"), ("Director")
