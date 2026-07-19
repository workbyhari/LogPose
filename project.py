# LogPose: Offline IMBD Content Recommendation Engine
import gzip
import random
from tabulate import tabulate

def main():
    typ = chosen_type()
    imbd = chosen_imbd()
    gen = chosen_gen()
    year = chosen_year()  
    
    print("\nFetching data... Please wait.")
    data = fetch_data(typ, imbd, gen, year)
    
    display_results(data)


def fetch_data(typ, imbd, gen, year):
    filter_content = {}
    with gzip.open("title.basics.tsv.gz", "rt", encoding="utf-8") as f:
        for lines in f:
            try:
                a = lines.strip().split("\t")
                b = a[8]
                genre = b.split(",")
                if a[1] == typ and a[5] == str(year) and genre[0] == gen:
                    filter_content[a[0]] = a[3]
            except (IndexError, ValueError):
                continue

    
    def rating():
        with gzip.open("title.ratings.tsv.gz", "rt", encoding="utf-8") as f:       
            final_result = {}
            for lines in f:
                try:
                    a = lines.strip().split("\t")
                    tcode = a[0]
                    ratings = a[1]
                    num_votes = a[2]
                    
                    if tcode in filter_content:
                        
                        if float(ratings) >= imbd and int(num_votes) > 500:
                            series_name = filter_content[tcode]
                            final_result[tcode] = {
                                "title": series_name,
                                "rating": ratings,
                                "votes": num_votes
                            }
                    if 1 <= len(final_result) == 10:
                        break
                except (IndexError, ValueError):
                    continue
        return final_result

    
    return rating()



def chosen_year():
    while True:
        try:
            year_input = input("Enter preferred release year (e.g., 2024, 2025): ").strip()
            year = int(year_input)
            
            
            if year < 1888 or year > 2030:
                print("Please enter a valid year between 1888 and 2030.")
                continue
            return year
        except ValueError:
            print("Invalid input! Please enter a 4-digit number (e.g., 2025).")



def display_results(data):
    if not data:
        print("\n" + "="*50)
        print("Content not found for your preferences.")
        print("="*50 + "\n")
        return

    table_data = []
   
    for tcode, details in data.items():
        table_data.append([tcode, details['title'], details['rating'], details['votes']])

    headers = ["IMDb ID", "Title", "Rating", "Votes"]
    
    print("\n" + "="*20 + " YOUR TOP RECOMMENDATIONS " + "="*20)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print("="*69 + "\n")


# 4. Genre Selection Function
def chosen_gen():
    while True:
        try:
            
            type_list = [
                ["Action"], 
                ["Adventure"],
                ["Animation"],
                ["Comedy"], 
                ["Crime"], 
                ["Drama"], 
                ["Fantasy"],
                ["Romance"], 
                ["Sci-Fi"], 
                ["Thriller"]
            ]
            
            header = ["Genre"]
            fmt = tabulate(type_list, headers=header, tablefmt="grid")
            print(fmt)

            print('\nUnsure about the preferences? Type "random" in the preferred genre.\n')
            gen = input("Preferred genre: ").strip()
            
            
            valid_genres = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Drama", "Fantasy", "Romance", "Sci-Fi", "Thriller"]
            
            
            matched_genre = None
            for g in valid_genres:
                if gen.lower() == g.lower():
                    matched_genre = g
                    break
            
            if gen.lower() == "random":
                matched_genre = random.choice(valid_genres)
                print(f'\nSo, our preferred Genre for you is "{matched_genre}"\n')
                return matched_genre
                
            elif matched_genre is None:
                print("Enter a valid genre from the table above!")
                continue
                
            return matched_genre
            
        except ValueError:
            print("Please ensure your preferences before entering.")
            continue


def chosen_imbd():
    while True:
        try:
            imbd = float(input("\nPreferred minimum IMDb Rating (e.g., 8.5): "))
            if not 1.0 <= imbd <= 10.0:
                print('Range should be between 1.0 and 10.0')
                continue
            return imbd
        except ValueError:
            print("Enter a valid decimal number ranging between 1.0 and 10.0")



def chosen_type():
    while True:
        
        type_options = [
            ["movie"], 
            ["tvSeries"], 
            ["short"], 
            ["tvMiniSeries"]
        ]
        headers = ["Preferred Content Type:"]
        print("\n" + tabulate(type_options, headers=headers, tablefmt="grid"))

        typ = input("Your choice: ").strip()
        
        
        if typ not in ("movie", "tvSeries", "short", "tvMiniSeries"):
            print("\nInvalid Content Type! Please match the case exactly as shown.\n")
            continue
        return typ


if __name__ == "__main__":
    main()
###########################################################


