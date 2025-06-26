import requests
import csv



CSV_FILE = "movies.csv"

def fetch_movie_data(title):
    base_url = "http://www.omdbapi.com"
    params = {
        "t": title,
        "apikey": "bdd9467c"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return {
                "Title": data.get("Title"),
                "Year": data.get("Year"),
                "Director": data.get("Director"),
                "Genre": data.get("Genre"),
                "imdbRating": data.get("imdbRating")
            }
        else:
            print("Movie not found on OMDb API.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

def save_movie_to_csv(movie_data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Year","Director," "Genre", "imdbRating"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(movie_data)
    print(f"Movie '{movie_data['Title']}' saved to {CSV_FILE}")

def search_movie_in_csv(title):
    if not os.path.exists(CSV_FILE):
        print("No movie data file found.")
        return
    found = False
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Title"].lower() == title.lower():
                print(f"Found: {row}")
                found = True
                break
    if not found:
        print("The movie is not found.")

def main():
    while True:
        print("\n=== Movie App Menu ===")
        print("1. Add movie using OMDb API")
        print("2. Search movie in CSV file")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter movie name: ").strip()
            movie_data = fetch_movie_data(title)
            if movie_data:
                save_movie_to_csv(movie_data)
        elif choice == "2":
            title = input("Enter movie name to search: ").strip()
            search_movie_in_csv(title)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
