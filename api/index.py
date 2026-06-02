import urllib.request
import json
import os
from http.server import BaseHTTPRequestHandler

def get_github_stats(username):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
    
    req_user = urllib.request.Request(user_url, headers={'User-Agent': 'Mozilla/5.0'})
    req_repos = urllib.request.Request(repos_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        # Fetch dynamic Repos and Followers
        with urllib.request.urlopen(req_user) as response:
            user_data = json.loads(response.read())
            repos = user_data.get("public_repos", 0)
            followers = user_data.get("followers", 0)
            
        # Fetch dynamic Stars by iterating through all public repos
        stars = 0
        with urllib.request.urlopen(req_repos) as response:
            repos_data = json.loads(response.read())
            for repo in repos_data:
                stars += repo.get("stargazers_count", 0)
                
        return {
            "repos": str(repos), 
            "followers": str(followers),
            "stars": str(stars),        
            "commits": "Token Req.",    
            "loc": "Token Req.",      
            "status": "Online"
        }
    except Exception:
        return {"repos": "?", "followers": "?", "stars": "?", "commits": "?", "loc": "?", "status": "API Limit"}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        stats = get_github_stats("Sarvesh2005-code")
        
        w3_namespace = "http://" + "www.w3.org/2000/svg"
        my_website = "https://" + "sarvy.vercel.app/"

        # Automatically read the transparent base64 string from your txt file
        base64_image_data = ""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "base64.txt")
            with open(file_path, "r", encoding="utf-8") as f:
                base64_image_data = f.read().strip()
        except Exception as e:
            print(f"Could not read base64.txt: {e}")

        svg_content = f"""
        <svg width="1550" height="850" xmlns="{w3_namespace}">
          <style>
            .text {{
                font-family: 'Courier New', Courier, monospace;
                font-size: 22px; /* Increased from 20px to 22px */
                font-weight: bold;
                fill: #C9D1D9;
            }}
            .blue {{ fill: #58A6FF; }}
            .green {{ fill: #7EE787; }}
            .orange {{ fill: #E3B341; }}
            .grey {{ fill: #8B949E; }}
          </style>
          <rect width="1550" height="850" rx="10" fill="#161B22" stroke="#30363D" stroke-width="1"/>
          
          <image
              href="{base64_image_data}"
              x="20"
              y="20"
              width="620"
              height="780"
          />

          <text x="660" y="80" class="text" xml:space="preserve"><tspan class="blue">Sarvesh</tspan>@<tspan class="blue">Developer</tspan> <tspan class="grey">----------------------------------</tspan></text>
          
          <text x="660" y="130" class="text" xml:space="preserve">. <tspan class="orange">OS:</tspan> ........................... <tspan class="blue">Windows 11, Kali Linux</tspan></text>
          <text x="660" y="160" class="text" xml:space="preserve">. <tspan class="orange">Uptime:</tspan> ..................................... <tspan class="blue">20 years</tspan></text>
          <text x="660" y="190" class="text" xml:space="preserve">. <tspan class="orange">IDE:</tspan> ................................ <tspan class="blue">Eclipse, VS Code</tspan></text>
          
          <text x="660" y="250" class="text" xml:space="preserve">. <tspan class="orange">Languages.Programming:</tspan> .......................... <tspan class="blue">Java</tspan></text>
          <text x="660" y="280" class="text" xml:space="preserve">. <tspan class="orange">Languages.Computer:</tspan> ........ <tspan class="blue">HTML, CSS, JS, SQL, JSON</tspan></text>
          
          <text x="660" y="340" class="text" xml:space="preserve">. <tspan class="orange">Hobbies.Software:</tspan> ..... <tspan class="blue">Backend Architecture, Spring Boot</tspan></text>
          <text x="660" y="370" class="text" xml:space="preserve">. <tspan class="orange">Hobbies.Security:</tspan> ......... <tspan class="blue">NIST Frameworks, Custom Firewalls</tspan></text>

          <text x="660" y="440" class="text" xml:space="preserve"><tspan class="grey">- Contact --------------------------------------------</tspan></text>
          <text x="660" y="490" class="text" xml:space="preserve">. <tspan class="orange">Email:</tspan> ...................... <tspan class="blue">sarveshnakhale21@gmail.com</tspan></text>
          <text x="660" y="525" class="text" xml:space="preserve">. <tspan class="orange">Website:</tspan> ....................... <tspan class="blue">{my_website}</tspan></text>
          <text x="660" y="560" class="text" xml:space="preserve">. <tspan class="orange">LinkedIn:</tspan> .............................. <tspan class="blue">in/sarveshnakhale</tspan></text>
          <text x="660" y="595" class="text" xml:space="preserve">. <tspan class="orange">X:</tspan> ........................................... <tspan class="blue">@Sarvyx2005</tspan></text>
          <text x="660" y="630" class="text" xml:space="preserve">. <tspan class="orange">Discord:</tspan> ....................................... <tspan class="blue">@sarvy123</tspan></text>

          <text x="660" y="710" class="text" xml:space="preserve"><tspan class="grey">- GitHub Stats [{stats['status']}] --------------------------</tspan></text>
          <text x="660" y="750" class="text" xml:space="preserve">. <tspan class="orange">Repos:</tspan> .... <tspan class="green">{stats['repos']}</tspan> | <tspan class="orange">Stars:</tspan> ............. <tspan class="green">{stats['stars']}</tspan></text>
          <text x="660" y="785" class="text" xml:space="preserve">. <tspan class="orange">Commits:</tspan> .. <tspan class="green">{stats['commits']}</tspan> | <tspan class="orange">Followers:</tspan> ......... <tspan class="green">{stats['followers']}</tspan></text>
          <text x="660" y="820" class="text" xml:space="preserve">. <tspan class="orange">Lines of Code on GitHub:</tspan> ................... <tspan class="green">{stats['loc']}</tspan></text>
        </svg>
        """

        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.send_header('Cache-Control', 's-maxage=3600, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(svg_content.encode('utf-8'))
