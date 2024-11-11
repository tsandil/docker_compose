Crypto Price Data Pipeline with Redis and PostgreSQL
========

This project is a Docker-based ETL (Extract, Transform, Load) pipeline that fetches cryptocurrency price data, stores it temporarily in Redis, and then loads it into a PostgreSQL database. This project demonstrates how to use Docker Compose to manage a multi-container setup involving a Redis data cache, a PostgreSQL database, and two Python-based microservices for fetching and loading data.

Overview
================
This project uses the Coindesk API to retrieve the current price of Bitcoin in USD. The data_fetcher service fetches the price data, stores it in Redis, and the data_loader service then reads the data from Redis and loads it into PostgreSQL.

Key Concepts
================
- **Docker and Docker Compose** : Simplifies the development and deployment by managing multiple services.
- **Redis** : Used as a fast in-memory data store for holding fetched data temporarily.
- **PostgreSQL** : Serves as the long-term storage for fetched data.
- **Python** : Handles data fetching, processing, and loading.


Services defined: 
===========================

1. **Redis** : An in-memory data store used as a cache to store fetched data temporarily.
2. **PostgreSQL** : A  relational database for storing data persistently.
3. **Data Fetcher** (```data_fetcher```) : A Python-based service that fetches cryptocurrency data and stores it in Redis.
4. **Data Loader** (```data_loader```) : A Python-based service that reads data from Redis and inserts it into the PostgreSQL database.

Set up and Installation
=================================
**Prerequisites**

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

**Instructions**
1. Clone the repository:

2. Build and start the containers:
- ```docker-compose up --build``` - This command will build and start all services defined in the ```docker-compose.yml``` file and sets up the Reis and PostgreSQL with persistent volumes.

3. Stop the containers:
- ```docker-compose down``` 
- ```docker-compose down --volumes --rmi all``` - to stop the container deleting all existing images and volumes.

Configuration
=======
- **Environment Variables** : Update the necessary environment variables in the ```docker-compose.yml``` file like PostgreSQL user and password.

- **Database Connection** : 
    - PostgreSQL user and password are set in ```docker-compose.yml```.
    - ```load_data.py``` connects to the PostgreSQL using the connection string in ```conn_string```

