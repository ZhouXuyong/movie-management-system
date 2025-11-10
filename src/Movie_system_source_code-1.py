import uuid
from datetime import datetime

# Movie class to store details about a movie
class Movie:
    def __init__(self, title, year, genre, release_date):
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(year, int) or year < 1888:  # The first film was made in 1888
            raise ValueError("Year must be a valid integer greater than or equal to 1888.")
        if not genre or not isinstance(genre, str):
            raise ValueError("Genre must be a non-empty string.")
        if not release_date or not isinstance(release_date, str):
            raise ValueError("Release date must be a non-empty string in YYYY-MM-DD format.")
        # Validate release date format
        try:
            datetime.strptime(release_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Release date must be in YYYY-MM-DD format.")

        self.movie_id = str(uuid.uuid4())  # Generate a unique ID for the movie
        self.title = title  # Title of the movie
        self.year = year  # The year the movie was released
        self.genre = genre  # The genre of the movie
        self.release_date = release_date  # The release date in YYYY-MM-DD format

    # Methods to set and get movie attributes
    def set_title(self, title):
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        self.title = title

    def get_title(self):
        return self.title

    def set_year(self, year):
        if not isinstance(year, int) or year < 1888:
            raise ValueError("Year must be a valid integer greater than or equal to 1888.")
        self.year = year

    def get_year(self):
        return self.year

    def set_genre(self, genre):
        if not genre or not isinstance(genre, str):
            raise ValueError("Genre must be a non-empty string.")
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_release_date(self, release_date):
        if not release_date or not isinstance(release_date, str):
            raise ValueError("Release date must be a non-empty string in YYYY-MM-DD format.")
        # Validate release date format
        try:
            datetime.strptime(release_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Release date must be in YYYY-MM-DD format.")
        self.release_date = release_date

    def get_release_date(self):
        return self.release_date

# MovieList class to manage a collection of movies
class MovieList:
    def __init__(self):
        self.movies = {}  # Dictionary to store movies using movie_id as the key

    def add_movie(self, movie):
        if not isinstance(movie, Movie):
            raise TypeError("Only instances of Movie can be added.")
        self.movies[movie.movie_id] = movie  # Add the movie to the collection

    def find_movie(self, title=None, genre=None, release_date=None):
        results = []  # List to store matching movies
        for movie in self.movies.values():
            if (title and movie.title == title) or \
               (genre and movie.genre == genre) or \
               (release_date and movie.release_date == release_date):
                results.append(movie)
        return results

    def remove_movie(self, title):
        for movie_id, movie in list(self.movies.items()):
            if movie.title == title:
                del self.movies[movie_id]  # Remove the movie by title
                return True
        return False

    def total_movies(self):
        return len(self.movies)  # Return the total number of movies in the collection

# Actor class to store details about an actor
class Actor:
    def __init__(self, first_name, surname, gender, date_of_birth):
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name must be a non-empty string.")
        if not surname or not isinstance(surname, str):
            raise ValueError("Surname must be a non-empty string.")
        if gender not in ["Male", "Female", "Other"]:
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'.")
        if not date_of_birth or not isinstance(date_of_birth, str):
            raise ValueError("Date of birth must be a non-empty string in YYYY-MM-DD format.")
        # Validate date_of_birth format
        try:
            datetime.strptime(date_of_birth, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date of birth must be in YYYY-MM-DD format.")

        self.first_name = first_name  # First name of the actor
        self.surname = surname  # Surname of the actor
        self.gender = gender  # Gender of the actor
        self.date_of_birth = date_of_birth  # Date of birth in YYYY-MM-DD format

    # Methods to set and get actor attributes
    def set_first_name(self, first_name):
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name must be a non-empty string.")
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_surname(self, surname):
        if not surname or not isinstance(surname, str):
            raise ValueError("Surname must be a non-empty string.")
        self.surname = surname

    def get_surname(self):
        return self.surname

    def set_gender(self, gender):
        if gender not in ["Male", "Female", "Other"]:
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'.")
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_date_of_birth(self, date_of_birth):
        if not date_of_birth or not isinstance(date_of_birth, str):
            raise ValueError("Date of birth must be a non-empty string in YYYY-MM-DD format.")
        # Validate date_of_birth format
        try:
            datetime.strptime(date_of_birth, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date of birth must be in YYYY-MM-DD format.")
        self.date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self.date_of_birth

# ActorsList class to manage a collection of actors
class ActorsList:
    def __init__(self):
        self.actors = []  # List to store actor objects

    def add_actor(self, actor):
        if not isinstance(actor, Actor):
            raise TypeError("Only instances of Actor can be added.")
        self.actors.append(actor)  # Add the actor to the collection

    def remove_actor(self, first_name, surname=None):
        # Find actors with matching first name
        matched_actors = [actor for actor in self.actors if actor.first_name == first_name and (surname is None or actor.surname == surname)]
        if len(matched_actors) > 1:
            print(f"Multiple actors with the first name {first_name} found.")
            return False
        elif matched_actors:
            self.actors.remove(matched_actors[0])  # Remove the matched actor
            return True
        else:
            print(f"No actor with the first name {first_name} found.")
            return False

    def count_actors(self):
        return len(self.actors)  # Return the total number of actors

    def find_actor(self, first_name):
        for actor in self.actors:
            if actor.first_name == first_name:
                return actor  # Return the actor if found
        return None

# Test Code
if __name__ == "__main__":
    try:
        # Create a movie object
        movie_007 = Movie("007", 1962, "Action", "1962-10-05")
        print(f"Created movie: ID: {movie_007.movie_id}, Title: {movie_007.get_title()}, "
              f"Year: {movie_007.get_year()}, Genre: {movie_007.get_genre()}, "
              f"Release Date: {movie_007.get_release_date()}")

        # Create a movie list and add the movie
        movie_collection = MovieList()
        movie_collection.add_movie(movie_007)
        print(f"Total movies in collection: {movie_collection.total_movies()}")

        # Find movie by title
        found_movies = movie_collection.find_movie(title="007")
        for movie in found_movies:
            print(f"Found movie: ID: {movie.movie_id}, Title: {movie.get_title()}, "
                  f"Year: {movie.get_year()}, Genre: {movie.get_genre()}, "
                  f"Release Date: {movie.get_release_date()}")

        # Remove the movie and check count
        if movie_collection.remove_movie("007"):
            print(f"Movie '007' removed successfully.")
        else:
            print(f"Movie '007' not found.")
        print(f"Total movies after removal: {movie_collection.total_movies()}")

        # Create an actor object
        james_bond = Actor("James", "Bond", "Male", "1920-11-11")
        print(f"Created actor: First Name: {james_bond.get_first_name()}, Surname: {james_bond.get_surname()}, "
              f"Gender: {james_bond.get_gender()}, Date of Birth: {james_bond.get_date_of_birth()}")

        # Create an actor list and add the actor
        actor_collection = ActorsList()
        actor_collection.add_actor(james_bond)
        print(f"Total actors in collection: {actor_collection.count_actors()}")

        # Find actor by first name
        found_actor = actor_collection.find_actor("James")
        if found_actor:
            print(f"Found actor: First Name: {found_actor.get_first_name()}, Surname: {found_actor.get_surname()}, "
                  f"Gender: {found_actor.get_gender()}, Date of Birth: {found_actor.get_date_of_birth()}")

        # Remove the actor and check count
        if actor_collection.remove_actor("James"):
            print(f"Actor 'James' removed successfully.")
        else:
            print(f"Actor 'James' not found.")
        print(f"Total actors after removal: {actor_collection.count_actors()}")

    except Exception as e:
        print(f"An error occurred: {e}")
