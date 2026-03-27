import re

html = """
<html>
<body>
<a href="https://example.com">Example</a>
<a href="https://python.org">Python</a>
</body>
</html>
"""

links = re.findall(r'href="(.*?)"', html)

for link in links:
    print(link)