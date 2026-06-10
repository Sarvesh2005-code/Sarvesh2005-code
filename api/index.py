# Apple Neumorphism GitHub README Card API

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

        svg = f"""<svg width="1000" height="1070" viewBox="0 0 1000 1070" xmlns="http://www.w3.org/2000/svg">
<style>
:root {{
 --bg: #1e1e1e;
 --text: #e0e0e0;
 --muted: #888888;
 --accent-cyan: #00ffcc;
 --accent-pink: #ff0066;
 --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}}

* {{ font-family: var(--font-family); }}

.bg-rect {{ fill: var(--bg); }}

/* Typography */
.name {{ font-weight: 800; font-size: 42px; fill: var(--accent-cyan); letter-spacing: -1px; }}
.title-role {{ font-weight: 600; font-size: 20px; fill: var(--muted); }}
.section-title {{ font-weight: 700; font-size: 20px; fill: var(--accent-pink); letter-spacing: -0.5px; }}
.body-text {{ font-weight: 400; font-size: 15px; fill: var(--text); line-height: 1.6; }}
.stat-val {{ font-weight: 800; font-size: 48px; fill: var(--text); text-anchor: middle; letter-spacing: -2px; }}
.stat-lbl {{ font-weight: 500; font-size: 14px; fill: var(--accent-cyan); text-anchor: middle; text-transform: uppercase; letter-spacing: 1px; }}
.chip-text {{ font-weight: 600; font-size: 13px; fill: var(--bg); }}
.proj-title {{ font-weight: 800; font-size: 18px; fill: var(--text); }}
.proj-desc {{ font-weight: 400; font-size: 14px; fill: var(--muted); line-height: 1.5; }}
.tech-item {{ font-weight: 600; font-size: 15px; fill: var(--text); }}

</style>

<defs>
<!-- Perfect Neumorphism Dual Shadow Filter -->
<filter id="neu" x="-20%" y="-20%" width="140%" height="140%">
  <!-- Light highlight top-left -->
  <feGaussianBlur in="SourceAlpha" stdDeviation="6" result="blurLight"/>
  <feOffset in="blurLight" dx="-6" dy="-6" result="offsetLight"/>
  <feFlood flood-color="#2a2a2a" flood-opacity="1"/>
  <feComposite in2="offsetLight" operator="in" result="shadowLight"/>

  <!-- Dark shadow bottom-right -->
  <feGaussianBlur in="SourceAlpha" stdDeviation="8" result="blurDark"/>
  <feOffset in="blurDark" dx="8" dy="8" result="offsetDark"/>
  <feFlood flood-color="#121212" flood-opacity="1"/>
  <feComposite in2="offsetDark" operator="in" result="shadowDark"/>

  <!-- Merge -->
  <feMerge>
    <feMergeNode in="shadowDark"/>
    <feMergeNode in="shadowLight"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
</defs>

<!-- BACKGROUND -->
<rect width="1000" height="1070" class="bg-rect"/>

<!-- ======================= NEUMORPHIC GRID ======================= -->

<!-- 1. HERO BOX (Dur: 6s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0" dur="6s" repeatCount="indefinite" />
<rect x="35" y="40" width="450" height="280" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="65" y="100" class="title-role">Hi, I'm</text>
<text x="65" y="150" class="name">Sarvesh Nakhale</text>
<text x="65" y="190" class="title-role">Software Developer | Backend Dev</text>

<rect x="65" y="220" width="165" height="32" rx="16" fill="var(--accent-cyan)"/>
<text x="95" y="241" class="chip-text">📍 Maharashtra, India</text>

<rect x="240" y="220" width="205" height="32" rx="16" fill="var(--accent-pink)"/>
<text x="255" y="241" class="chip-text" style="fill:#fff;">✉️ sarveshnakhale21@gmail.com</text>
</g>

<!-- 2. ABOUT ME BOX (Dur: 7s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-6; 0,0" dur="7s" repeatCount="indefinite" />
<rect x="515" y="40" width="450" height="280" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="545" y="85" class="section-title">About Me</text>
<text x="545" y="125" class="body-text">I build clean, functional backend systems and</text>
<text x="545" y="150" class="body-text">applications that solve real-world problems.</text>
<text x="545" y="185" class="body-text">I am passionate about finding practical use cases</text>
<text x="545" y="210" class="body-text">for technology and mathematics, and I enjoy</text>
<text x="545" y="235" class="body-text">integrating complex ideas into unified, functional</text>
<text x="545" y="260" class="body-text">solutions to build things that stand out.</text>
</g>

<!-- 3. STATS: REPOS (Dur: 5.5s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-10; 0,0" dur="5.5s" repeatCount="indefinite" />
<rect x="35" y="350" width="210" height="200" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="140" y="465" class="stat-val">{repos}</text>
<text x="140" y="500" class="stat-lbl">Repositories</text>
</g>

<!-- 4. STATS: STARS (Dur: 6.5s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-7; 0,0" dur="6.5s" repeatCount="indefinite" />
<rect x="275" y="350" width="210" height="200" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="380" y="465" class="stat-val">{stars}</text>
<text x="380" y="500" class="stat-lbl">Total Stars</text>
</g>

<!-- 5. STATS: FOLLOWERS (Dur: 7.5s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-9; 0,0" dur="7.5s" repeatCount="indefinite" />
<rect x="515" y="350" width="210" height="200" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="620" y="465" class="stat-val">{followers}</text>
<text x="620" y="500" class="stat-lbl">Followers</text>
</g>

<!-- 6. TECH STACK (Dur: 8s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-5; 0,0" dur="8s" repeatCount="indefinite" />
<rect x="755" y="350" width="210" height="530" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="785" y="405" class="section-title">Tech Stack</text>
<text x="785" y="456" class="tech-item">☕ Java</text>
<text x="785" y="511" class="tech-item">🍃 Spring Boot</text>
<text x="785" y="566" class="tech-item">🗄️ SQL</text>
<text x="785" y="621" class="tech-item">🌐 HTML / CSS</text>
<text x="785" y="676" class="tech-item">🟨 JavaScript</text>
<text x="785" y="731" class="tech-item">📄 JSON</text>
<text x="785" y="786" class="tech-item">🐧 Linux</text>
<text x="785" y="841" class="tech-item">⚙️ Git</text>
</g>

<!-- 7. PROJECT 1 (Dur: 6s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-7; 0,0" dur="6s" repeatCount="indefinite" />
<rect x="35" y="580" width="210" height="300" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="65" y="630" class="proj-title">subtext</text>
<text x="65" y="665" class="proj-desc">A high-performance,</text>
<text x="65" y="685" class="proj-desc">offline relational DB</text>
<text x="65" y="705" class="proj-desc">that embeds SQL data</text>
<text x="65" y="725" class="proj-desc">into LSBs of images.</text>
<text x="65" y="830" class="chip-text" style="fill:var(--accent-cyan);">Rust • SQL</text>
</g>

<!-- 8. PROJECT 2 (Dur: 7s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0" dur="7s" repeatCount="indefinite" />
<rect x="275" y="580" width="210" height="300" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="305" y="630" class="proj-title">specter</text>
<text x="305" y="665" class="proj-desc">A zero-cost, parasitic</text>
<text x="305" y="685" class="proj-desc">AI engine that runs</text>
<text x="305" y="705" class="proj-desc">LLM API calls locally</text>
<text x="305" y="725" class="proj-desc">on client hardware.</text>
<text x="305" y="830" class="chip-text" style="fill:var(--accent-pink);">TypeScript • WebGPU</text>
</g>

<!-- 9. PROJECT 3 (Dur: 6.5s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-6; 0,0" dur="6.5s" repeatCount="indefinite" />
<rect x="515" y="580" width="210" height="300" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="545" y="630" class="proj-title">voidNet</text>
<text x="545" y="665" class="proj-desc">The ICMP Ghost</text>
<text x="545" y="685" class="proj-desc">Protocol. A tunnel</text>
<text x="545" y="705" class="proj-desc">disguising traffic</text>
<text x="545" y="725" class="proj-desc">as standard Pings.</text>
<text x="545" y="830" class="chip-text" style="fill:var(--accent-cyan);">TypeScript • Net</text>
</g>

<!-- 10. SOCIALS BOX (Dur: 7.5s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-5; 0,0" dur="7.5s" repeatCount="indefinite" />
<rect x="35" y="910" width="690" height="120" rx="32" class="bg-rect" filter="url(#neu)"/>
<text x="65" y="950" class="section-title">Let's Connect</text>

<text x="65" y="990" class="tech-item">🌐 GitHub</text>
<text x="190" y="990" class="tech-item">💼 LinkedIn</text>
<text x="320" y="990" class="tech-item">🐦 Twitter / X</text>
<text x="460" y="990" class="tech-item">🎮 Discord</text>
</g>

<!-- 11. AVAILABILITY BOX (Dur: 6s) -->
<g>
<animateTransform attributeName="transform" type="translate" values="0,0; 0,-7; 0,0" dur="6s" repeatCount="indefinite" />
<rect x="755" y="910" width="210" height="120" rx="32" class="bg-rect" filter="url(#neu)"/>
<circle cx="860" cy="955" r="8" fill="var(--accent-cyan)">
    <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
</circle>
<text x="860" y="990" class="tech-item" style="text-anchor:middle; font-size:13px;">Available for</text>
<text x="860" y="1010" class="tech-item" style="text-anchor:middle; font-size:13px;">new opportunities</text>
</g>

</svg>
"""
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml")
        self.send_header("Cache-Control", "public, max-age=1800")
        self.end_headers()
        self.wfile.write(svg.encode("utf-8"))


