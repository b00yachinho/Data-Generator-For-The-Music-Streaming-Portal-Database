# EN - Sample Data Generator For Music Streaming Portal Database

This program generates sample data to a database for a fictional music streaming service using Python and Oracle Database.
 
### Installation

1. Clone the repository to your local machine.
2. Install the library used in this project - `oracledb`.
3. Create a new Oracle database and update the credentials in the `reset.py` and `ex2db.py` files in a designated place.
4. Run `reset.py` in your terminal and select the second option to create the necessary tables in the database.
5. Run `ex2db.py` in your terminal and follow the prompts in the terminal to generate the data for the database.

### Usage
The program generates sample data, including users, producers, music tracks, albums, playlists, concerts, ratings and servers, to tables on a Oracle Database. The number of queries to generate can be specified and whether to execute them to all tables or to a specific table.
This program also generates `.txt` files containing all generated SQL queries, separate for each table.

To delete, or add tables to the database, or delete all generated `.txt` files, execute the `reset.py` script and select the desired option.

To run the program, execute the `ex2db.py` script and follow the prompts in your terminal.

### What every file does
- `tables.sql` - a file containing the neccesary SQL code to create the tables,
- `drop_tables.sql` - a file containing a SQL script that drops all tables from a database,
- `con_to_db.py` - a module responsible for connecting to a Oracle database,
- `reset.py` - a tool that drops and creates tables and deletes all generated `.txt` files,
- `gen_data.py` - a module that generates data,
- `ex2db.py` - main program that executes everything to the database.
---
# PL - Generator Przykładowych Danych Dla Bazy Danych Portalu Streamingu Muzyki

Ten program generuje przykładowe dane do bazy danych dla fikcyjnego serwisu streamingu muzyki przy użyciu Pythona i bazy danych Oracle.

### Instalacja

1. Sklonuj repozytorium na swoją lokalną maszynę.
2. Zainstaluj bibliotekę wykorzystywaną w tym projekcie - `oracledb`.
3. Utwórz nową bazę danych Oracle i zaktualizuj dane uwierzytelniające w plikach `reset.py` i `ex2db.py` w odpowiednim miejscu.
4. Uruchom `reset.py` w swoim terminalu i wybierz drugą opcję, żeby stworzyć odpowiednie tabele w bazie danych.
5. Uruchom `ex2db.py` w swoim terminalu i postępuj zgodnie z monitami w terminalu, aby wygenerować dane dla bazy danych.

### Użycie
Program generuje przykładowe dane, w tym użytkowników, producentów, utwory muzyczne, albumy, playlisty, koncerty, oceny i serwery, do tabel w bazie danych Oracle. Można określić liczbę rekordów do wygenerowania i czy wykonać je do wszystkich tabel lub określonej tabeli.
Program ten generuje również pliki `.txt` zawierające wszystkie wygenerowane zapytania SQL, oddzielnie do każdej tabeli.

Żeby usunąć, bądź dodać tabele do bazy danych, lub usunąć wszystkie wygenerowane pliki `.txt`, należy wykonać skrypt `reset.py` i wybrać odpowiednią opcję.

Aby uruchomić program, należy wykonać skrypt `ex2db.py` i postępować zgodnie z monitami w terminalu.

### Co robi każdy plik
- `tables.sql` - plik zawierający kod SQL, niezbędny do tworzenia tabel,
- `drop_tables.sql` - plik zawierający skrypt SQL, który usuwa wszystkie tabele z bazy danych,
- `con_to_db.py` - moduł odpowiedzialny za połączenie z bazą danych Oracle,
- `reset.py` - narzędzie, które usuwa i tworzy tabele oraz usuwa wszystkie wygenerowane pliki `.txt`,
- `gen_data.py` - moduł generujący dane,
- `ex2db.py` - główny program wykonujący wszystko do bazy danych.
---
