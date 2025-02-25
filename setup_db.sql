-- Create your tables and insert initial data here.

CREATE DATABASE things;

CREATE TABLE IF NOT EXISTS thing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO thing (name) VALUES ('OMG'), ('this is like totally data inside of a database!'), ('if you are reading this, it worked baby! you''re a full on software engineer now!');
