# 🎬 Movie Web App – Learning Project (Flask + TMDb API)

This project is a simple movie web application that fetches real-time movie data from the TMDb (The Movie Database) API and displays it using Flask.

Users can:
- Browse trending movies
- Search for movies
- View detailed movie information
- Watch movie trailers

## 🛠️ Tech Stack 
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Jinja2
- **API:** TMDb (The Movie Database API)



## ⚙️ How It Works

    User → Flask Route → API Call → JSON Data → Template → Browser UI

1. User opens the website or searches for a movie
2. Flask sends a request to TMDb API
3. API returns data in JSON format
4. Flask processes the data
5. Data is rendered using Jinja templates
6. User sees movie details on the webpage


## Features

- Fetch trending movies (real-time)
- Search movies by name
- Movie detail page (dynamic routing)
- Trailer integration (YouTube embed)
- Display rating, popularity, genres, etc


## 📁 Project Structure

    project/
    │
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   └── movie_detail.html
    │
    ├── static/
    │   ├── style.css
    │   └── logo.svg
    │
    └── venv/
