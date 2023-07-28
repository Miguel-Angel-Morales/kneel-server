import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import get_all_metals, get_single_metal, create_metal, delete_metal, update_metal
from views import get_all_orders, get_single_order, create_order, delete_order, update_order
from views import get_all_sizes, get_single_size, create_size, delete_size, update_size
from views import get_all_styles, get_single_style, create_style, delete_style, update_style


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass

        return (resource, pk)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        """Handles GET requests to the server"""
        self._set_headers(200)

        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)
            else:
                response = get_all_metals()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)
            else:
                response = get_all_orders()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)
            else:
                response = get_all_sizes()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)
            else:
                response = get_all_styles()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_resource = None

        if resource == "metals":
            if "metal" in post_body:
                new_resource = create_metal(post_body)
            else:
                self._set_headers(400)
                new_resource = {
                    "message" f'{"metal is required" if "metal" not in post_body else ""}'
                }

        if resource == "orders":
            if "style_id" in post_body and "metal_id" in post_body and "size_id" in post_body:
                new_resource = create_order(post_body)
            else:
                self._set_headers(400)
                new_resource = {
                    "message": f'{"style_id is required" if "style_id" not in post_body else ""} {"metal_id is required" if "metal_id" not in post_body else ""} {"size_id is required" if "size_id" not in post_body else ""}'
                }

        if resource == "sizes":
            if "carets" in post_body:
                new_resource = create_size(post_body)
            else:
                self._set_headers(400)
                new_resource = {
                    "message": f'{"carets is required" if "carets" not in post_body else ""}'
                }

        if resource == "styles":
            if "style" in post_body:
                new_resource = create_size(post_body)
            else:
                self._set_headers(400)
                new_resource = { 
                    "message": f'{"style is required" if "style" not in post_body else ""}'
                }

        self.wfile.write(json.dumps(new_resource).encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "metals":
            success = update_metal(id, post_body)
        elif resource == "orders":
            update_order(id, post_body)
        elif resource == "sizes":
            update_size(id, post_body)
        elif resource == "styles":
            update_style(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "metals":
            delete_metal(id)

        if resource == "orders":
            delete_order(id)

        if resource == "sizes":
            delete_size(id)

        if resource == "styles":
            delete_style(id)

        # Encode the new animal and send in response
        self.wfile.write(json.dumps(resource).encode())

# This function is not inside the class. It is the starting
# point of this application.


# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
