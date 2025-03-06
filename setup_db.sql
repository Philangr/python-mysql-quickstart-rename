-- Create your tables and insert initial data here.

create table movies(
title text,
release_year int,
genre text
);

alter table movies add column imdb_id varchar(10);

alter table movies add primary key (imdb_id); 
