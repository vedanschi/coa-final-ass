# 🐳 Flask-MySQL Dockerized Application

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

A containerized Flask application that connects to a MySQL database using Docker bridge networking.

## 🌟 Features
- **Dockerized Flask** web application
- **MySQL container** with persistent storage
- **Bridge networking** between containers
- **Dynamic HTML template** displaying user data
- **Production-ready** configuration


🌐 Access the Application
Visit http://localhost:5000 in your browser to see the user data table.
![lab008](https://github.com/user-attachments/assets/088219f5-ea17-4fe0-b619-f609b2f7c72b)

<!-- SCREENSHOT_PLACEHOLDER: browser_output.png -->🌐 Access the Application
Visit http://localhost:5000 in your browser to see the user data table.

<!-- SCREENSHOT_PLACEHOLDER: browser_output.png -->
🧩 Database Initialization
To populate your MySQL database with sample data:

bash
docker exec -i mysql-container mysql -uroot -proot mydb <<EOF
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
INSERT INTO users (name, age) VALUES 
    ('Alice', 28),
    ('Bob', 32),
    ('Charlie', 24);
![lab004](https://github.com/user-attachments/assets/3aa14649-4508-4456-809f-5cfa29412ae0)


