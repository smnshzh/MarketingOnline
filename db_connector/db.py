import pymysql


def my_sql_connection(host, user, password, database, port=3306):
    
    try:
        connection = pymysql.connect(
            host=host,       # MySQL database host address (e.g., "127.0.0.1" or "localhost")
            user=user,       # MySQL username
            password=password,  # MySQL password
            database=database,  # Name of the database
            port=port         # MySQL port (e.g., 3308)
        )
        
        return connection
    except pymysql.Error as e:
        print(f"Error: {e}")
        return None

def connect_to_db():
    dpm = {
    "user": "sql12649695",
    "password": "LjgnWc9Y41",
    "host": "sql12.freemysqlhosting.net",
    "database": "sql12649695",
}

    port = 3306  # Update the port to match your MySQL server configuration

    # Establish a database connection
    cnx = my_sql_connection(host=dpm["host"], 
                            user=dpm['user'], 
                            password=dpm['password'], 
                            database=dpm['database'], 
                            port=port)
    return cnx