def reconstructQueue(people: [[]]):
    print(people)
    people.sort(key=lambda x: (-x[0], x[0]))
    print(people)
reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])