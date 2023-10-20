def word_merger(a,b):
    added = ""
    for i in range(min(len(a),len(b))):
        added += a[i]+b[i]
    return added
print(word_merger("hello", "world"))