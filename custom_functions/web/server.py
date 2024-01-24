from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from custom_functions.config import get_section, get_value, get_key, save_config
from custom_functions.web.templates import html_beginning, html_end, html_table_end, html_table_start
import threading, mimetypes


class handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        # Parse the URL
        parsed_url = urlparse(self.path)

        # Extract query parameters
        query_params = parse_qs(parsed_url.query)

        # Get values from the query parameters
        section = query_params.get('section', [None])[0]
        key = query_params.get('key', [None])[0]
        print(key)
        value = query_params.get('value', [None])[0]

        if section != None and key != None and value != None:
            save_config(section, key, value)
        generate_html(section, key)
        # Override the default behavior to serve my custom HTML file
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()
    
    def parse_get_params(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        self.get_params = params

def save_html(file, html):
    #Save HTML
    html += html_end
    f = open(file, "w")
    f.write(html)
    f.close

def generate_html(section=None, key=None):
    #Beginning of HTML file
    html = html_beginning

    #Generate HTML for sections
    if section == None:
        list_of_sections = get_section().split("\n")
        number_of_sections = len(list_of_sections)

        html += '<h1 class="title">List of sections</h1><br>'

        for section in range(1, number_of_sections - 1):
            destination = list_of_sections[section]
            html += f'<a href=keys.html?section={destination}><button class="btn">{destination}</button></a><br>'
        save_html("index.html", html)
        print(list_of_sections)

    #Generate HTML for keys
    elif section != None and key == None:
        html += f'<h1 class="title">Keys in {section}</h1><br>'
        list_of_keys = get_key(section).split("\n")
        number_of_keys = len(list_of_keys)

        for key_number in range(1, number_of_keys - 1):
            print(key_number)
            destination = list_of_keys[key_number]
            print(destination)
            html += f'<a href=value.html?section={section}&key={destination}><button class="btn">{destination}</button></a><br>'
        save_html("keys.html", html)


    elif section == "General" and key == "webhook":
        html += f'<h1 class="error"> Discord webhook CAN NOT be changed via web'
        save_html("value.html", html)

    #Generate HTML for value
    elif section != None and key != None:
        value = get_value(section, key)

        html += f'<h+ class="title">Changing value: {value} in {key}'
        html += f'<form action=modify.html?section={section}&key={key}>'
        html += '<label for="value"> Modify value to: </label>'
        html += f'<input type="text" id="value" value="{value}"'
        html += '<input type="submit" value="CHANGE IT!"></form>'

        save_html("value.html", html)

            
   # elif section != None and key != None:
    #    html += f'<h1 class="title"> Value in {key}</h1><br>'
     #   old_value = get_value(section, key)
      #  destination = list_of_keys[key]
       # html += f'<a href=index.html?section={section}&?key={destination}><form action="index.html?section={section}&?key={destination}&?value="{old_value}"> <input type="text" id="new_value" value="{old_value}"><input type="submit" value="Submit"></a><br>'
            
            #html += html_table_start
            #value = get_value(section, key)
            #html += f'<td>{key}</td><td>{value}</td></tr>'
        #html += html_table_end    




        


""" def generate_html():
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
    f = open("index.html", "w")
    f.write(html)
    f.close
    return html """

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