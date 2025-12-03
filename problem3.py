movies = {
    "Inception": ["Sci-Fi", "Action"], "The Matrix": ["Sci-Fi", "Action"],
    "Shrek": ["Animation", "Comedy"], "Toy Story": ["Animation", "Family"],
    "Interstellar": ["Sci-Fi", "Drama"]}
def genre_indexer(movies):
    genre_index = {}
    for title, genre in movies.items():
        if genre[0] in genre_index:
            genre_index[genre[0]].append(title)
        elif not genre[0] in genre_index:
            genre_index[genre[0]] = [title]
        if genre[1] in genre_index:
            genre_index[genre[1]].append(title)
        elif not genre[1] in genre_index:
            genre_index[genre[1]] = [title]
    organizer = []
    for genre1, titles in genre_index.items():
        organizer.append([genre1, titles])
    organizer.sort()
    print('\n{', end = '')
    for element in organizer:
        if not element == organizer[-1]:
            print(f"'{element[0]}':{element[1]}")
        else:
            print(f"'{element[0]}':{element[1]}", end = '')

    print('}\n')
genre_indexer(movies)
