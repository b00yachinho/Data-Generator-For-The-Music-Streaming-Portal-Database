import random
from datetime import datetime, timedelta

class genUsers:
    def generate_user_data(self, num_users):
        regions = {
            "Europe": "EUR",
            "Asia": "ASIA",
            "North America": "NOAM",
            "South America": "SOAM",
            "Africa": "AFR",
            "Oceania": "OCN"
        }
        countries = {
            "USA": "North America",
            "Canada": "North America",
            "UK": "Europe",
            "Australia": "Oceania",
            "India": "Asia",
            "China": "Asia",
            "Nigeria": "Africa",
            "Brazil": "South America",
            "Germany": "Europe",
            "Japan": "Asia"
        }
        user_data = []
        for i in range(num_users):
            nickname = f"user{i+1}"
            age = random.randint(18, 65) if random.randint(0, 1) else None
            sex = random.choice(["male", "female", None])
            country = random.choice(list(countries.keys()))
            region = regions[countries[country]]
            if random.randint(0, 1):
                sub_start = None
                sub_end = None
            else:
                sub_start = datetime.strptime("2014-01-01", "%Y-%m-%d") + timedelta(
                    days=random.randint(0, (datetime.today() - datetime.strptime("2014-01-01", "%Y-%m-%d")).days))
                sub_end = sub_start + timedelta(days=random.randint(1, (datetime.today() - sub_start).days))
            if age is None:
                age_str = "NULL"
            else:
                age_str = str(age)
            if sex is None:
                sex_str = "NULL"
            else:
                sex_str = sex
            if sub_start is None:
                sub_start_str = "NULL"
                sub_end_str = "NULL"
            else:
                sub_start_str = "TO_DATE('" + sub_start.strftime("%Y-%m-%d") + "', 'YYYY-MM-DD')"
                sub_end_str = "TO_DATE('" + sub_end.strftime("%Y-%m-%d") + "', 'YYYY-MM-DD')"
            sql = "INSERT into \"user\" (nickname, age, sex, country, region, sub_start, sub_end) " \
                  f"VALUES ('{nickname}', {age_str}, '{sex_str}', '{country}', '{region}', {sub_start_str}, {sub_end_str})"
            user_data.append(sql)

        with open('user_data.txt', 'w') as f:
            for sql in user_data:
                f.write(sql + '\n')
        return user_data

class genProd:
    def generate_producer_data(self, num_prod):
        producers = []
        for i in range(num_prod):
            prod_tag = f"Producer {i+1}"
            desc = random.choice([None, "'Short description'"])
            partner = random.choice(["Y", "N"])
            members = []
            for j in range(random.randint(1, 5)):
                member_name = f"Member {j+1}"
                members.append(member_name)
            members_str = ", ".join(members)
            desc_str = "NULL" if desc is None else f"'{desc}'"
            sql = f"INSERT into producer (prod_tag, \"desc\", partner, \"member/s\") " \
                  f"VALUES ('{prod_tag}', '{desc_str}', '{partner}', '{members_str}')"
            producers.append(sql)

        with open('prod_data.txt', 'w') as f:
            for sql in producers:
                f.write(sql + '\n')
        return producers

class genTrack:
    def generate_music_data(self, num_tracks, num_prod):
        genres = ["Rock", "Pop", "House", "Metal", "Hip-Hop", "Jazz"]
        track_data = []
        for i in range(num_tracks):
            name = f"Track {i+1}"
            genre = random.choice(genres)
            prod_id = random.randint(1, num_prod)
            sql = f"INSERT INTO music_tracks (name, genre, producer_prod_id)" \
                  f" VALUES ('{name}', '{genre}', {prod_id})"
            track_data.append(sql)

        with open('track_data.txt', 'w') as f:
            for sql in track_data:
                f.write(sql + '\n')
        return track_data

class genAlbums:
    def generate_album_data(self, num_album, num_prod):
        album_data = []
        for i in range(num_album):
            name = f"Cool album {i+1}"
            prod_id = random.randint(1, num_prod)
            sql = f"INSERT INTO albums (name, producer_prod_id) " \
                  f"VALUES ('{name}', {prod_id})"
            album_data.append(sql)

        with open('album_data.txt', 'w') as f:
            for sql in album_data:
                f.write(sql + '\n')
        return album_data

class genPlaylist:
    def generate_playlist_data(self, num_play, num_tracks, num_users):
        play_data = []
        for i in range(num_play):
            play_name = f'A very cool playlist {i+1}'
            track_id = random.randint(1, num_tracks)
            user_id = random.randint(1, num_users)
            sql = f"INSERT INTO playlists (play_name, music_tracks_track_id, user_user_id) " \
                  f"VALUES ('{play_name}', {track_id}, {user_id})"
            play_data.append(sql)

        with open('play_data.txt', 'w') as f:
            for sql in play_data:
                f.write(sql + '\n')
        return play_data

class genConcert:
    def generate_concert_info(self, num_conc, num_prod):
        cities = {
            "New York": "USA",
            "Tokyo": "Japan",
            "Paris": "France",
            "Sydney": "Australia",
            "Dubai": "United Arab Emirates",
            "Rome": "Italy",
            "Toronto": "Canada",
            "Cairo": "Egypt",
            "Moscow": "Russia",
            "Rio de Janeiro": "Brazil"
        }
        conc_data = []
        for i in range(num_conc):
            name = f"Woah! A concert {i+1} !!!"

            city, country = random.choice(list(cities.items()))
            place = f"{city}, {country}"

            start_date = datetime.now().replace(hour=14, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=3 * 365) + timedelta(days=1)

            hour_choices = [14, 15, 16, 17, 18, 19, 20]

            date = datetime(
                random.randint(start_date.year, end_date.year),
                random.randint(start_date.month, end_date.month),
                random.randint(start_date.day, end_date.day),
                random.choice(hour_choices),
                random.choice([0, 30])
            )

            date_str = date.strftime('%Y-%m-%d %H:%M:%S')
            desc = f'A short description for a concert {i+1} !!!'
            prod_id = random.randint(1, num_prod)
            sql = f"INSERT INTO concert_info (name, place, \"date\", description, producer_prod_id) " \
                  f"VALUES ('{name}', '{place}', TO_DATE('{date_str}', 'YYYY-MM-DD HH24:MI:SS'), '{desc}', {prod_id})"
            conc_data.append(sql)

        with open('conc_data.txt', 'w') as f:
            for sql in conc_data:
                f.write(sql + '\n')
        return conc_data

class genRating:
    def generate_rating_data(self, num_rat, num_users, num_album, num_track):
        rat_data = []
        for i in range(num_rat):
            rating = random.choice([i for i in range(11) if i % 2 == 0 or i % 2 == 1 / 2])
            comment = None
            if random.randint(0, 1):
                if rating < 3:
                    comment = f"I hate this song!"
                elif rating <= 5:
                    comment = f"This song is meh..."
                elif rating <= 7:
                    comment = f"This song is alright!"
                else:
                    comment = f"I love this song!!!"

            rating_type = random.choice(['album', 'track'])
            if rating_type == 'album':
                album_id = random.randint(1, num_album)
                track_id = None
            else:
                album_id = None
                track_id = random.randint(1, num_track)

            user_id = random.randint(1, num_users)
            if album_id is not None and track_id is None:
                if comment is None:
                    sql = f"INSERT INTO rating (rating, \"comment\", albums_album_id, music_tracks_track_id, user_user_id) " \
                          f"VALUES({rating}, NULL, {album_id}, NULL, {user_id})"
                else:
                    sql = f"INSERT INTO rating (rating, \"comment\", albums_album_id, music_tracks_track_id, user_user_id) " \
                          f"VALUES({rating}, '{comment}', {album_id}, NULL, {user_id})"
            elif album_id is None and track_id is not None:
                if comment is None:
                    sql = f"INSERT INTO rating (rating, \"comment\", albums_album_id, music_tracks_track_id, user_user_id) " \
                          f"VALUES({rating}, NULL, NULL, {track_id}, {user_id})"
                else:
                    sql = f"INSERT INTO rating (rating, \"comment\", albums_album_id, music_tracks_track_id, user_user_id) " \
                          f"VALUES({rating}, '{comment}', NULL, {track_id}, {user_id})"

            rat_data.append(sql)
        with open('rat_data.txt', 'w') as f:
            for sql in rat_data:
                f.write(sql + '\n')
        return rat_data

class servers:
    def generate_server_data(self, num_servers):
        domains = {
            "North America": "spidal.na",
            "South America": "spidal.sa",
            "Europe": "spidal.eu",
            "Asia": "spidal.as",
            "Africa": "spidal.af",
            "Oceania": "spidal.oc"
        }
        regions = {
            "Europe": "EUR",
            "Asia": "ASIA",
            "North America": "NOAM",
            "South America": "SOAM",
            "Africa": "AFR",
            "Oceania": "OCN"
        }
        server_data = []
        for i in range(num_servers):
            domain = f"{random.choice(list(domains.values()))}{i}"
            region = random.choice(list(regions.keys()))
            region_short = regions[region]
            is_up = random.choices(['Y', 'N'], weights=[90, 10], k=1)[0]
            sql = f"INSERT INTO server (domain, region, is_up) " \
                  f"VALUES ('{domain}', '{region_short}', '{is_up}')"
            server_data.append(sql)

        with open('server_data.txt', 'w') as f:
            for sql in server_data:
                f.write(sql + '\n')
        return server_data

class relations:
    def generate_relation_12_data(self, num_rel, num_servers, num_conc):
        rel12_data = []
        existing_pairs = set()
        while len(rel12_data) < num_rel:
            server_id = random.randint(1, num_servers)
            concert_id = random.randint(1, num_conc)
            if (server_id, concert_id) not in existing_pairs:
                sql = f"INSERT INTO relation_12 (server_server_id, concert_info_conc_id) " \
                      f"VALUES ({server_id}, {concert_id})"
                rel12_data.append(sql)
                existing_pairs.add((server_id, concert_id))
        with open('rel12_data.txt', 'w') as f:
            for sql in rel12_data:
                f.write(sql + '\n')
            f.close()
        return rel12_data

    def generate_relation_13_data(self, num_rel, num_servers, num_album):
        rel13_data = []
        existing_pairs = set()
        while len(rel13_data) < num_rel:
            server_id = random.randint(1, num_servers)
            album_id = random.randint(1, num_album)
            if (server_id, album_id) not in existing_pairs:
                sql = f"INSERT INTO relation_13 (server_server_id, albums_album_id) " \
                      f"VALUES({server_id}, {album_id})"
                rel13_data.append(sql)
                existing_pairs.add((server_id, album_id))
        with open('rel13_data.txt', 'w') as f:
            for sql in rel13_data:
                f.write(sql + '\n')
            f.close()
        return rel13_data

    def generate_relation_16_data(self, num_rel, num_track, num_servers):
        rel16_data = []
        existing_pairs = set()
        while len(rel16_data) < num_rel:
            track_id = random.randint(1, num_track)
            server_id = random.randint(1, num_servers)
            if (track_id, server_id) not in existing_pairs:
                sql = f"INSERT INTO relation_16 (music_tracks_track_id, server_server_id) " \
                      f"VALUES({track_id}, {server_id})"
                rel16_data.append(sql)
                existing_pairs.add((track_id, server_id))
        with open('rel16_data.txt', 'w') as f:
            for sql in rel16_data:
                f.write(sql + '\n')
            f.close()
        return rel16_data

    def generate_relation_17_data(self, num_rel, num_rat, num_servers):
        rel17_data = []
        existing_pairs = set()
        while len(rel17_data) < num_rel:
            rat_id = random.randint(1, num_rat)
            server_id = random.randint(1, num_servers)
            if (rat_id, server_id) not in existing_pairs:
                sql = f"INSERT INTO relation_17 (rating_rat_id, server_server_id) " \
                      f"VALUES({rat_id}, {server_id})"
                rel17_data.append(sql)
                existing_pairs.add((rat_id, server_id))
        with open('rel17_data.txt', 'w') as f:
            for sql in rel17_data:
                f.write(sql + '\n')
            f.close()
        return rel17_data
