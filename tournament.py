#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

# connects to the database
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    # Deletes all rows from the matches table
    c.execute("DELETE FROM matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    #Deletes all rows from the players table
    c.execute("DELETE FROM players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    # counts the number of players in the players table
    c.execute("SELECT count(*) as num FROM players;")
    # stores the result in the "num" variable so it can be returned
    num = c.fetchone()
    db.commit()
    db.close()
    # returns the result as a number as opposed to the original format of # a list
    return num[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    # Adds a player to the players table
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    # Counts all of the times the player's id shows up in either the
    # winner or loser colum of the matches table.  
    c.execute("SELECT players.id, players.name, players.wins, count(matches.match_id) AS matches FROM players LEFT JOIN matches ON players.id = matches.winner OR players.id = matches.loser GROUP BY players.id ORDER BY players.wins DESC;")
    result = c.fetchall()
    db.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    # Inserts the result of the match into the matches tables
    c.execute("INSERT INTO matches (winner, loser) VALUES (('%s'), ('%s'))", (winner, loser,))
    # Increments the win column by 1 to the winner of the match
    c.execute("UPDATE players SET wins = wins + 1 WHERE id = ('%s')", (winner,))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # initiates an index to be used in the while loop
    i = 0
    # initiates the result list to be returned
    result = []
    db = connect()
    c = db.cursor()
    # retrieves the id and name of each player, sorted in descending
    # order by number of wins
    c.execute("SELECT id, name FROM players ORDER BY wins DESC;")
    # assigns all of the data from the query to the "order" variable
    order = c.fetchall()
    db.close()
    # determines the number of players in the match
    numPlayers = len(order)
    # reformats the query to a list of truples containing
    # (id1, name1, id2, name2) 
    while (i < numPlayers):
        match = (order[i][0], order[i][1], order[i+1][0], order[i+1][1])
        result.append(match)
        i = i + 2
    return result