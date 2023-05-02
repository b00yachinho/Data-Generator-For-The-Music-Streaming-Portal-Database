CREATE TABLE server (
    server_id NUMBER GENERATED ALWAYS AS IDENTITY,
    domain    VARCHAR2(50) NOT NULL,
    region    VARCHAR2(4) NOT NULL,
    is_up     CHAR(1) NOT NULL
);

ALTER TABLE server ADD CONSTRAINT server_pk PRIMARY KEY ( server_id );

CREATE TABLE "user" (
    user_id   NUMBER GENERATED ALWAYS AS IDENTITY,
    nickname  VARCHAR2(20) NOT NULL,
    age       NUMBER,
    sex       VARCHAR2(30),
    country   VARCHAR2(30) NOT NULL,
    region    VARCHAR2(4) NOT NULL,
    sub_start DATE,
    sub_end   DATE
);

ALTER TABLE "user" ADD CONSTRAINT user_pk PRIMARY KEY ( user_id );

CREATE TABLE producer (
    prod_id    NUMBER GENERATED ALWAYS AS IDENTITY,
    prod_tag   VARCHAR2(30) NOT NULL,
    "desc"     VARCHAR2(450),
    partner    CHAR(1) NOT NULL,
    "member/s" VARCHAR2(450) NOT NULL
);

ALTER TABLE producer ADD CONSTRAINT producer_pk PRIMARY KEY ( prod_id );

CREATE TABLE albums (
    album_id         NUMBER GENERATED ALWAYS AS IDENTITY,
    name             VARCHAR2(30) NOT NULL,
    producer_prod_id NUMBER NOT NULL
);

ALTER TABLE albums ADD CONSTRAINT albums_pk PRIMARY KEY ( album_id );

CREATE TABLE concert_info (
    conc_id          NUMBER GENERATED ALWAYS AS IDENTITY,
    name             VARCHAR2(100) NOT NULL,
    place            VARCHAR2(30) NOT NULL,
    "date"           DATE NOT NULL,
    description      VARCHAR2(500) NOT NULL,
    producer_prod_id NUMBER NOT NULL
);

ALTER TABLE concert_info ADD CONSTRAINT concert_info_pk PRIMARY KEY ( conc_id );

CREATE TABLE music_tracks (
    track_id         NUMBER GENERATED ALWAYS AS IDENTITY,
    name             VARCHAR2(30) NOT NULL,
    genre            VARCHAR2(30) NOT NULL,
    producer_prod_id NUMBER NOT NULL
);

ALTER TABLE music_tracks ADD CONSTRAINT music_tracks_pk PRIMARY KEY ( track_id );

CREATE TABLE playlists (
    play_id               NUMBER GENERATED ALWAYS AS IDENTITY,
    play_name             VARCHAR2(30) NOT NULL,
    music_tracks_track_id NUMBER NOT NULL,
    user_user_id          NUMBER NOT NULL
);

ALTER TABLE playlists ADD CONSTRAINT playlists_pk PRIMARY KEY ( play_id );

CREATE TABLE rating (
    rat_id                NUMBER GENERATED ALWAYS AS IDENTITY,
    rating                NUMBER NOT NULL,
    "comment"             VARCHAR2(450),
    albums_album_id       NUMBER,
    music_tracks_track_id NUMBER,
    user_user_id          NUMBER NOT NULL
);

ALTER TABLE rating ADD CONSTRAINT rating_pk PRIMARY KEY ( rat_id );

CREATE TABLE relation_12 (
    server_server_id     NUMBER NOT NULL,
    concert_info_conc_id NUMBER NOT NULL
);

ALTER TABLE relation_12 ADD CONSTRAINT relation_12_pk PRIMARY KEY ( server_server_id, concert_info_conc_id );

CREATE TABLE relation_13 (
    server_server_id NUMBER NOT NULL,
    albums_album_id  NUMBER NOT NULL
);

ALTER TABLE relation_13 ADD CONSTRAINT relation_13_pk PRIMARY KEY ( server_server_id, albums_album_id );

CREATE TABLE relation_16 (
    music_tracks_track_id NUMBER NOT NULL,
    server_server_id      NUMBER NOT NULL
);

ALTER TABLE relation_16 ADD CONSTRAINT relation_16_pk PRIMARY KEY ( music_tracks_track_id, server_server_id );

CREATE TABLE relation_17 (
    rating_rat_id    NUMBER NOT NULL,
    server_server_id NUMBER NOT NULL
);

ALTER TABLE relation_17 ADD CONSTRAINT relation_17_pk PRIMARY KEY ( rating_rat_id, server_server_id );


ALTER TABLE albums
    ADD CONSTRAINT albums_producer_fk FOREIGN KEY ( producer_prod_id )
        REFERENCES producer ( prod_id );

ALTER TABLE concert_info
    ADD CONSTRAINT concert_info_producer_fk FOREIGN KEY ( producer_prod_id )
        REFERENCES producer ( prod_id );

ALTER TABLE music_tracks
    ADD CONSTRAINT music_tracks_producer_fk FOREIGN KEY ( producer_prod_id )
        REFERENCES producer ( prod_id );

ALTER TABLE playlists
    ADD CONSTRAINT playlists_music_tracks_fk FOREIGN KEY ( music_tracks_track_id )
        REFERENCES music_tracks ( track_id );

ALTER TABLE playlists
    ADD CONSTRAINT playlists_user_fk FOREIGN KEY ( user_user_id )
        REFERENCES "user" ( user_id );

ALTER TABLE rating
    ADD CONSTRAINT rating_albums_fk FOREIGN KEY ( albums_album_id )
        REFERENCES albums ( album_id );

ALTER TABLE rating
    ADD CONSTRAINT rating_music_tracks_fk FOREIGN KEY ( music_tracks_track_id )
        REFERENCES music_tracks ( track_id );

ALTER TABLE rating
    ADD CONSTRAINT rating_user_fk FOREIGN KEY ( user_user_id )
        REFERENCES "user" ( user_id );

ALTER TABLE relation_12
    ADD CONSTRAINT relation_12_concert_info_fk FOREIGN KEY ( concert_info_conc_id )
        REFERENCES concert_info ( conc_id );

ALTER TABLE relation_12
    ADD CONSTRAINT relation_12_server_fk FOREIGN KEY ( server_server_id )
        REFERENCES server ( server_id );

ALTER TABLE relation_13
    ADD CONSTRAINT relation_13_albums_fk FOREIGN KEY ( albums_album_id )
        REFERENCES albums ( album_id );

ALTER TABLE relation_13
    ADD CONSTRAINT relation_13_server_fk FOREIGN KEY ( server_server_id )
        REFERENCES server ( server_id );

ALTER TABLE relation_16
    ADD CONSTRAINT relation_16_music_tracks_fk FOREIGN KEY ( music_tracks_track_id )
        REFERENCES music_tracks ( track_id );

ALTER TABLE relation_16
    ADD CONSTRAINT relation_16_server_fk FOREIGN KEY ( server_server_id )
        REFERENCES server ( server_id );

ALTER TABLE relation_17
    ADD CONSTRAINT relation_17_rating_fk FOREIGN KEY ( rating_rat_id )
        REFERENCES rating ( rat_id );

ALTER TABLE relation_17
    ADD CONSTRAINT relation_17_server_fk FOREIGN KEY ( server_server_id )
        REFERENCES server ( server_id );