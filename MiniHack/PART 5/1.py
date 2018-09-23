import webbrowser

move = {
    "title": "Infinity War",
    "release_year": 2018,
    "imdb_rating": 8.6,
    "trailer": "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
}
print("*"*15)
for key, value in move.items():
    print("*", key, value)
print("*"*15)
print("*"*15)

print("*", "imdb_rating:",move["imdb_rating"])
print("*"*15)
move["title"] = move["title"].upper()
webbrowser.open(move["trailer"])