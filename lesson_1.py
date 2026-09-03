"""
✅ Project 1: Favorite Movie List
Practice lists, input, and string basics.

Ask the user for 3 favorite movies.

Save them in a list.

Print:

Full list
First movie
Last movie
Number of movies
👉 Hint: Use len(), list[index].
"""

movieList=[]
for i in range(1,4,1):
    movieList.append(input(f"Favori {i}. Filminizin Adını Girin\n"))

print(f"\nFull list >>> {movieList}")

print("\nFirst movie:", movieList[0])
print("\nLast movie:", movieList[-1])
print("\nNumber of movies:", len(movieList))

 

