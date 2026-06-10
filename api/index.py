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
        with urllib.request.urlopen(req_user) as response:
            user_data = json.loads(response.read())
            repos = user_data.get("public_repos", 0)
            followers = user_data.get("followers", 0)
            
        stars = 0
        with urllib.request.urlopen(req_repos) as response:
            repos_data = json.loads(response.read())
            for repo in repos_data:
                stars += repo.get("stargazers_count", 0)
                
        return {"repos": str(repos), "followers": str(followers), "stars": str(stars)}
    except Exception:
        return {"repos": "15", "followers": "9", "stars": "342"}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        stats = get_github_stats("Sarvesh2005-code")
        w3_namespace = "http://www.w3.org/2000/svg"
        
        base64_image_data = ""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "base64.txt")
            with open(file_path, "r", encoding="utf-8") as f:
                base64_image_data = f.read().strip()
        except Exception:
            pass # Fails gracefully if image is missing

        svg_content = f"""
        <svg width="1200" height="900" xmlns="{w3_namespace}">
          <defs>
            <filter id="orb-blur" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="100"/>
            </filter>
            
            <linearGradient id="glass-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="rgba(255, 255, 255, 0.12)"/>
              <stop offset="100%" stop-color="rgba(255, 255, 255, 0.03)"/>
            </linearGradient>
            
            <clipPath id="avatar-clip">
              <circle cx="1000" cy="180" r="110" />
            </clipPath>
          </defs>

          <rect width="1200" height="900" fill="#0D1117"/>
          
          <circle cx="200" cy="200" r="300" fill="#4B0082" filter="url(#orb-blur)" opacity="0.6"/>
          <circle cx="1000" cy="800" r="350" fill="#0047AB" filter="url(#orb-blur)" opacity="0.5"/>
          <circle cx="600" cy="450" r="250" fill="#8B4500" filter="url(#orb-blur)" opacity="0.4"/>

          <rect x="40" y="40" width="1120" height="820" rx="30" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>

          <style>
            .title {{ font-family: 'Segoe UI', Helvetica, sans-serif; font-size: 52px; font-weight: 800; fill: #FFFFFF; }}
            .subtitle {{ font-family: 'Segoe UI', Helvetica, sans-serif; font-size: 26px; font-weight: 600; fill: #58A6FF; }}
            .text {{ font-family: 'Segoe UI', Helvetica, sans-serif; font-size: 18px; fill: #C9D1D9; }}
            .text-sm {{ font-family: 'Segoe UI', Helvetica, sans-serif; font-size: 14px; fill: #8B949E; }}
            .bold {{ font-weight: bold; fill: #FFFFFF; }}
            .badge-text {{ font-family: 'Segoe UI', Helvetica, sans-serif; font-size: 15px; font-weight: 600; fill: #FFFFFF; }}
          </style>

          <text x="90" y="130" class="title">Hi, I'm Sarvesh Nakhale 👋</text>
          
          <rect x="90" y="160" width="220" height="36" rx="18" fill="rgba(88, 166, 255, 0.15)" stroke="rgba(88, 166, 255, 0.4)" stroke-width="1"/>
          <circle cx="110" cy="178" r="5" fill="#58A6FF"/>
          <text x="125" y="184" class="badge-text" fill="#58A6FF">Software Developer</text>

          <text x="90" y="240" class="text">I build clean, functional backend systems and applications</text>
          <text x="90" y="270" class="text">that solve real-world problems.</text>

          <rect x="520" y="160" width="300" height="110" rx="15" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="540" y="190" class="text-sm">📍 Maharashtra, India</text>
          <text x="540" y="220" class="text-sm">✉️ sarveshnakhale21@gmail.com</text>
          <text x="540" y="250" class="text-sm">🟢 Available for new opportunities</text>

          <circle cx="1000" cy="180" r="115" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="4"/>
          <image href="{base64_image_data}" x="850" y="30" width="300" height="300" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />

          <rect x="90" y="330" width="235" height="100" rx="16" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="110" y="375" class="title" font-size="36">20<tspan font-size="24" fill="#58A6FF">yrs</tspan></text>
          <text x="110" y="405" class="text-sm">System Uptime</text>

          <rect x="345" y="330" width="235" height="100" rx="16" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="365" y="375" class="title" font-size="36">{stats['repos']}</text>
          <text x="365" y="405" class="text-sm">Public Repositories</text>

          <rect x="600" y="330" width="235" height="100" rx="16" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="620" y="375" class="title" font-size="36">{stats['stars']}</text>
          <text x="620" y="405" class="text-sm">Total Stars</text>

          <rect x="855" y="330" width="235" height="100" rx="16" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="875" y="375" class="title" font-size="36">{stats['followers']}</text>
          <text x="875" y="405" class="text-sm">Followers</text>

          <rect x="90" y="460" width="490" height="200" rx="20" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="120" y="505" class="subtitle" font-size="22">👤 About Me</text>
          <text x="120" y="545" class="text" font-size="16">I am a software developer passionate about finding</text>
          <text x="120" y="570" class="text" font-size="16">real-world use cases for technology and mathematics.</text>
          <text x="120" y="595" class="text" font-size="16">I enjoy integrating complex ideas into unified,</text>
          <text x="120" y="620" class="text" font-size="16">functional solutions to build things that stand out.</text>

          <rect x="600" y="460" width="490" height="200" rx="20" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="630" y="505" class="subtitle" font-size="22">⚙️ Tech Stack</text>
          <text x="630" y="550" class="text">Backend: <tspan class="bold">Java, Spring Boot, SQL</tspan></text>
          <text x="630" y="585" class="text">Frontend: <tspan class="bold">HTML, CSS, JS, JSON</tspan></text>
          <text x="630" y="620" class="text">Security/OS: <tspan class="bold">Kali Linux, Custom Firewalls</tspan></text>

          <rect x="90" y="690" width="490" height="140" rx="16" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="120" y="730" class="bold" font-size="20">🌐 Distributed Compute Node</text>
          <text x="120" y="760" class="text-sm">A distributed architecture project focused on solving</text>
          <text x="120" y="780" class="text-sm">complex mathematical computations across nodes.</text>
          <text x="120" y="810" class="text-sm" fill="#58A6FF">Java • Spring Boot</text>

          <rect x="600" y="690" width="490" height="140" rx="16" fill="url(#glass-gradient)" stroke="rgba(255,255,255,0.1)"/>
          <text x="630" y="730" class="bold" font-size="20">🛡️ SecureNet Configurator</text>
          <text x="630" y="760" class="text-sm">A custom network firewall configuration system</text>
          <text x="630" y="780" class="text-sm">based heavily on NIST security frameworks.</text>
          <text x="630" y="810" class="text-sm" fill="#58A6FF">Kali Linux • Custom Firewalls • JSON</text>

        </svg>
        """

        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.send_header('Cache-Control', 's-maxage=3600, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(svg_content.encode('utf-8'))
