# Movie and Actor Management System (Python)

This project implements a simple Movie and Actor management system using Python object-oriented programming. It supports creating, storing, searching, and removing Movie and Actor objects, with input validation to ensure data integrity.

## Features

### Movie Management
- Create movie objects with:
  - Title
  - Release year (must be ≥ 1888)
  - Genre
  - Release date (YYYY-MM-DD)
- Automatically generates a unique Movie ID using `uuid.uuid4()`.
- Store movies in `MovieList` (dictionary by movie ID).
- Search movies by title, genre, or release date.
- Remove movies by title.
- Display total number of movies in collection.

### Actor Management
- Create actor objects with:
  - First name
  - Surname
  - Gender (`Male`, `Female`, `Other`)
  - Date of birth (YYYY-MM-DD)
- Store actors in `ActorsList` (list of actors).
- Search actors by first name.
- Remove actors by first name (with optional surname matching to avoid ambiguity).
- Display total number of actors in the collection.

## Requirements
- Python 3.8 or above
- No external libraries required

## Running the Program
1. Save the code in a file, for example `main.py`.
2. Run the script using:
   ```bash
   python main.py
Input Validation

The system ensures:

Names and genre must be non-empty strings.

Year must be an integer ≥ 1888.

Dates must match YYYY-MM-DD format.

Gender must be one of: Male, Female, Other.

Invalid input will raise ValueError or TypeError.
