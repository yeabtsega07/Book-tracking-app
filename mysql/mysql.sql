use book;

-- Create the 'books' table if not exists
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    status VARCHAR(255)
);

-- Insert records into the 'books' table if it's empty
INSERT IGNORE INTO books (title, status) VALUES ('Intro to DSA', 'to-read');
INSERT IGNORE INTO books (title, status) VALUES ('Distributed Systems', 'to-read');
INSERT IGNORE INTO books (title, status) VALUES ('System Design', 'in-progress');
INSERT IGNORE INTO books (title, status) VALUES ('Test and Implementation', 'in-progress');
INSERT IGNORE INTO books (title, status) VALUES ('Deployment', 'completed');
INSERT IGNORE INTO books (title, status) VALUES ('Nationalism', 'completed');