from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from custom_functions.config import load_config
from custom_functions.web.templates import html_beginning, html_end, html_table_end
import threading

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = generate_html()
        
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        length = self.headers['content-length']
        data = self.rfile.read(int(length))  
        print(length)
        print(data)  
        message = "Saved!"
        self.wfile.write(bytes(message, "utf8"))
        
def generate_html():
    #Load config
    config = load_config()

    #Beginning of HTML file
    html = html_beginning
    for section in config:
        html += f'<h2>{section}</h2>'
        html += f'<form action="" method="POST" id={section}><table border="1"><th>Option</th><th>Value</th></tr>'
        print(section)
        for key in config[section]:
            if key == "webhook":
                value = "****REDACTED****"
            else:
                value = config[section][key]
            if key == "created" or key == "modified" or key == "webhook":
                html += f'<td>{key}</td><td>{value}</td></tr>'    
            else:        
                html += f'<td>{key}</td><td><input type="text" name="{section + "_" + key}" value="{value}" form={section}</td></tr>'
            print(key)
            print(value)
        html += html_table_end
    html += html_end
    print(html)
    #Save HTML
    f = open("custom_functions/web/index.html", "w")
    f.write(html)
    f.close
    return html

def start_server(host, port):
    #Setup threading for HTML server
    httpd = ThreadingHTTPServer((host, int(port)),handler)
    server_thread = threading.Thread(target=httpd.serve_forever)

    #Allow daemon
    server_thread.daemon = True

    #Generate html
    generate_html()

    #Finally start server
    server_thread.start()

    print(f"Web server started! Available at {host}:{port}")