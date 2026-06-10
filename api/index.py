# Apple Glassmorphism GitHub README Card API

import urllib.request
import json
from http.server import BaseHTTPRequestHandler

def get_github_stats(username):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"

    try:
        req_user = urllib.request.Request(user_url, headers={"User-Agent":"Mozilla/5.0"})
        req_repos = urllib.request.Request(repos_url, headers={"User-Agent":"Mozilla/5.0"})

        with urllib.request.urlopen(req_user) as response:
            user_data = json.loads(response.read())
            repos = user_data.get("public_repos", 0)
            followers = user_data.get("followers", 0)

        stars = 0
        with urllib.request.urlopen(req_repos) as response:
            repos_data = json.loads(response.read())
            for repo in repos_data:
                stars += repo.get("stargazers_count", 0)

        return repos, followers, stars

    except Exception:
        return 15, 9, 342


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        repos, followers, stars = get_github_stats("Sarvesh2005-code")

        svg = f"""<svg width="1000" height="1350" viewBox="0 0 1000 1350" xmlns="http://www.w3.org/2000/svg">
<style>
:root {{
 --bg:#0d1117;
 --card:rgba(255,255,255,.04);
 --card-hover:rgba(255,255,255,.08);
 --stroke:rgba(255,255,255,.12);
 --text:#f8fafc;
 --muted:#9ca3af;
 --accent:#60a5fa;
 --accent-bg:rgba(96,165,250,.15);
}}

@media (prefers-color-scheme: light) {{
 :root {{
 --bg:#f5f7fb;
 --card:rgba(255,255,255,.70);
 --card-hover:rgba(255,255,255,.90);
 --stroke:rgba(255,255,255,.80);
 --text:#111827;
 --muted:#6b7280;
 --accent:#2563eb;
 --accent-bg:rgba(37,99,235,.15);
 }}
}}

.title {{font:700 48px 'SF Pro Display', -apple-system, sans-serif; fill:var(--text); text-anchor:middle;}}
.subtitle {{font:600 22px 'SF Pro Display', -apple-system, sans-serif; fill:var(--accent); text-anchor:middle;}}
.heading {{font:600 24px 'SF Pro Display', -apple-system, sans-serif; fill:var(--text);}}
.body {{font:400 16px 'SF Pro Text', -apple-system, sans-serif; fill:var(--muted); line-height: 1.5;}}
.body-center {{font:400 16px 'SF Pro Text', -apple-system, sans-serif; fill:var(--muted); text-anchor:middle;}}
.stat {{font:700 38px 'SF Pro Display', -apple-system, sans-serif; fill:var(--text); text-anchor:middle;}}
.small {{font:500 14px 'SF Pro Text', -apple-system, sans-serif; fill:var(--muted); text-anchor:middle;}}
.chip {{font:600 14px 'SF Pro Text', -apple-system, sans-serif; fill:var(--text);}}
.proj-title {{font:600 20px 'SF Pro Display', -apple-system, sans-serif; fill:var(--text);}}
.proj-desc {{font:400 14px 'SF Pro Text', -apple-system, sans-serif; fill:var(--muted);}}
</style>

<defs>
<filter id="blur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="120"/></filter>
<linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="white" stop-opacity="0.10"/>
<stop offset="100%" stop-color="white" stop-opacity="0.02"/>
</linearGradient>
</defs>

<!-- BACKGROUND -->
<rect width="1000" height="1350" fill="var(--bg)"/>
<circle cx="200" cy="200" r="280" fill="var(--accent)" opacity="0.25" filter="url(#blur)"/>
<circle cx="800" cy="1100" r="320" fill="#8b5cf6" opacity="0.20" filter="url(#blur)"/>

<!-- MAIN CONTAINER -->
<rect x="40" y="40" width="920" height="1270" rx="40" fill="url(#glass)" stroke="var(--stroke)"/>

<!-- HERO SECTION -->
<text x="500" y="140" class="title">Hi, I'm Sarvesh Nakhale</text>
<text x="500" y="180" class="subtitle">Software Developer | Backend Dev</text>

<!-- Contact Chips Row 1 -->
<rect x="230" y="210" width="160" height="36" rx="18" fill="var(--card)" stroke="var(--stroke)"/>
<text x="310" y="233" class="small">📍 Maharashtra, India</text>

<rect x="405" y="210" width="240" height="36" rx="18" fill="var(--card)" stroke="var(--stroke)"/>
<text x="525" y="233" class="small">✉️ sarveshnakhale21@gmail.com</text>

<rect x="660" y="210" width="110" height="36" rx="18" fill="var(--card)" stroke="var(--stroke)"/>
<text x="715" y="233" class="small">🌐 Portfolio</text>

<!-- Contact Chips Row 2 -->
<rect x="375" y="260" width="250" height="36" rx="18" fill="var(--accent-bg)" stroke="var(--stroke)"/>
<circle cx="395" cy="278" r="5" fill="#10b981"/>
<text x="510" y="283" class="small" style="fill:var(--text);">Available for new opportunities</text>

<!-- STATS SECTION -->
<rect x="80" y="340" width="260" height="130" rx="28" fill="var(--card)" stroke="var(--stroke)"/>
<rect x="370" y="340" width="260" height="130" rx="28" fill="var(--card)" stroke="var(--stroke)"/>
<rect x="660" y="340" width="260" height="130" rx="28" fill="var(--card)" stroke="var(--stroke)"/>

<text x="210" y="415" class="stat">{repos}</text>
<text x="210" y="445" class="small">Public Repositories</text>

<text x="500" y="415" class="stat">{stars}</text>
<text x="500" y="445" class="small">Total Stars</text>

<text x="790" y="415" class="stat">{followers}</text>
<text x="790" y="445" class="small">Followers</text>

<!-- ABOUT ME SECTION -->
<rect x="80" y="500" width="840" height="150" rx="28" fill="var(--card)" stroke="var(--stroke)"/>
<text x="120" y="555" class="heading">👤 About Me</text>
<text x="120" y="595" class="body">I build clean, functional backend systems and applications that solve real-world problems.</text>
<text x="120" y="620" class="body">I am passionate about finding practical use cases for technology and mathematics, and I</text>
<text x="120" y="645" class="body">enjoy integrating complex ideas into unified, functional solutions to build things that stand out.</text>

<!-- TECH STACK SECTION -->
<rect x="80" y="680" width="840" height="120" rx="28" fill="var(--card)" stroke="var(--stroke)"/>
<text x="120" y="735" class="heading">⚙️ Tech Stack</text>

<!-- Tech Badges -->
<rect x="290" y="710" width="70" height="36" rx="12" fill="var(--bg)" stroke="var(--stroke)"/><text x="325" y="733" class="small">Java</text>
<rect x="375" y="710" width="110" height="36" rx="12" fill="var(--bg)" stroke="var(--stroke)"/><text x="430" y="733" class="small">Spring Boot</text>
<rect x="500" y="710" width="60" height="36" rx="12" fill="var(--bg)" stroke="var(--stroke)"/><text x="530" y="733" class="small">SQL</text>
<rect x="575" y="710" width="180" height="36" rx="12" fill="var(--bg)" stroke="var(--stroke)"/><text x="665" y="733" class="small">HTML / CSS / JavaScript</text>
<rect x="770" y="710" width="60" height="36" rx="12" fill="var(--bg)" stroke="var(--stroke)"/><text x="800" y="733" class="small">JSON</text>


<!-- FEATURED PROJECTS SECTION -->
<text x="80" y="865" class="heading">📁 Featured Projects</text>

<!-- Project 1 -->
<rect x="80" y="890" width="260" height="200" rx="24" fill="var(--card)" stroke="var(--stroke)"/>
<text x="100" y="930" class="proj-title">subtext</text>
<text x="100" y="960" class="proj-desc">A high-performance, offline</text>
<text x="100" y="980" class="proj-desc">relational database engine</text>
<text x="100" y="1000" class="proj-desc">that mathematically embeds</text>
<text x="100" y="1020" class="proj-desc">SQL data into LSBs of images.</text>
<!-- Stack -->
<rect x="100" y="1040" width="50" height="26" rx="8" fill="var(--accent-bg)"/><text x="125" y="1057" class="small" style="font-size:12px; fill:var(--accent);">Rust</text>
<rect x="160" y="1040" width="45" height="26" rx="8" fill="var(--accent-bg)"/><text x="182" y="1057" class="small" style="font-size:12px; fill:var(--accent);">SQL</text>

<!-- Project 2 -->
<rect x="370" y="890" width="260" height="200" rx="24" fill="var(--card)" stroke="var(--stroke)"/>
<text x="390" y="930" class="proj-title">specter</text>
<text x="390" y="960" class="proj-desc">A zero-cost, parasitic AI</text>
<text x="390" y="980" class="proj-desc">engine that intercepts LLM</text>
<text x="390" y="1000" class="proj-desc">API calls and executes them</text>
<text x="390" y="1020" class="proj-desc">locally on client hardware.</text>
<!-- Stack -->
<rect x="390" y="1040" width="80" height="26" rx="8" fill="var(--accent-bg)"/><text x="430" y="1057" class="small" style="font-size:12px; fill:var(--accent);">TypeScript</text>
<rect x="475" y="1040" width="45" height="26" rx="8" fill="var(--accent-bg)"/><text x="497" y="1057" class="small" style="font-size:12px; fill:var(--accent);">Rust</text>
<rect x="525" y="1040" width="60" height="26" rx="8" fill="var(--accent-bg)"/><text x="555" y="1057" class="small" style="font-size:12px; fill:var(--accent);">WebGPU</text>

<!-- Project 3 -->
<rect x="660" y="890" width="260" height="200" rx="24" fill="var(--card)" stroke="var(--stroke)"/>
<text x="680" y="930" class="proj-title">voidNet</text>
<text x="680" y="960" class="proj-desc">The ICMP Ghost Protocol.</text>
<text x="680" y="980" class="proj-desc">An unstoppable network</text>
<text x="680" y="1000" class="proj-desc">tunnel that disguises</text>
<text x="680" y="1020" class="proj-desc">traffic as standard Pings.</text>
<!-- Stack -->
<rect x="680" y="1040" width="80" height="26" rx="8" fill="var(--accent-bg)"/><text x="720" y="1057" class="small" style="font-size:12px; fill:var(--accent);">TypeScript</text>
<rect x="765" y="1040" width="80" height="26" rx="8" fill="var(--accent-bg)"/><text x="805" y="1057" class="small" style="font-size:12px; fill:var(--accent);">Networking</text>

<!-- LET'S CONNECT SECTION -->
<rect x="80" y="1120" width="840" height="120" rx="28" fill="var(--card)" stroke="var(--stroke)"/>
<text x="120" y="1175" class="heading">💬 Let's Connect</text>

<!-- Social Links -->
<rect x="300" y="1150" width="130" height="36" rx="18" fill="var(--bg)" stroke="var(--stroke)"/>
<text x="365" y="1173" class="small">GitHub</text>

<rect x="445" y="1150" width="150" height="36" rx="18" fill="var(--bg)" stroke="var(--stroke)"/>
<text x="520" y="1173" class="small">LinkedIn</text>

<rect x="610" y="1150" width="120" height="36" rx="18" fill="var(--bg)" stroke="var(--stroke)"/>
<text x="670" y="1173" class="small">Twitter / X</text>

<rect x="745" y="1150" width="130" height="36" rx="18" fill="var(--bg)" stroke="var(--stroke)"/>
<text x="810" y="1173" class="small">Discord</text>

<text x="500" y="1290" class="small">Built with 🔥 and ❤️ in Python</text>

</svg>
"""
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml")
        self.send_header("Cache-Control", "public, max-age=1800")
        self.end_headers()
        self.wfile.write(svg.encode("utf-8"))

