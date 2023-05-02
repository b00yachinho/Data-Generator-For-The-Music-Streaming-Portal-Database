import sys, os
from con_to_db import Database
import oracledb

# change to correct db credentials
db = Database(username='username',
              password='password',
              host='host',
              port=0000,  # change to correct port
              service_name='service_name')
conn = db.connect()
cur = conn.cursor()

def createTables():
    with open('tables.sql') as f:
        sql = f.read()
        queries = sql.split(';')
        queries.pop()

        for query in queries:
            cur.execute(query)
            print("\nExecuting query:", query)
        print("\nCheck SQL Developer for created tables.")

def dropTables():
    with open('drop_tables.sql', 'r') as f:
        sql = f.read()
        print("Executing query:\n")
        print(sql + '\n')
        cur.execute(sql)
        print('Dropped existing tables.')

def deleteFiles():
    choiceWithFiles = input("Are you sure? (y/n) -> ")

    if choiceWithFiles == 'y':
        for filename in os.listdir("."):
            if filename.endswith("_data.txt"):
                print("Deleting file " + filename)
                os.remove(filename)

    elif choiceWithFiles == 'n':
        print("Closing...")
        sys.exit(1)

    else:
        print('Wrong input, closing program...')
        sys.exit(1)


print("What to do:")
print("1. Drop Tables | 2. Create Tables | 3. Drop, then Create Tables | 4. Delete every '_data.txt' file")

choice = int(input("-> "))

if choice == 1:
    dropTables()

elif choice == 2:
    createTables()

elif choice == 3:
    dropTables()
    createTables()

elif choice == 4:
    deleteFiles()

else:
    print("Wrong input, closing program...")
    sys.exit(1)

cur.close()
conn.close()
