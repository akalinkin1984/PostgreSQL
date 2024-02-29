--------Первое задание--------

----Жанры----
INSERT INTO genre(genre_title)
VALUES ('pop');

INSERT INTO genre(genre_title)
VALUES ('rock');

INSERT INTO genre(genre_title)
VALUES ('chanson');

INSERT INTO genre(genre_title)
VALUES ('punk');

INSERT INTO genre(genre_title)
VALUES ('metal');

----Исполнители----
INSERT INTO artists(artist)
VALUES ('Britney Spears');

INSERT INTO artists(artist)
VALUES ('Агата Кристи');

INSERT INTO artists(artist)
VALUES ('Red Hot Chili Peppers');

INSERT INTO artists(artist)
VALUES ('Король и Шут');

INSERT INTO artists(artist)
VALUES ('Михаил Круг');

INSERT INTO artists(artist)
VALUES ('Петлюра');

INSERT INTO artists(artist)
VALUES ('BLACKPINK');

----Жанры-исполнители----
INSERT INTO genre_artist(genre_id, artist_id)
VALUES (1, 1);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES (2, 2);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES (2, 3);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES (3, 5);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES (3, 6);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES (4, 4);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES (1, 7);

INSERT INTO genre_artist(genre_id, artist_id)
VALUES (2, 4);


----Альбомы----
INSERT INTO album(release_year, album_title)
VALUES (2002, 'Жаль, нет ружья');

INSERT INTO album(release_year, album_title)
VALUES (1998, 'Мадам');

INSERT INTO album(release_year, album_title)
VALUES (2007, 'Blackout');

INSERT INTO album(release_year, album_title)
VALUES (1994, 'Опиум');

INSERT INTO album(release_year, album_title)
VALUES (1999, 'Californication');

INSERT INTO album(release_year, album_title)
VALUES (1995, 'Малолетка');

INSERT INTO album(release_year, album_title)
VALUES (2020, 'THE ALBUM');

----Артисты-альбомы----
INSERT INTO artist_album(artist_id, album_id)
VALUES (1, 3);

INSERT INTO artist_album(artist_id, album_id)
VALUES (2, 4);

INSERT INTO artist_album(artist_id, album_id)
VALUES (3, 5);

INSERT INTO artist_album(artist_id, album_id)
VALUES (4, 1);

INSERT INTO artist_album(artist_id, album_id)
VALUES (5, 2);

INSERT INTO artist_album(artist_id, album_id)
VALUES (6, 6);

INSERT INTO artist_album(artist_id, album_id)
VALUES (7, 7);

----Треки----
INSERT INTO track(album_id, duration, track_title)
VALUES (1, 351, 'Мой характер');

INSERT INTO track(album_id, duration, track_title)
VALUES (1, 247, 'Мёртвый анархист');

INSERT INTO track(album_id, duration, track_title)
VALUES (2, 174, 'Красные карманы');

INSERT INTO track(album_id, duration, track_title)
VALUES (3, 208, 'Ooh Ooh Baby');

INSERT INTO track(album_id, duration, track_title)
VALUES (4, 339, 'Халигаликришна');

INSERT INTO track(album_id, duration, track_title)
VALUES (5, 163, 'Porcelain');

INSERT INTO track(album_id, duration, track_title)
VALUES (6, 165, 'Бродяга');

INSERT INTO track(album_id, duration, track_title)
VALUES (7, 179, 'How You Like That');

INSERT INTO track(album_id, duration, track_title)
VALUES (4, 180, 'Сказочная тайга');

----Сборники----
INSERT INTO collection(title, release_year)
VALUES ('Сборник Панк-рока', 2018);

INSERT INTO collection(title, release_year)
VALUES ('Сборник Панк-рока 2', 2019);

INSERT INTO collection(title, release_year)
VALUES ('Сборник Поп-рока', 2010);

INSERT INTO collection(title, release_year)
VALUES ('Сборник Шансона', 2000);

INSERT INTO collection(title, release_year)
VALUES ('Сборник Поп-музыки', 2023);

----Треки-Сборники----
INSERT INTO track_collection(track_id, collection_id)
VALUES (1, 1);

INSERT INTO track_collection(track_id, collection_id)
VALUES (5, 1);

INSERT INTO track_collection(track_id, collection_id)
VALUES (2, 2);

INSERT INTO track_collection(track_id, collection_id)
VALUES (5, 2);

INSERT INTO track_collection(track_id, collection_id)
VALUES (4, 3);

INSERT INTO track_collection(track_id, collection_id)
VALUES (6, 3);

INSERT INTO track_collection(track_id, collection_id)
VALUES (8, 3);

INSERT INTO track_collection(track_id, collection_id)
VALUES (3, 4);

INSERT INTO track_collection(track_id, collection_id)
VALUES (7, 4);

INSERT INTO track_collection(track_id, collection_id)
VALUES (4, 5);

INSERT INTO track_collection(track_id, collection_id)
VALUES (8, 5);
