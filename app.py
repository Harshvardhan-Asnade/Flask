from flask import Flask,render_template,request
import requests 

app = Flask(__name__)



def fetch_movies():
    url = "https://api.themoviedb.org/3/trending/movie/week"
    params={
        "api_key":"9b00a8153736b7c4f78662ac037bbb99"
    }
    response=requests.get(url,params=params)
    data=response.json()
    return data["results"]
def fetch_movie_detail(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": "9b00a8153736b7c4f78662ac037bbb99"}

    response = requests.get(url, params=params)
    return response.json()
@app.route('/', methods=['GET', 'POST'])
def home():
    movies = fetch_movies()

    if request.method == 'POST':
        search = request.form.get('search')

        if search:   
            movies = search_movies(search)

    return render_template('index.html', movies=movies)
@app.route('/movies/<int:id>')
def movie_detail(id):
    movie=fetch_movie_detail(id)
    videos = fetch_videos(id)
    if movie:
        return render_template('movie_detail.html', movie=movie, videos=videos)
    
def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": "9b00a8153736b7c4f78662ac037bbb99",
        "query": query
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("results", [])

def fetch_videos(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
    params = {"api_key": "9b00a8153736b7c4f78662ac037bbb99"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("results", [])

if __name__=='__main__':
    app.run(debug=True,port=9100)