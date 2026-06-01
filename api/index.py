import urllib.request
import json
from http.server import BaseHTTPRequestHandler

def get_github_stats(username):
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            # Basic API fetch. Advanced stats (Commits, LoC) are hardcoded placeholders 
            # below as they require complex GraphQL queries to calculate dynamically.
            return {
                "repos": data.get("public_repos", 0), 
                "followers": data.get("followers", 0),
                "stars": "342",        # Placeholder
                "commits": "2,116",    # Placeholder
                "loc": "446,276",      # Placeholder
                "status": "Online"
            }
    except Exception:
        return {"repos": "?", "followers": "?", "stars": "?", "commits": "?", "loc": "?", "status": "API Limit"}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        stats = get_github_stats("Sarvesh2005-code")
        
        # Split URLs to prevent rich-text editors from auto-formatting them
        w3_namespace = "http://" + "www.w3.org/2000/svg"
        my_website = "https://" + "sarvy.vercel.app/"
        
        # 35-Character Spooky Specter (Adapted from your Braille Ghost)
        ascii_art_lines = [
            r"                                   ",
            r"            .---.---.              ",
            r"          .'         '.            ",
            r"         /             \           ",
            r"        /               \          ",
            r"       |                 |         ",
            r"       |  .---.   .---.  |         ",
            r"       | /     \ /     \ |         ",
            r"       | \  0  / \  0  / |         ",
            r"       |  '---'   '---'  |         ",
            r"       |                 |         ",
            r"       |                 |         ",
            r"       |                 |         ",
            r"       |                 |         ",
            r"       |                 |         ",
            r"       \      .---.      /         ",
            r"        \    /     \    /          ",
            r"         '-.'       '.-'           ",
            r"           /         \             ",
            r"         .'           '.           ",
            r"        /               \          ",
            r"       |                 |         ",
            r"       '~^~^~^~^~^~^~^~^~'         ",
            r"                                   ",
            r"                                   "
        ]

        tspan_blocks = ""
        y_pos = 70  
        for line in ascii_art_lines:
            clean_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            tspan_blocks += f'<tspan x="30" y="{y_pos}">{clean_line}</tspan>\n          '
            y_pos += 15  

        svg_content = f"""
        <svg width="900" height="520" xmlns="{w3_namespace}">
          <style>
            .text {{ font-family: 'Courier New', Courier, monospace; font-size: 14px; fill: #C9D1D9; }}
            .ascii {{ font-family: 'Courier New', Courier, monospace; font-size: 12px; fill: #F0F6FC; }} /* White Ghost */
            .blue {{ fill: #58A6FF; }}
            .green {{ fill: #7EE787; }}
            .lightblue {{ fill: #79C0FF; }} /* Updated description color */
            .grey {{ fill: #8B949E; }}
          </style>
          <rect width="900" height="520" rx="10" fill="#161B22" stroke="#30363D" stroke-width="1"/>
          
          <text class="ascii" xml:space="preserve">
          {tspan_blocks}
          </text>

          <text x="350" y="70" class="text" xml:space="preserve"><tspan class="blue">Sarvesh</tspan>@<tspan class="blue">Developer</tspan> <tspan class="grey">----------------------------------</tspan></text>
          
          <text x="350" y="105" class="text" xml:space="preserve">. <tspan class="lightblue">OS:</tspan> ........................... Windows 11, Kali Linux</text>
          <text x="350" y="125" class="text" xml:space="preserve">. <tspan class="lightblue">Uptime:</tspan> ..................................... 20 years</text>
          <text x="350" y="145" class="text" xml:space="preserve">. <tspan class="lightblue">IDE:</tspan> ................................ Eclipse, VS Code</text>
          
          <text x="350" y="185" class="text" xml:space="preserve">. <tspan class="lightblue">Languages.Programming:</tspan> .......................... Java</text>
          <text x="350" y="205" class="text" xml:space="preserve">. <tspan class="lightblue">Languages.Computer:</tspan> ........ HTML, CSS, JS, SQL, JSON</text>
          
          <text x="350" y="245" class="text" xml:space="preserve">. <tspan class="lightblue">Hobbies.Software:</tspan> ..... Backend Architecture, Spring Boot</text>
          <text x="350" y="265" class="text" xml:space="preserve">. <tspan class="lightblue">Hobbies.Security:</tspan> ......... NIST Frameworks, Custom Firewalls</text>

          <text x="350" y="310" class="text" xml:space="preserve"><tspan class="grey">- Contact --------------------------------------------</tspan></text>
          <text x="350" y="340" class="text" xml:space="preserve">. <tspan class="lightblue">Email:</tspan> ...................... sarveshnakhale21@gmail.com</text>
          <text x="350" y="360" class="text" xml:space="preserve">. <tspan class="lightblue">Website:</tspan> ....................... {my_website}</text>
          <text x="350" y="380" class="text" xml:space="preserve">. <tspan class="lightblue">LinkedIn:</tspan> .............................. in/sarveshnakhale</text>
          <text x="350" y="400" class="text" xml:space="preserve">. <tspan class="lightblue">X:</tspan> ........................................... @Sarvyx2005</text>
          <text x="350" y="420" class="text" xml:space="preserve">. <tspan class="lightblue">Discord:</tspan> ....................................... @sarvy123</text>

          <text x="350" y="460" class="text" xml:space="preserve"><tspan class="grey">- GitHub Stats [{stats['status']}] --------------------------</tspan></text>
          <text x="350" y="485" class="text" xml:space="preserve">. <tspan class="lightblue">Repos:</tspan> .... <tspan class="green">{stats['repos']}</tspan> | <tspan class="lightblue">Stars:</tspan> ............. <tspan class="green">{stats['stars']}</tspan></text>
          <text x="350" y="505" class="text" xml:space="preserve">. <tspan class="lightblue">Commits:</tspan> .. <tspan class="green">{stats['commits']}</tspan> | <tspan class="lightblue">Followers:</tspan> ......... <tspan class="green">{stats['followers']}</tspan></text>
          <text x="350" y="525" class="text" xml:space="preserve">. <tspan class="lightblue">Lines of Code on GitHub:</tspan> ................... <tspan class="green">{stats['loc']}</tspan></text>
        </svg>
        """

        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.send_header('Cache-Control', 's-maxage=3600, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(svg_content.encode('utf-8'))
