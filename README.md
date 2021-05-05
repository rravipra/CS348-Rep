# Steps

1. Activate **MySQL** server:

    ```bash
    $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
    $ mysql.exe -u <username> -p<password>
    $ mysql -u <username> -p
    ```

    On my case:

    ```bash
    $ mysql.exe -u lintang -p12345
    $ mysql -u lintang -p
    ```

#

2. Create a database & table on MySQL. I'll use a database called **"lin_flask"** & a table called **"users"**:

    ```bash
    mysql>  CREATE DATABASE lin_flask;
    mysql>  USE lin_flask;
    mysql>  CREATE TABLE users (
                id int auto_increment,
                name varchar(100) not null,
                age tinyint,
                primary key (id)
            );
    ```

#

3. Clone this repo. Edit **database.yaml** file according to your database configuration, then install all the packages needed. In this project I'm using **flask**, **flask_cors** & **flask_mysqldb**:

    ```bash
    $ git clone https://github.com/LintangWisesa/CRUD_Flask_MySQL.git
    $ cd CRUD_Flask_MySQL
    ```

    Install dependencies:

    ```bash
    $ pip install flask flask_cors flask_mysqldb
    $ py -m pip install flask flask_cors flask_mysqldb
    ```

#

4. Run the server file. Make sure your MySQL server is still running. Your application server will run locally at **_http://localhost:5000/_** :
    ```bash
    $ py app.py
    $ python app.py
    $ python3 app.py
    ```

#

5. Give a request to the server. You can use **Postman** app:

    **See the opening screen (_home.html_)**

    ```bash
    GET /
    ```

    **Post a data to database:**

    ```bash
    POST /data
    body request: {name:"x", age:"y"}
    ```

    **Get all data & specific data by id:**

    ```bash
    GET /data
    GET /data/{:id}
    ```

    **Update a data by id**:

    ```bash
    PUT /data/{:id}
    body request: {name:"x", age:"y"}
    ```

    **Delete a data by id:**

    ```bash
    DELETE /data/{:id}
    ```

#
