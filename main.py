import requests

from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
movies_titles = []
response = requests.get(URL).text

soup = BeautifulSoup(response,  "html.parser")
titles = soup.find_all(name="h3", class_="title")


for movie in titles:
    title = movie.getText()
    movies_titles.append(title)

movies = movies_titles[::-1]
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

