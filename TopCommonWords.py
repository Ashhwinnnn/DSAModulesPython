from collections import Counter
import re
text = """python is an easy programmers language.
python syntax is like the English Language
Python language is easy to learn and adapt to compared with java and C.
In python language, the same task can be performed using fewer lines code.
Its easy learning and easy to code."""

words=re.findall('\w+',text)
count= Counter(words)

# ...existing code...
print(count.most_common(3))
# ...existing code...