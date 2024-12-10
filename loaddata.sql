CREATE TABLE tunaapi_artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL,
    bio VARCHAR(50) NOT NULL
);

CREATE TABLE tunaapi_song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50) NOT NULL,
    artist_id INTEGER NOT NULL,
    album VARCHAR(50) NOT NULL,
    length INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id) ON DELETE CASCADE
);

CREATE TABLE tunaapi_genre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(50) NOT NULL
);

CREATE TABLE tunaapi_songgenre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    FOREIGN KEY (song_id) REFERENCES song(id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genre(id) ON DELETE CASCADE
);












INSERT INTO tunaapi_artist (name, age, bio) VALUES 
('Kendrick Lamar', 37, 'A Grammy-winning rapper and songwriter, known for introspective lyrics and storytelling.'),
('Sting', 73, 'A legendary musician, songwriter, and activist with global acclaim.'),
('Imogen Heap', 46, 'A singer, songwriter, producer, and pioneer in music technology innovation.');



INSERT INTO tunaapi_genre (description) VALUES 
('Hip Hop'),
('Pop'),
('Rock'),
('Electronic');


INSERT INTO tunaapi_songgenre (song_id, genre_id) VALUES 
(1, 1), -- "Alright" (Hip Hop)
(2, 4), -- "First Train Home" (Electronic)
(3, 3), -- "Every Breath You Take" (Rock)
(4, 2), -- "Goodnight and Go" (Pop)
(5, 1), -- "HUMBLE." (Hip Hop)
(6, 3), -- "Shape of My Heart" (Rock)
(7, 3), -- "The A Team" (Rock)
(8, 4), -- "Hide and Seek" (Electronic)
(9, 3), -- "Fields of Gold" (Rock)
(10, 1); -- "DNA." (Hip Hop)


INSERT INTO tunaapi_song (title, artist_id, album, length) VALUES
('Alright', 1, 'To Pimp a Butterfly', 373),
('First Train Home', 3, 'Ellipse', 295),
('Every Breath You Take', 2, 'Synchronicity', 293),
('Goodnight and Go', 3, 'Speak for Yourself', 214),
('HUMBLE.', 1, 'DAMN.', 204),
('Shape of My Heart', 2, 'Ten Summoner''s Tales', 320),
('The A Team', 2, 'The Last Ship', 279),
('Hide and Seek', 3, 'Speak for Yourself', 290),
('Fields of Gold', 2, 'Ten Summoner''s Tales', 256),
('DNA.', 1, 'DAMN.', 258);


SELECT name FROM sqlite_master WHERE type='table';


SELECT * FROM Artist;
DELETE FROM song;
SELECT * FROM Genre;
SELECT * FROM SongGenre;
SELECT * FROM Song;

PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;

DELETE * FROM tunaapi_Song;

DROP TABLE Song;
DROP TABLE IF EXISTS tunaapi_song_genre;






DROP TABLE IF EXISTS Artist;