import sys, os
import oracledb
from gen_data import genUsers, genProd, genTrack, genAlbums, genPlaylist, genConcert, genRating, servers, relations
from con_to_db import Database

# change to correct db credentials
db = Database(
    username='username',
    password='password',
    host='host',
    port=0000,  # change to correct port
    service_name='service_name'
)

conn = db.connect()
cur = conn.cursor()

num_records = int(input("How many records to generate: "))
num_prod = num_track = num_users = num_album = num_conc = num_rat = num_servers = num_records


def generate_users_data(num_records, cur):
    object = genUsers()
    data = object.generate_user_data(num_records)

    with open('user_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    return data

def generate_producers_data(num_records, cur):
    object = genProd()
    data = object.generate_producer_data(num_records)

    with open('prod_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        
        conn.commit()

    return data

def generate_tracks_data(num_records, cur):
    object = genTrack()
    num_prod = num_records
    data = object.generate_music_data(num_records, num_prod)

    with open('track_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    return data

def generate_albums_data(num_records, cur):
    object = genAlbums()
    num_prod = num_records
    data = object.generate_album_data(num_records, num_prod)

    with open('album_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    return data

def generate_playlists_data(num_records, cur):
    object = genPlaylist()
    num_track = num_users = num_records
    data = object.generate_playlist_data(num_records, num_track, num_users)

    with open('play_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    return data

def generate_concerts_data(num_records, cur):
    object = genConcert()
    num_prod = num_records
    data = object.generate_concert_info(num_records, num_prod)

    with open('conc_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    return data

def generate_ratings_data(num_records, cur):
    object = genRating()
    num_users = num_album = num_track = num_records
    data = object.generate_rating_data(num_records, num_users, num_album, num_track)

    with open('rat_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    return data

def generate_servers_data(num_records, cur):
    object = servers()
    num_servers = num_records
    data = object.generate_server_data(num_servers)

    with open('server_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    return data

def generate_relations_data(num_records, cur):
    object = relations()

    relation_12_set = set()
    relation_13_set = set()
    relation_16_set = set()
    relation_17_set = set()
    rel12_data = []
    rel13_data = []
    rel16_data = []
    rel17_data = []

    while len(relation_12_set) < num_records:
        new_rel = object.generate_relation_12_data(num_records, num_servers, num_conc)
        if new_rel[0] not in relation_12_set:
            relation_12_set.add(new_rel[0])
            rel12_data.append(new_rel)
        else:
            print("Duplicated key in relation 1-2. Skipping...")

    while len(relation_13_set) < num_records:
        new_rel = object.generate_relation_13_data(num_records, num_servers, num_album)
        if new_rel[0] not in relation_13_set:
            relation_13_set.add(new_rel[0])
            rel13_data.append(new_rel)
        else:
            print("Duplicated key in relation 1-3. Skipping...")

    while len(relation_16_set) < num_records:
        new_rel = object.generate_relation_16_data(num_records, num_track, num_servers)
        if new_rel[0] not in relation_16_set:
            relation_16_set.add(new_rel[0])
            rel16_data.append(new_rel)
        else:
            print("Duplicated key in relation 1-6. Skipping...")

    while len(relation_17_set) < num_records:
        new_rel = object.generate_relation_17_data(num_records, num_rat, num_servers)
        if new_rel[0] not in relation_17_set:
            relation_17_set.add(new_rel[0])
            rel17_data.append(new_rel)
        else:
            print("Duplicated key in relation 1-7. Skipping...")

    with open('rel12_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    with open('rel13_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    with open('rel16_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()

    with open('rel17_data.txt') as file:
        for line in file:
            cur.execute(line)
            print(f"Executing SQL query: {line.strip()}")
        conn.commit()


def all():
    generate_users_data(num_records, cur)
    generate_producers_data(num_records, cur)
    generate_tracks_data(num_records, cur)
    generate_albums_data(num_records, cur)
    generate_playlists_data(num_records, cur)
    generate_concerts_data(num_records, cur)
    generate_ratings_data(num_records, cur)
    generate_servers_data(num_records, cur)
    generate_relations_data(num_records, cur)

def exit_program():
    print("Exiting program...")
    sys.exit(1)

def default():
    print("Wrong option.")

switcher = {
    0: all,
    1: generate_users_data,
    2: generate_producers_data,
    3: generate_tracks_data,
    4: generate_albums_data,
    5: generate_playlists_data,
    6: generate_concerts_data,
    7: generate_ratings_data,
    8: generate_servers_data,
    9: generate_relations_data,
}

print("Options to select:")
print("0. all tables | 1. users | 2. producers | 3. music_tracks | 4. albums | 5. playlists | 6. concert_info | "
      "7. ratings | 8. servers | 9. relations (12, 13, 16 & 17)")

selected_option = None
while selected_option not in switcher:
    try:
        selected_option = int(input("Select a table to generate data to: "))
        if selected_option not in switcher:
            print("Wrong input.")
    except ValueError:
        print("Wrong input. Insert a correct value.")

if selected_option == 0:
    switcher.get(selected_option, default)()
else:
    switcher.get(selected_option, default)(num_records, cur)


cur.close()
conn.close()
