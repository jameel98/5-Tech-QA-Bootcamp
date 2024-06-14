import datetime


def get_current_time():
    return datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")


def write_log(entry):
    try:
        with open('time_log.txt', 'a') as file:  # Use 'a' mode to append
            file.write(entry)
    except IOError as e:
        print(f"An IOError occurred: {e}")


def print_log():
    try:
        with open('time_log.txt', 'r') as file:
            content = file.read()
            print("All log entries:")
            print(content)
    except IOError as e:
        print(f"An IOError occurred: {e}")


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
        log_entry = f"{get_current_time()} - Added movie '{new_movie}' with default rating {default_rate}.\n"
        write_log(log_entry)
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
    while True:
        func = input("write 1 to add movie\nwrite 2 to print log\n")
        if func == '1':  # Compare with string '1'
            advanced()
        elif func == '2':  # Compare with string '2'
            print_log()
        else:
            break
