# Dockerized Python + MySQL Project

## 📌 Project Overview
This project demonstrates how to use **Docker and Docker Compose** to run a **Python application** that interacts with a **MySQL database**. It includes:

- A Python application that stores **lists of random integers** in a MySQL database.
- A MySQL service with **persistent storage**.
- **Automated testing** using `pytest`.
- **Custom networking** for inter-container communication.

## 📂 Folder Structure
```
.
├── src/                 # Python application code
│   ├── app.py           # Main application script
│   ├── dbutils.py       # Database utility functions
├── tests/               # Test scripts
│   ├── test_app.py      # Pytest verification
│   ├── requirements.txt # Dependencies for tests
├── dockerfile           # Builds the app container
├── mysql-only.yml       # Running just the MySQL container
├── docker-compose.md    # Detailed documentation of the compose file
├── docker-compose.yml   # Orchestrates multi-container setup
├── .dockerignore        # Excludes files from Docker builds
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation (this file)
```

## 🚀 Getting Started
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/wolfpaulus/docker-python-mysql.git
cd docker-python-mysql
```

### **2️⃣ Build and Run the Containers**
```sh
docker-compose up -d
```
- Runs the **MySQL database** and **Python application** in separate containers.
- The database **persists data** using a Docker volume.

### **3️⃣ Verify Running Containers**
```sh
docker ps
```

## 🛠️ Configuration
Modify environment variables in `docker-compose.yml` as needed:
```yaml
environment:
  MYSQL_HOST: db
  MYSQL_USER: root
  MYSQL_PASSWORD: rootpassword
  MYSQL_DATABASE: demo_db
```

## 🔗 Connecting to MySQL

```sh
docker exec -it <cointainer-id> mysql -uroot -prootpassword
```
- Connects to MySQL running in Docker.
- Enter `rootpassword` when prompted.

## 🛑 Stopping and Cleaning Up
```sh
docker-compose down
```
- Stops and removes all containers **but keeps the database data**.
- To delete all data, run:
  ```sh
  docker-compose down -v
  ```


