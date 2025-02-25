-- Create your tables and insert initial data here.

CREATE TABLE IF NOT EXISTS thing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO thing (name) VALUES ('thing1'), ('thing2');
