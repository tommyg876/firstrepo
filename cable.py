grades = [
    ('Alice', 'Math', 85),
    ('Bob', 'Math', 92),
    ('Alice', 'English', 78),
]

def store_grades (grades):
    d = {}
    for name, subject, score in grades:
        d[(subject,name)] = score
    return d

print(store_grades(grades))