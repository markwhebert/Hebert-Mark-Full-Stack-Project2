-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines 

-- Creates the players table, which holds the Player's ID (id) as the 
-- primary key, the Player's Name (name) and their number of wins (win)
CREATE TABLE players (id serial PRIMARY KEY, name text, wins integer DEFAULT 0);

-- Creates the matches table, which holds the match id (match_id) as the 
-- primary key, the Player ID of the winning player (winner) and the
-- Player ID of the losing player (loser)
CREATE TABLE matches (match_id serial PRIMARY KEY, winner integer REFERENCES players(id), loser integer REFERENCES players(id));