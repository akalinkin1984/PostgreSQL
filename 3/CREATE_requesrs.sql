CREATE TABLE IF NOT EXISTS genre(
	id SERIAL PRIMARY KEY,
	genre_title VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS artists(
	id SERIAL PRIMARY KEY,
	artist VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS genre_Artist(
	id SERIAL PRIMARY KEY,
	genre_id INTEGER NOT NULL REFERENCES Genre(id),
	artist_id INTEGER NOT NULL REFERENCES Artists(id)
);

CREATE TABLE IF NOT EXISTS album(
	id SERIAL PRIMARY KEY,
	release_year INTEGER NOT NULL CHECK(release_year BETWEEN 1900 AND EXTRACT(YEAR FROM NOW())),
	album_title VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS artist_Album(
	id SERIAL PRIMARY KEY,
	artist_id INTEGER NOT NULL REFERENCES Artists(id),
	album_id INTEGER NOT NULL REFERENCES Album(id)
);

CREATE TABLE IF NOT EXISTS track(
	id SERIAL PRIMARY KEY,
	album_id INTEGER NOT NULL REFERENCES Album(id),
	duration INTEGER NOT NULL CHECK(duration > 0), --Продолжительность в секундах
	track_title VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS collection(
	id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	release_year INTEGER NOT NULL CHECK(release_year BETWEEN 1900 AND EXTRACT(YEAR FROM NOW()))
);

CREATE TABLE IF NOT EXISTS track_collection(
	id SERIAL PRIMARY KEY,
	track_id INTEGER NOT NULL REFERENCES Track(id),
	collection_id INTEGER NOT NULL REFERENCES Collection(id)
);