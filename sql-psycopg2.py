"""psycopg2 library
"""
import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of database
# (This is a set or list, smilar to an array in JS)
cursor = connection.cursor()

# Query 1 - Select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ['Queen'])

# Query 4 - Select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')

# Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 51')

# Query 6
# - Select all tracks wehre the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7
# - Select all tracks where the composer is "Isham Jones & Marty Symes"
# from the "Track" table
# cursor.execute(
#     'SELECT * FROM "Track" WHERE "Composer" = %s',
#     ['Isham Jones & Marty Symes'])

# Query 8
# - Select all tracks where the composer is "test" from the "Track" table
# "test" is invalid: terminal shows nothing.
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['test'])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result)
