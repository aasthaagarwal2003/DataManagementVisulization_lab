import matplotlib.pyplot as plt


movies = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
box_office = [150, 200, 120, 300, 250]   # in millions
ratings = [7.5, 8.2, 6.8, 9.0, 8.5]


plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.bar(movies, box_office, color="skyblue")
plt.title("Box Office Collection")
plt.xlabel("Movies")
plt.ylabel("Collection (in millions)")
plt.xticks(rotation=45)


plt.subplot(1, 2, 2)
plt.scatter(movies, ratings, color="red", s=100)
plt.title("Movie Ratings")
plt.xlabel("Movies")
plt.ylabel("Ratings")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
