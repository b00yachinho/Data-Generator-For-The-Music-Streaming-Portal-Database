# EN - Sample Data Generator For Music Streaming Portal Database

This program generates sample data to a database for a music streaming service using Python and Oracle Database.
 
### Installation

1. Clone the repository to your local machine.
2. Install the library used in this project - `oracledb`.
3. Create a new Oracle database and update the credentials in the `reset.py` and `ex2db.py` files in the appropriate place.
4. Run `reset.py` in your terminal and select the second option to create the necessary tables in the database.
5. Run `ex2db.py` in your terminal and follow the prompts in the terminal to generate the data for the database.

### Usage
The program generates data , including users, producers, music tracks, albums, playlists, concerts, ratings and servers, to tables on a Oracle Database. The number of queries to generate can be specified and whether to execute them to all tables or to a specific table.
This program also generates `.txt` files containing all generated SQL queries, separate for each table.

To delete, or add tables to the database, or delete all generated `.txt` files, execute the `reset.py` script and select desired option.

To run the program, execute the `ex2db.py` script and follow the prompts in your terminal.

# PL - Generator Przykładowych Danych Dla Bazy Danych Portalu Streamingu Muzyki

Ten program generuje przykładowe dane do bazy danych dla serwisu streamingu muzyki przy użyciu Pythona i bazy danych Oracle.

### Instalacja

1. Sklonuj repozytorium na swoją lokalną maszynę.
2. Zainstaluj bibliotekę wykorzystywaną w tym projekcie - `oracledb`.
3. Utwórz nową bazę danych Oracle i zaktualizuj dane uwierzytelniające w plikach `reset.py` i `ex2db.py` w odpowiednim miejscu.
4. Uruchom `reset.py` w swoim terminalu i wybierz drugą opcję, żeby stworzyć odpowiednie tabele w bazie danych.
5. Uruchom `ex2db.py` w swoim terminalu i postępuj zgodnie z monitami w terminalu, aby wygenerować dane dla bazy danych.

### Użycie
Program generuje przykąldowe dane, w tym użytkowników, producentów, utwory muzyczne, albumy, playlisty, koncerty, oceny i serwery, do tabel w bazie danych Oracle. Można określić liczbę rekordów do wygenerowania i czy wykonać je do wszystkich tabel lub określonej tabeli.
Program ten generuje również pliki `.txt` zawierające wszystkie wygenerowane zapytania SQL, oddzielnie do każdej tabeli.

Żeby usunąć, bądź dodać tabele do bazy danych, lub usunąć wszystkie wygenerowane pliki `.txt`, należy wykonać skrypt `reset.py` i wybrać odpowiednią opcję.

Aby uruchomić program, należy wykonać skrypt `ex2db.py` i postępować zgodnie z monitami w terminalu.
