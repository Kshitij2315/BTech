# Friend Suggestion Algorithm in Python

# Friend graph
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3],
    5: [3]
}

user = int(input("Enter the user between 1-5: "))

friends = graph[user]
suggest = {}

for f in friends:
    for person in graph[f]:
        if person != user and person not in friends:
            if person in suggest:
                suggest[person] += 1
            else:
                suggest[person] = 1

# Sort by mutual friends (descending), then user ID
result = sorted(suggest.items(), key=lambda x: (-x[1], x[0]))

print("Suggested Friends:")
for person, count in result:
    print(person, "Mutual Friends:", count)