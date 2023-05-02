import oracledb

class Database:
    def __init__(self, username, password, host, port, service_name):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.service_name = service_name

    def connect(self):
        try:
            dsn = oracledb.makedsn(self.host, self.port, service_name=self.service_name)
            conn = oracledb.connect(user=self.username, password=self.password, dsn=dsn)
            print("Successfully connected to database")
            return conn
        except oracledb.Error as e:
            print("Error while connecting to database:", e)
            return None
