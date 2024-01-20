from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from custom_functions.config import load_config
from custom_functions.web.templates import html_beginning, html_end
import threading

class HTMLHandler(SimpleHTTPRequestHandler):
    # Override the default behavior to serve my custom HTML file
    def do_GET(self):
        generate_html()
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def generate_html():
    #Load config
    config = load_config()

    #Beginning of HTML file
    html = html_beginning
    for section in config:
        html += f'<h2>{section}</h2>'
        html += f'<table border="1"><th>Option</th><th>Value</th></tr>'
        print(section)
        for key in config[section]:
            if key == "webhook":
                value = "****REDACTED****"
            else:
                value = config[section][key]
            html += f'<td>{key}</td><td><input type="text" name="{section + "_" + key + "_" + value}" value="{value}"</td></tr>'
            print(key)
            print(value)
        html += '</table>'
    html += html_end
    print(html)
    #Save HTML
    f = open("index.html", "w")
    f.write(html)
    f.close

def start_server(host, port):
    #Setup threading for HTML server
    httpd = ThreadingHTTPServer((host, int(port)),HTMLHandler)
    server_thread = threading.Thread(target=httpd.serve_forever)

    #Allow daemon
    server_thread.daemon = True

    #Generate html
    generate_html()

    #Finally start server
    server_thread.start()

    print(f"Web server started! Available at {host}:{port}")