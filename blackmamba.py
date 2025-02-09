import wikipediaapi

def get_population_data():
    wiki = wikipediaapi.Wikipedia("en")
    page = wiki.page("World_population")

    if page.exists():
        print("Fetching data from Wikipedia...")
        print(page.summary[:1000])  # Print first 1000 characters of summary
    else:
        print("Page not found!")

get_population_data()
