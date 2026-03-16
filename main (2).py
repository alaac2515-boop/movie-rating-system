class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

class MovieSystem:
    def __init__(self):
        self.movies_list = []

    def add_movie(self, title, rating):
        new_movie = Movie(title, rating)
        self.movies_list.append(new_movie)
        print(f"Success! '{title}' has been added.")

    def display_movies(self):
        print("\n--- Final Movie Ratings List ---")
        for movie in self.movies_list:
            print(f"Movie: {movie.title} | Rating: {movie.rating}/10")

my_system = MovieSystem()

print("Welcome to the Movie Rating System!")

for i in range(3):
    title_input = input("\nEnter movie title (or type 'exit' to finish): ")
    
    if title_input.lower() == 'exit':
        break
        
    try:
        rating_input = float(input(f"Enter rating for '{title_input}' (0-10): "))
        my_system.add_movie(title_input, rating_input)
    except ValueError:
        print("Invalid input! Please enter a number.")

my_system.display_movies()
print("\nSystem finished. Thank you!")