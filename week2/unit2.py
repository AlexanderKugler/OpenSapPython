# Week 2, Unit 2: Exercise (Python_1)
# Below you find a code snippet to create a Python list containing the titles of
# all Star Wars movies. The list contains:

# A list containing the titles of the prequel trilogy: The Phantom Menace, Attack of the Clones, Revenge of the Sith
# A list containing the titles of the original trilogy: A New Hope, The Empire Strikes Back, Return of the Jedi,
# A list containing the titles of the sequel trilogy: The Force Awakens, The Last Jedi, The Rise of Skywalker

star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

trilogy = int(input("Which Trilogy?"))
movie = int(input("Which Movie"))

if __name__ == '__main__':
    print(star_wars_movies[trilogy - 1][movie - 1])
