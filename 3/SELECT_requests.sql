--------Второе задание--------

--1
SELECT track_title, duration FROM track
WHERE duration = (SELECT MAX(duration) FROM track);

--2
SELECT track_title FROM track
WHERE duration >= 210;

--3
SELECT title FROM collection
WHERE release_year BETWEEN 2018 AND 2020;

--4
SELECT artist FROM artists
WHERE artist NOT LIKE '% %';

--5
SELECT track_title FROM track
WHERE track_title ILIKE '%мой%' OR track_title ILIKE '%my%';


--------Третье задание--------

--1
SELECT g.genre_title, COUNT(artist_id) FROM genre_artist AS ga
RIGHT JOIN genre AS g ON ga.genre_id = g.id 
GROUP BY g.genre_title;

--2
SELECT COUNT(track_title) FROM track AS t
JOIN album AS a ON a.id = t.album_id 
WHERE a.release_year BETWEEN 2019 AND 2020;

--3
SELECT a.album_title, AVG(duration) FROM track AS t
LEFT JOIN album AS a ON t.album_id  = a.id
GROUP BY a.album_title;

--4
SELECT artist FROM artists AS a 
JOIN artist_album AS aa ON a.id = aa.artist_id 
JOIN album AS al ON aa.album_id = al.id 
WHERE al.release_year != 2020;

--5
SELECT title FROM collection AS c
JOIN track_collection AS tc ON c.id = tc.collection_id 
JOIN track AS t ON tc.track_id = t.id 
JOIN album AS a ON t.album_id = a.id 
JOIN artist_album AS aa ON a.id = aa.album_id 
JOIN artists AS ar ON aa.artist_id = ar.id 
WHERE ar.artist  = 'Агата Кристи';


--------Четвертое задание--------

--1
SELECT album_title FROM album AS a
JOIN artist_album AS aa ON a.id = aa.album_id 
JOIN artists AS ar ON aa.artist_id = ar.id 
JOIN genre_artist AS ga ON ar.id = ga.artist_id
GROUP BY album_title 
HAVING COUNT(ga.artist_id) > 1;

--2
SELECT track_title FROM track AS t
LEFT JOIN track_collection AS tc ON t.id = tc.track_id
WHERE tc.collection_id IS NULL;

--3
SELECT artist FROM artists AS a 
JOIN artist_album AS aa ON a.id = aa.artist_id 
JOIN album AS al ON aa.album_id = al.id 
JOIN track AS t ON al.id = t.album_id 
WHERE t.duration = (SELECT MIN(duration) FROM track);

--4
SELECT album_title, COUNT(*) FROM album AS a
JOIN track AS t ON a.id = t.album_id 
GROUP BY album_title 
HAVING COUNT(*) = (
				SELECT COUNT(*) FROM album AS a
				JOIN track AS t ON a.id = t.album_id 
				GROUP BY album_title 
				ORDER BY COUNT(*) 
				LIMIT 1
					);