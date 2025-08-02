
from flask import Flask, render_template, request, redirect
from samfaa_fetcher import fetch_movies
import pyodbc

app = Flask(__name__)

# Replace with your actual SQL Server config
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=CinemaDB;"
    "Trusted_Connection=yes;"
)

@app.route('/')
def index():
    movies = fetch_movies()
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie_page(movie_id):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Movies WHERE id = ?", movie_id)
    movie = cursor.fetchone()
    cursor.execute("SELECT * FROM Comments WHERE movie_id = ? ORDER BY created_at DESC", movie_id)
    comments = cursor.fetchall()
    return render_template('movie.html', movie=movie, comments=comments)

@app.route('/comment', methods=['POST'])
def comment():
    movie_id = request.form['movie_id']
    name = request.form['name']
    text = request.form['text']
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Comments (movie_id, name, text) VALUES (?, ?, ?)", movie_id, name, text)
    conn.commit()
    return redirect(f'/movie/{movie_id}')

if __name__ == '__main__':
    app.run(debug=True)
