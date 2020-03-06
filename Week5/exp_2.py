counts = dict()
names = ['mustafa', 'ayşe', 'mustafa', 'mehmet', 'ayşe']
for name in names :
    counts[name] = counts.get(name,0) + 1
print(counts)
