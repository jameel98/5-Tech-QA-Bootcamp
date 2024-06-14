def movies_list():
    movie_list = ["movie1", "movie2", "movie3", "movie4", "movie5"]
    print(movie_list)
    movie_list.append("new movie")
    print(movie_list)


def actors_set():
    actor_set = {"Leonardo DiCaprio", "Dwayne Johnson", "Denzel Washington"}
    print("Initial set of actors:", actor_set)
    actor_set.add("Leonardo DiCaprio")
    print("Set after adding a duplicate actor:", actor_set)


def rate_dict():
    movie_ratings = {}
    movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "12 Angry Men", "Schindler's List"]
    ratings = [9.3, 9.2, 9.0, 9.0, 8.9]

    for movie, rating in zip(movies, ratings):
        movie_ratings[movie] = rating

    print("Movie Ratings Dictionary:")
    for movie, rating in movie_ratings.items():
        print(f"{movie}: {rating}")

    # Output the dictionary
    print("\nComplete Dictionary:")
    print(movie_ratings)


def initialize_movie_data():
    movies = ["Inception", "The Devil Wears Prada", "Training Day"]
    actors = [
        ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],  # Inception
        ["Meryl Streep", "Anne Hathaway", "Emily Blunt"],  # The Devil Wears Prada
        ["Denzel Washington", "Ethan Hawke", "Scott Glenn"]  # Training Day
    ]
    ratings = [8.8, 6.9, 7.7]

    movie_actors_dict = {movie: actor_list for movie, actor_list in zip(movies, actors)}
    rating_dict = {movie: rate for movie, rate in zip(movies, ratings)}

    return movie_actors_dict, rating_dict


def display_data(movie_actors_dict, rating_dict):
    print(f"This is the movie actors dict: {movie_actors_dict}")
    print(f"This is the rating dict: {rating_dict}")


def add_new_movie(rating_dict, new_movie, default_rate):
    if new_movie not in rating_dict:
        rating_dict[new_movie] = default_rate
        print(f"Added '{new_movie}' with default rating {default_rate}.")
    else:
        print(f"'{new_movie}' already exists in the rating dictionary.")


def advanced():
    default_rate = 5
    movie_actors_dict, rating_dict = initialize_movie_data()
    display_data(movie_actors_dict, rating_dict)

    while True:
        new_movie = input("Add a movie to the list (or press enter to stop): ")
        if not new_movie:
            break
        add_new_movie(rating_dict, new_movie, default_rate)


if __name__ == '__main__':
    advanced()
