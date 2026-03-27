from db.connection import get_connection
import urllib.parse
from handlers.not_found import not_found_handler

def search_handler(path):
    query = urllib.parse.urlparse(path).query
    params = urllib.parse.parse_qs(query)

    keyword = params.get("q", [""])[0]

    conn = get_connection()
    cursor = conn.cursor()

    results = cursor.execute(
        "SELECT * FROM vlogs WHERE title LIKE ?",
        (f"%{keyword}%",)
    ).fetchall()

    if not results:
        return not_found_handler()

    items = ""
    for r in results:
        items += f"<p>{r['title']} - {r['description']}</p>"

    html = f"""
    <h1>Search results</h1>
    {items}
    <a href="/">Back</a>
    """

    response = f"""HTTP/1.1 200 OK
Content-Type: text/html

{html}
"""
    return response.encode()


