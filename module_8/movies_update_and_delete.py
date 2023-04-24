import mysql.connector

def show_films(cursor, title):
    # Inner join query
    cursor.execute("""
        SELECT film_name AS Name, film_director AS Director,
               genre_name AS Genre, studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    
    # Get the results from cursor object
    films = cursor.fetchall()
    
    print("\n--{}--".format(title))
    
        # Iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]
        ))
        
# Connect to the MySQL database
conn = mysql.connector.connect(
    user = "movies_user",
    password = "popcorn",
    host = "127.0.0.1",
    database = "movies",
)

# Create a cursor object
cursor = conn.cursor()

# Call the show_films function
show_films(cursor, "DISPLAYING FILMS")

# Close the database connection
conn.close()
