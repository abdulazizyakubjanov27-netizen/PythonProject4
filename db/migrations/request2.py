from handlers.home import home_handler
from handlers.create_post import create_post_handler
from handlers.search import search_handler
from handlers.not_found import not_found_handler

def parse_request(request):
    lines = request.split("\r\n")
    method, path, _ = lines[0].split()

    body = ""
    if "\r\n\r\n" in request:
        body = request.split("\r\n\r\n")[1]

    return method, path, body


def handle_request(request):
    method, path, body = parse_request(request)

    if path == "/" and method == "GET":
        return home_handler()

    elif path == "/create" and method == "POST":
        return create_post_handler(body)

    elif path.startswith("/search") and method == "GET":
        return search_handler(path)

    else:
        return not_found_handler()