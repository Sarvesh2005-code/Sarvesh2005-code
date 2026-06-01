import urllib.request
import json
from http.server import BaseHTTPRequestHandler

def get_github_stats(username):
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            return {
                "repos": data.get("public_repos", 0), 
                "followers": data.get("followers", 0),
                "stars": "342",        
                "commits": "2,116",    
                "loc": "446,276",      
                "status": "Online"
            }
    except Exception:
        return {"repos": "?", "followers": "?", "stars": "?", "commits": "?", "loc": "?", "status": "API Limit"}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        stats = get_github_stats("Sarvesh2005-code")
        
        w3_namespace = "http://" + "www.w3.org/2000/svg"
        my_website = "https://" + "sarvy.vercel.app/"

        svg_content = f"""
        <svg width="1400" height="850" xmlns="{w3_namespace}">
          <style>
            .text {{
                font-family: 'Courier New', Courier, monospace;
                font-size: 20px;
                font-weight: bold;
                fill: #C9D1D9;
            }}
            .ascii {{
                font-family: 'Courier New', Courier, monospace;
                font-size: 18px;
                fill: #F0F6FC;
            }}
            .blue {{ fill: #58A6FF; }}
            .green {{ fill: #7EE787; }}
            .orange {{ fill: #E3B341; }}
            .grey {{ fill: #8B949E; }}
          </style>
          <rect width="1400" height="850" rx="10" fill="#161B22" stroke="#30363D" stroke-width="1"/>
          
          <image
              href="https://raw.githubusercontent.com/Sarves2005-code/Sarves2005-code/main/profile.png"
              x="20"
              y="20"
              width="620"
              height="780"
          />

          <text x="700" y="80" class="text" xml:space="preserve"><tspan class="blue">Sarvesh</tspan>@<tspan class="blue">Developer</tspan> <tspan class="grey">----------------------------------</tspan></text>
          
          <text x="700" y="130" class="text" xml:space="preserve">. <tspan class="orange">OS:</tspan> ........................... <tspan class="blue">Windows 11, Kali Linux</tspan></text>
          <text x="700" y="160" class="text" xml:space="preserve">. <tspan class="orange">Uptime:</tspan> ..................................... <tspan class="blue">20 years</tspan></text>
          <text x="700" y="190" class="text" xml:space="preserve">. <tspan class="orange">IDE:</tspan> ................................ <tspan class="blue">Eclipse, VS Code</tspan></text>
          
          <text x="700" y="250" class="text" xml:space="preserve">. <tspan class="orange">Languages.Programming:</tspan> .......................... <tspan class="blue">Java</tspan></text>
          <text x="700" y="280" class="text" xml:space="preserve">. <tspan class="orange">Languages.Computer:</tspan> ........ <tspan class="blue">HTML, CSS, JS, SQL, JSON</tspan></text>
          
          <text x="700" y="340" class="text" xml:space="preserve">. <tspan class="orange">Hobbies.Software:</tspan> ..... <tspan class="blue">Backend Architecture, Spring Boot</tspan></text>
          <text x="700" y="370" class="text" xml:space="preserve">. <tspan class="orange">Hobbies.Security:</tspan> ......... <tspan class="blue">NIST Frameworks, Custom Firewalls</tspan></text>

          <text x="700" y="440" class="text" xml:space="preserve"><tspan class="grey">- Contact --------------------------------------------</tspan></text>
          <text x="700" y="490" class="text" xml:space="preserve">. <tspan class="orange">Email:</tspan> ...................... <tspan class="blue">sarveshnakhale21@gmail.com</tspan></text>
          <text x="700" y="525" class="text" xml:space="preserve">. <tspan class="orange">Website:</tspan> ....................... <tspan class="blue">{my_website}</tspan></text>
          <text x="700" y="560" class="text" xml:space="preserve">. <tspan class="orange">LinkedIn:</tspan> .............................. <tspan class="blue">in/sarveshnakhale</tspan></text>
          <text x="700" y="595" class="text" xml:space="preserve">. <tspan class="orange">X:</tspan> ........................................... <tspan class="blue">@Sarvyx2005</tspan></text>
          <text x="700" y="630" class="text" xml:space="preserve">. <tspan class="orange">Discord:</tspan> ....................................... <tspan class="blue">@sarvy123</tspan></text>

          <text x="700" y="710" class="text" xml:space="preserve"><tspan class="grey">- GitHub Stats [{stats['status']}] --------------------------</tspan></text>
          <text x="700" y="750" class="text" xml:space="preserve">. <tspan class="orange">Repos:</tspan> .... <tspan class="green">{stats['repos']}</tspan> | <tspan class="orange">Stars:</tspan> ............. <tspan class="green">{stats['stars']}</tspan></text>
          <text x="700" y="785" class="text" xml:space="preserve">. <tspan class="orange">Commits:</tspan> .. <tspan class="green">{stats['commits']}</tspan> | <tspan class="orange">Followers:</tspan> ......... <tspan class="green">{stats['followers']}</tspan></text>
          <text x="700" y="820" class="text" xml:space="preserve">. <tspan class="orange">Lines of Code on GitHub:</tspan> ................... <tspan class="green">{stats['loc']}</tspan></text>
        </svg>
        """

        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.send_header('Cache-Control', 's-maxage=3600, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(svg_content.encode('utf-8'))
