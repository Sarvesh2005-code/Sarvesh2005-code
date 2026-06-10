# Linear-inspired Dashboard GitHub README Card API

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

        svg = f"""<svg width="1000" height="780" viewBox="0 0 1000 780" xmlns="http://www.w3.org/2000/svg">
<style>
:root {{
 --bg: #000000;
 --card-fill: rgba(255, 255, 255, 0.015);
 --text-main: #ffffff;
 --text-muted: #a1a1aa;
 --accent: #60a5fa;
 --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}}

* {{ font-family: var(--font-family); }}

.bg {{ fill: var(--bg); }}
.glass-card {{ fill: var(--card-fill); stroke: url(#card-border); stroke-width: 1px; backdrop-filter: blur(10px); }}

.hero-name {{ font-weight: 800; font-size: 26px; fill: var(--text-main); letter-spacing: -0.5px; }}
.hero-role {{ font-weight: 500; font-size: 15px; fill: var(--text-muted); }}
.contact-text {{ font-weight: 500; font-size: 13px; fill: var(--text-muted); }}

.section-label {{ font-weight: 600; font-size: 12px; fill: var(--text-muted); letter-spacing: 2px; text-transform: uppercase; }}
.body-text {{ font-weight: 400; font-size: 15px; fill: var(--text-muted); line-height: 1.6; }}

.stat-val {{ font-weight: 700; font-size: 32px; fill: var(--text-main); text-anchor: middle; letter-spacing: -1px; }}
.stat-lbl {{ font-weight: 600; font-size: 11px; fill: var(--text-muted); text-anchor: middle; letter-spacing: 1.5px; text-transform: uppercase; }}

.badge-text {{ font-weight: 600; font-size: 13px; fill: var(--text-main); }}

.proj-title {{ font-weight: 700; font-size: 18px; fill: var(--text-main); }}
.proj-desc {{ font-weight: 400; font-size: 14px; fill: var(--text-muted); }}
.proj-tag {{ font-weight: 600; font-size: 12px; fill: var(--accent); }}

.btn-fill {{ fill: rgba(255,255,255,0.03); stroke: rgba(255,255,255,0.08); stroke-width: 1px; }}
.btn-text {{ font-weight: 500; font-size: 14px; fill: var(--text-main); }}
</style>

<defs>
<linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="rgba(255,255,255,0.15)"/>
    <stop offset="100%" stop-color="rgba(255,255,255,0.02)"/>
</linearGradient>

<filter id="blur-heavy" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="100" />
</filter>
</defs>

<!-- BACKGROUND -->
<rect width="1000" height="780" class="bg"/>

<!-- ANIMATED AURORA ORBS -->
<g filter="url(#blur-heavy)">
  <!-- Indigo -->
  <circle cx="200" cy="150" r="300" fill="#4f46e5" opacity="0.3">
    <animate attributeName="cx" values="100; 400; 100" dur="20s" repeatCount="indefinite" />
    <animate attributeName="cy" values="150; 50; 150" dur="25s" repeatCount="indefinite" />
  </circle>
  <!-- Cyan -->
  <circle cx="800" cy="600" r="350" fill="#06b6d4" opacity="0.25">
    <animate attributeName="cx" values="800; 600; 800" dur="22s" repeatCount="indefinite" />
    <animate attributeName="cy" values="600; 700; 600" dur="18s" repeatCount="indefinite" />
  </circle>
  <!-- Rose -->
  <circle cx="500" cy="400" r="250" fill="#e11d48" opacity="0.2">
    <animate attributeName="cx" values="500; 700; 500" dur="24s" repeatCount="indefinite" />
    <animate attributeName="cy" values="400; 200; 400" dur="21s" repeatCount="indefinite" />
  </circle>
</g>

<!-- ===================== DASHBOARD LAYOUT ===================== -->

<!-- === LEFT SIDEBAR (x:30, w:280) === -->

<!-- Hero Card -->
<rect x="30" y="40" width="280" height="230" rx="20" class="glass-card"/>
<text x="55" y="90" class="hero-name">SARVESH NAKHALE</text>
<text x="55" y="115" class="hero-role">Software Developer | Backend</text>

<text x="55" y="160" class="contact-text">📍 Maharashtra, India</text>
<text x="55" y="190" class="contact-text">✉️ sarveshnakhale21@gmail.com</text>

<circle cx="62" cy="225" r="5" fill="#10b981">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
</circle>
<text x="75" y="230" class="contact-text" style="fill:var(--text-main);">Available for opportunities</text>

<!-- Stats Card -->
<rect x="30" y="290" width="280" height="120" rx="20" class="glass-card"/>
<text x="76" y="345" class="stat-val">{repos}</text>
<text x="76" y="375" class="stat-lbl">REPOS</text>

<text x="170" y="345" class="stat-val">{stars}</text>
<text x="170" y="375" class="stat-lbl">STARS</text>

<text x="264" y="345" class="stat-val">{followers}</text>
<text x="264" y="375" class="stat-lbl">FOLLOWS</text>

<!-- Socials Card -->
<rect x="30" y="430" width="280" height="280" rx="20" class="glass-card"/>
<text x="55" y="475" class="section-label">LET'S CONNECT</text>

<rect x="55" y="495" width="230" height="36" rx="8" class="btn-fill"/>
<text x="75" y="518" class="btn-text">🌐 GitHub Profile</text>

<rect x="55" y="545" width="230" height="36" rx="8" class="btn-fill"/>
<text x="75" y="568" class="btn-text">💼 LinkedIn Network</text>

<rect x="55" y="595" width="230" height="36" rx="8" class="btn-fill"/>
<text x="75" y="618" class="btn-text">🐦 Twitter / X</text>

<rect x="55" y="645" width="230" height="36" rx="8" class="btn-fill"/>
<text x="75" y="668" class="btn-text">🎮 Discord Server</text>


<!-- === MAIN FEED (x:330, w:640) === -->

<!-- About Me -->
<rect x="330" y="40" width="640" height="180" rx="20" class="glass-card"/>
<text x="365" y="85" class="section-label">ABOUT ME</text>
<text x="365" y="120" class="body-text">I build clean, functional backend systems and</text>
<text x="365" y="145" class="body-text">applications that solve real-world problems. I am</text>
<text x="365" y="170" class="body-text">passionate about finding practical use cases for</text>
<text x="365" y="195" class="body-text">technology, and integrating complex ideas into</text>

<!-- Tech Stack -->
<rect x="330" y="240" width="640" height="140" rx="20" class="glass-card"/>
<text x="365" y="285" class="section-label">ENGINEERING STACK</text>

<!-- Stack Badges Row 1 -->
<rect x="365" y="305" width="80" height="32" rx="8" class="btn-fill"/><text x="382" y="326" class="badge-text">☕ Java</text>
<rect x="460" y="305" width="130" height="32" rx="8" class="btn-fill"/><text x="477" y="326" class="badge-text">🍃 Spring Boot</text>
<rect x="605" y="305" width="75" height="32" rx="8" class="btn-fill"/><text x="622" y="326" class="badge-text">🗄️ SQL</text>
<rect x="695" y="305" width="165" height="32" rx="8" class="btn-fill"/><text x="712" y="326" class="badge-text">🌐 HTML / CSS / JS</text>

<!-- Stack Badges Row 2 -->
<rect x="365" y="350" width="90" height="32" rx="8" class="btn-fill"/><text x="382" y="371" class="badge-text">📄 JSON</text>
<rect x="470" y="350" width="90" height="32" rx="8" class="btn-fill"/><text x="487" y="371" class="badge-text">🐧 Linux</text>
<rect x="575" y="350" width="80" height="32" rx="8" class="btn-fill"/><text x="592" y="371" class="badge-text">⚙️ Git</text>
<rect x="670" y="350" width="120" height="32" rx="8" class="btn-fill"/><text x="687" y="371" class="badge-text">⛓️ Blockchain</text>

<!-- Projects -->
<rect x="330" y="400" width="640" height="350" rx="20" class="glass-card"/>
<text x="365" y="445" class="section-label">FEATURED ARCHITECTURE</text>

<!-- Proj 1 -->
<rect x="365" y="465" width="570" height="85" rx="12" class="btn-fill"/>
<text x="390" y="495" class="proj-title">subtext</text>
<text x="390" y="520" class="proj-desc">High-performance offline relational DB that</text>
<text x="390" y="540" class="proj-desc">mathematically embeds SQL in images.</text>
<text x="880" y="505" class="proj-tag">Rust • SQL</text>

<!-- Proj 2 -->
<rect x="365" y="565" width="570" height="85" rx="12" class="btn-fill"/>
<text x="390" y="595" class="proj-title">specter</text>
<text x="390" y="620" class="proj-desc">Zero-cost parasitic AI engine intercepting</text>
<text x="390" y="640" class="proj-desc">LLM API calls to run locally on hardware.</text>
<text x="825" y="605" class="proj-tag">TypeScript • WebGPU</text>

<!-- Proj 3 -->
<rect x="365" y="665" width="570" height="85" rx="12" class="btn-fill"/>
<text x="390" y="695" class="proj-title">voidNet</text>
<text x="390" y="720" class="proj-desc">The ICMP Ghost Protocol. Unstoppable network</text>
<text x="390" y="740" class="proj-desc">tunnel disguised as standard Pings.</text>
<text x="825" y="705" class="proj-tag">TypeScript • Network</text>

</svg>
"""
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml")
        self.send_header("Cache-Control", "public, max-age=1800")
        self.end_headers()
        self.wfile.write(svg.encode("utf-8"))


