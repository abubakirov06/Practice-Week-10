def gradebook_organizer(scores):
    gradebook = {}
    for data in scores:
        if data[0] in gradebook:
            gradebook[data[0]][data[1]] = data[2]
        else:
            #gradebook[data[0]][data[1]] = data[2]
            gradebook[data[0]]= {data[1]:data[2]}
    print()
    for key, value in gradebook.items():
        print(f"{key}: {value}")
    print()

raw_scores = [("Alice", "Math", 85), ("Bob", "Math", 75), ("Alice", "Physics", 90), 
("Charlie", "History", 88), ("Bob", "Physics", 82), ("Alice", "History", 92)]

gradebook_organizer(raw_scores)