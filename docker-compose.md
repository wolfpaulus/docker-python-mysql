# Docker Compose Configuration Explained

This document provides an explanation of the `docker-compose.yml` file used for running a Python application alongside a MySQL database in Docker containers. The setup ensures database persistence and enables communication between services via a custom network.

## **Overview**
This `docker-compose.yml` defines three services:

1. **db** - A MySQL database container.
2. **app** - A Python application that interacts with the database.
3. **test** - A Python application that runs the unit tests.

Additionally, it includes:

- A **custom network (`my_network`)** for container communication.
- A **named volume (`mysql_data`)** for persistent database storage.

## **docker-compose.yml Breakdown**

```yaml
services:
  db:
    image: mysql:8.0
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=rootpassword
      - MYSQL_DATABASE=demo_db
    networks:
      - mynetwork
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  app:
    build: .
    depends_on:
      - db
    environment:
      - MYSQL_HOST=db
      - MYSQL_USER=root
      - MYSQL_PASSWORD=rootpassword
      - MYSQL_DATABASE=demo_db
    networks:
      - mynetwork
    command: ["python", "src/app.py"]

  test:
    build: . 
    depends_on:
      - db
      - app
    environment:
      - MYSQL_HOST=db
      - MYSQL_USER=root
      - MYSQL_PASSWORD=rootpassword
      - MYSQL_DATABASE=demo_db
    entrypoint: ["pytest", "tests/test_app.py"] # Runs tests when started
    networks:
      - my_network # Connects tests to the network    

networks:
  mynetwork:
    driver: bridge

volumes:
  mysql_data:
```

## **Service Explanations**

### **1. Database Service (`db`)**
- **`image: mysql:8.0`** → Uses MySQL 8.0 as the database engine.
- **`restart: always`** → Ensures the database container restarts if it stops.
- **`environment`** → Defines environment variables for MySQL:
  - `MYSQL_ROOT_PASSWORD` → Root user password.
  - `MYSQL_DATABASE` → Creates a default database named `demo_db`.
- **`networks`** → Connects the database to the `my_network` network.
- **`ports`** → Maps MySQL’s internal **port 3306** to the host machine.
- **`volumes`** → Uses `mysql_data` to persist database files across container restarts.

### **2. Application Service (`app`)**
- **`build: .`** → Builds the application image from the `Dockerfile` in the same directory.
- **`depends_on: - db`** → Ensures the database starts before the app.
- **`environment`** → Passes database connection settings to the app:
  - `MYSQL_HOST: db` → The app connects to `db` (MySQL service name in Compose).
  - `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE` → Credentials to connect to MySQL.
- **`networks: - my_network`** → Ensures the app can communicate with the database.
- **`command: ["python", "src/app.py"]`** → Runs the app when the container starts.

### **3. Application Service (`test`)**
- **`build: .`** → Builds the application image from the `Dockerfile` in the same directory.
- **`depends_on: - db, app`** → Ensures the database and app starts before the test.
- **`environment`** → Passes database connection settings to the app.
- **`networks: - my_network`** → Ensures the test can communicate with the database.
- **`entrypoint: ["python", "tests/test_app.py"]`** → Runs the tests when the container starts.

## **Network & Volume Configuration**

### **🔹 Custom Network (`my_network`)**
```yaml
networks:
  my_network:
    driver: bridge
```
- Creates an **isolated network** where containers can communicate **by service name**.
- Ensures the `app` service can refer to MySQL as `db`.

### **🔹 Persistent Database Storage (`mysql_data`)**
```yaml
volumes:
  mysql_data:
```
- Stores MySQL data persistently in a Docker volume.
- Prevents data loss when containers restart.

## **How to Use**
### **Start the Services**
```sh
docker-compose up --build -d
```
- The `-d` flag runs containers in detached mode.
- MySQL and the Python app will start in the background.

### **Stop the Services**
```sh
docker-compose down
```
- Stops and removes all containers, but **data is preserved**.

### **Check Running Containers**
```sh
docker ps
```
- Lists active containers to verify everything is running.
