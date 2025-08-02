
import requests

def fetch_movies():
    url = "https://api.samfaa.ir/admin/report/recent_shows?recently=all&province_id=&screening_id=1404&from=&to="
    response = requests.get(url)
    data = response.json().get("data", [])
    movies = []
    for m in data:
        movies.append({
            "id": m.get("id"),
            "title": m.get("title"),
            "image_url": m.get("image_url"),
            "distribution_title": m.get("distribution_title", "ناشناخته"),
            "director": m.get("director")[0] if m.get("director") else "ناشناخته",
            "start_date": m.get("start_date", "")
        })
    return movies
