import re
from collections import Counter
txt = input("Enter text = ")
with open('sample.txt', 'w') as f:
    f.write(txt)
n = int(input("Top common words = "))
words = re.findall(r"\b\w+\b", txt.lower())
data = f"Word Count Report\nTotal Words: {len(words)}\nTop {n} Words:\n"
print(f"Total words: {len(words)}")
print(f"Top {n} most common words:")
words = Counter(words)
for a, b in words.most_common(n):
    print(f"{a} - {b} times")
    data += f"{a} - {b}\n"
with open("word_count_report.txt", 'w') as f:
    f.write(data)