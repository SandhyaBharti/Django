from movies import movies


def display_movie(movie):
    print("\n-------------------------")
    print("Title  :", movie["title"])
    print("Genre  :", movie["genre"])
    print("Year   :", movie["year"])
    print("Rating :", movie["rating"])
    print("-------------------------")


def show_all_movies():
    print("\n===== ALL MOVIES =====")

    for movie in movies:
        display_movie(movie)


def search_by_title():
    title = input("\nEnter movie name: ").lower()

    found = False

    for movie in movies:
        if title in movie["title"].lower():
            display_movie(movie)
            found = True

    if not found:
        print("\nMovie not found.")


def search_by_genre():
    genre = input("\nEnter genre: ").lower()

    found = False

    for movie in movies:
        if movie["genre"].lower() == genre:
            display_movie(movie)
            found = True

    if not found:
        print("\nNo movies found for this genre.")


def search_by_year():
    year = int(input("\nEnter release year: "))

    found = False

    for movie in movies:
        if movie["year"] == year:
            display_movie(movie)
            found = True

    if not found:
        print("\nNo movies found for this year.")


def main():

    while True:

        print("\n==========================")
        print("       MOVIE FINDER")
        print("==========================")

        print("1. Show All Movies")
        print("2. Search Movie")
        print("3. Search by Genre")
        print("4. Search by Year")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_all_movies()

        elif choice == "2":
            search_by_title()

        elif choice == "3":
            search_by_genre()

        elif choice == "4":
            search_by_year()

        elif choice == "5":
            print("\nThank you for using Movie Finder!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()