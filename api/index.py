# Apple Glassmorphism & Bento Grid GitHub README Card API

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

        svg = f"""<svg width="1000" height="1060" viewBox="0 0 1000 1060" xmlns="http://www.w3.org/2000/svg">
<style>
:root {{
 --bg: #030303;
 --card: rgba(255,255,255,0.03);
 --card-border: rgba(255,255,255,0.08);
 --card-hover: rgba(255,255,255,0.05);
 --text: #ffffff;
 --muted: #a1a1aa;
 --accent: #38bdf8;
 --accent-bg: rgba(56, 189, 248, 0.1);
 --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}}

@media (prefers-color-scheme: light) {{
 :root {{
  --bg: #f8fafc;
  --card: rgba(255,255,255,0.8);
  --card-border: rgba(0,0,0,0.08);
  --card-hover: rgba(255,255,255,1);
  --text: #0f172a;
  --muted: #64748b;
  --accent: #0ea5e9;
  --accent-bg: rgba(14, 165, 233, 0.1);
 }}
}}

* {{ font-family: var(--font-family); }}

/* Background effects */
.glow-cyan {{ fill: #06b6d4; opacity: 0.15; filter: blur(100px); }}
.glow-purple {{ fill: #8b5cf6; opacity: 0.15; filter: blur(100px); }}
.glow-emerald {{ fill: #10b981; opacity: 0.15; filter: blur(100px); }}

/* Card setup */
.bento-card {{
    fill: var(--card);
    stroke: var(--card-border);
    stroke-width: 1px;
}}

/* Typography */
.name {{ font-weight: 800; font-size: 42px; fill: url(#text-gradient); letter-spacing: -1px; }}
.title-role {{ font-weight: 600; font-size: 20px; fill: var(--muted); }}
.section-title {{ font-weight: 700; font-size: 20px; fill: var(--text); letter-spacing: -0.5px; }}
.body-text {{ font-weight: 400; font-size: 15px; fill: var(--muted); line-height: 1.6; }}
.stat-val {{ font-weight: 800; font-size: 48px; fill: var(--text); text-anchor: middle; letter-spacing: -2px; }}
.stat-lbl {{ font-weight: 500; font-size: 14px; fill: var(--muted); text-anchor: middle; text-transform: uppercase; letter-spacing: 1px; }}
.chip-text {{ font-weight: 500; font-size: 13px; fill: var(--text); }}
.proj-title {{ font-weight: 700; font-size: 18px; fill: var(--text); }}
.proj-desc {{ font-weight: 400; font-size: 14px; fill: var(--muted); line-height: 1.5; }}
.tech-item {{ font-weight: 600; font-size: 15px; fill: var(--text); }}

</style>

<defs>
<linearGradient id="text-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#38bdf8"/>
    <stop offset="50%" stop-color="#818cf8"/>
    <stop offset="100%" stop-color="#c084fc"/>
</linearGradient>
</defs>

<!-- BACKGROUND -->
<rect width="1000" height="1060" fill="var(--bg)"/>

<!-- GLOW ORBS -->
<circle cx="200" cy="200" r="300" class="glow-purple"/>
<circle cx="800" cy="500" r="350" class="glow-cyan"/>
<circle cx="300" cy="900" r="250" class="glow-emerald"/>

<!-- ======================= BENTO GRID ======================= -->

<!-- 1. HERO BOX (x:30, y:30, w:460, h:300) -->
<rect x="30" y="30" width="460" height="300" rx="32" class="bento-card"/>
<text x="60" y="110" class="title-role">Hi, I'm</text>
<text x="60" y="160" class="name">Sarvesh Nakhale</text>
<text x="60" y="200" class="title-role">Software Developer | Backend Dev</text>

<!-- Contact Chips -->
<rect x="60" y="235" width="165" height="32" rx="16" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="90" y="256" class="chip-text">📍 Maharashtra, India</text>

<rect x="235" y="235" width="205" height="32" rx="16" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="260" y="256" class="chip-text">✉️ sarveshnakhale21@gmail.com</text>

<!-- 2. ABOUT ME BOX (x:510, y:30, w:460, h:300) -->
<rect x="510" y="30" width="460" height="300" rx="32" class="bento-card"/>
<text x="540" y="80" class="section-title">About Me</text>
<text x="540" y="125" class="body-text">I build clean, functional backend systems and</text>
<text x="540" y="150" class="body-text">applications that solve real-world problems.</text>
<text x="540" y="185" class="body-text">I am passionate about finding practical use cases</text>
<text x="540" y="210" class="body-text">for technology and mathematics, and I enjoy</text>
<text x="540" y="235" class="body-text">integrating complex ideas into unified, functional</text>
<text x="540" y="260" class="body-text">solutions to build things that stand out.</text>

<!-- 3. STATS: REPOS (x:30, y:350, w:220, h:200) -->
<rect x="30" y="350" width="220" height="200" rx="32" class="bento-card"/>
<text x="140" y="465" class="stat-val">{repos}</text>
<text x="140" y="500" class="stat-lbl">Repositories</text>

<!-- 4. STATS: STARS (x:270, y:350, w:220, h:200) -->
<rect x="270" y="350" width="220" height="200" rx="32" class="bento-card"/>
<text x="380" y="465" class="stat-val">{stars}</text>
<text x="380" y="500" class="stat-lbl">Total Stars</text>

<!-- 5. STATS: FOLLOWERS (x:510, y:350, w:220, h:200) -->
<rect x="510" y="350" width="220" height="200" rx="32" class="bento-card"/>
<text x="620" y="465" class="stat-val">{followers}</text>
<text x="620" y="500" class="stat-lbl">Followers</text>

<!-- 6. TECH STACK (x:750, y:350, w:220, h:520) -->
<rect x="750" y="350" width="220" height="520" rx="32" class="bento-card"/>
<text x="780" y="400" class="section-title">Tech Stack</text>

<rect x="780" y="430" width="160" height="40" rx="12" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="800" y="456" class="tech-item">☕ Java</text>

<rect x="780" y="485" width="160" height="40" rx="12" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="800" y="511" class="tech-item">🍃 Spring Boot</text>

<rect x="780" y="540" width="160" height="40" rx="12" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="800" y="566" class="tech-item">🗄️ SQL</text>

<rect x="780" y="595" width="160" height="40" rx="12" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="800" y="621" class="tech-item">🌐 HTML / CSS</text>

<rect x="780" y="650" width="160" height="40" rx="12" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="800" y="676" class="tech-item">🟨 JavaScript</text>

<rect x="780" y="705" width="160" height="40" rx="12" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="800" y="731" class="tech-item">📄 JSON</text>


<!-- 7. PROJECT 1 (x:30, y:570, w:220, h:300) -->
<rect x="30" y="570" width="220" height="300" rx="32" class="bento-card"/>
<text x="55" y="620" class="proj-title">subtext</text>
<text x="55" y="655" class="proj-desc">A high-performance,</text>
<text x="55" y="675" class="proj-desc">offline relational DB</text>
<text x="55" y="695" class="proj-desc">that embeds SQL data</text>
<text x="55" y="715" class="proj-desc">into LSBs of images.</text>
<rect x="55" y="810" width="55" height="26" rx="8" fill="var(--accent-bg)"/><text x="68" y="828" class="chip-text" style="font-size:12px; fill:var(--accent);">Rust</text>
<rect x="115" y="810" width="50" height="26" rx="8" fill="var(--accent-bg)"/><text x="127" y="828" class="chip-text" style="font-size:12px; fill:var(--accent);">SQL</text>

<!-- 8. PROJECT 2 (x:270, y:570, w:220, h:300) -->
<rect x="270" y="570" width="220" height="300" rx="32" class="bento-card"/>
<text x="295" y="620" class="proj-title">specter</text>
<text x="295" y="655" class="proj-desc">A zero-cost, parasitic</text>
<text x="295" y="675" class="proj-desc">AI engine that runs</text>
<text x="295" y="695" class="proj-desc">LLM API calls locally</text>
<text x="295" y="715" class="proj-desc">on client hardware.</text>
<rect x="295" y="775" width="85" height="26" rx="8" fill="var(--accent-bg)"/><text x="306" y="793" class="chip-text" style="font-size:12px; fill:var(--accent);">TypeScript</text>
<rect x="385" y="775" width="50" height="26" rx="8" fill="var(--accent-bg)"/><text x="397" y="793" class="chip-text" style="font-size:12px; fill:var(--accent);">Rust</text>
<rect x="295" y="810" width="70" height="26" rx="8" fill="var(--accent-bg)"/><text x="308" y="828" class="chip-text" style="font-size:12px; fill:var(--accent);">WebGPU</text>

<!-- 9. PROJECT 3 (x:510, y:570, w:220, h:300) -->
<rect x="510" y="570" width="220" height="300" rx="32" class="bento-card"/>
<text x="535" y="620" class="proj-title">voidNet</text>
<text x="535" y="655" class="proj-desc">The ICMP Ghost Protocol.</text>
<text x="535" y="675" class="proj-desc">An unstoppable tunnel</text>
<text x="535" y="695" class="proj-desc">disguising traffic</text>
<text x="535" y="715" class="proj-desc">as standard Pings.</text>
<rect x="535" y="810" width="85" height="26" rx="8" fill="var(--accent-bg)"/><text x="546" y="828" class="chip-text" style="font-size:12px; fill:var(--accent);">TypeScript</text>
<rect x="625" y="810" width="85" height="26" rx="8" fill="var(--accent-bg)"/><text x="635" y="828" class="chip-text" style="font-size:12px; fill:var(--accent);">Networking</text>

<!-- 10. SOCIALS BOX (x:30, y:890, w:700, h:120) -->
<rect x="30" y="890" width="700" height="120" rx="32" class="bento-card"/>
<text x="60" y="930" class="section-title">Let's Connect</text>

<rect x="60" y="955" width="130" height="36" rx="18" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="90" y="978" class="chip-text">GitHub</text>

<rect x="200" y="955" width="130" height="36" rx="18" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="228" y="978" class="chip-text">LinkedIn</text>

<rect x="340" y="955" width="130" height="36" rx="18" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="365" y="978" class="chip-text">Twitter / X</text>

<rect x="480" y="955" width="130" height="36" rx="18" fill="var(--bg)" stroke="var(--card-border)"/>
<text x="515" y="978" class="chip-text">Discord</text>


<!-- 11. AVAILABILITY BOX (x:750, y:890, w:220, h:120) -->
<rect x="750" y="890" width="220" height="120" rx="32" class="bento-card"/>
<circle cx="860" cy="940" r="8" fill="#10b981">
    <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
</circle>
<text x="860" y="975" class="chip-text" style="text-anchor:middle;">Available for</text>
<text x="860" y="995" class="chip-text" style="text-anchor:middle;">new opportunities</text>

</svg>
"""
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml")
        self.send_header("Cache-Control", "public, max-age=1800")
        self.end_headers()
        self.wfile.write(svg.encode("utf-8"))


