
#Devinder Randhawa, 04/23/2023, Module 7.2 Assignment

# Define the studio records
studio_records = [
    {"id": 1, "name": "20th Century Fox"},
    {"id": 2, "name": "Blumhouse Productions"},
    {"id": 3, "name": "Universal Pictures"}
]

# Define the genre records
genre_records = [
    {"id": 1, "name": "Horror"},
    {"id": 2, "name": "SciFi"},
    {"id": 3, "name": "Drama"}
]

# Define the short film records
short_film_records = [
    {"name": "Alien", "runtime": 117},
    {"name": "Get Out", "runtime": 104}
]

# Define the director records
director_records = [
    {"film_name": "Get Out", "director": "Jordan Peele"},
    {"film_name": "Gladiator", "director": "Ridley Scott"},
    {"film_name": "Alien", "director": "Ridley Scott"}
]

# Display the studio records
print("DISPLAYING studio RECORDS")
for record in studio_records:
    print("Studio ID: {}".format(record["id"]))
    print("Studio Name: {}\n".format(record["name"]))

# Display the genre records
print("DISPLAYING Genre RECORDS")
for record in genre_records:
    print("Genre ID: {}".format(record["id"]))
    print("Genre Name: {}\n".format(record["name"]))

# Display the short film records
print("DISPLAYING Short Film RECORDS")
for record in short_film_records:
    print("Film Name: {}".format(record["name"]))
    print("Runtime: {}\n".format(record["runtime"]))

# Display the director records in order
print("DISPLAYING Director RECORDS in Order")
for record in director_records:
    print("Film Name: {}".format(record["film_name"]))
    print("Director: {}\n".format(record["director"]))
