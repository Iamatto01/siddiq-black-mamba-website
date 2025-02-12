from flask import Flask, render_template
import wikipediaapi

app = Flask(__name__)

def get_population_data():
    wiki = wikipediaapi.Wikipedia("en")
    page = wiki.page("World_population")

    if page.exists():
        return page.summary[:1000]  # Return first 1000 characters of summary
    else:
        return "Page not found!"

@app.route('/')
def index():
    population_data = get_population_data()
    return render_template('index.html', population_data=population_data)

if __name__ == '__main__':
    app.run(debug=True)
