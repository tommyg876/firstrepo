positions = {
    (2,3): "Alice",
    (5,1): "Bob",
    (0,0): "Spawn"
}

positions [(1,2)] = "Alpha"
positions [(1.0,2.0)] = "Beta"

print (positions)

for key, value in positions.items():
    print (key[1])