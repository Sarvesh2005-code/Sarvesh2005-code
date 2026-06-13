# Typography-Driven Minimalist Light/Dark Dashboard

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

        svg = f"""<svg width="1000" height="850" viewBox="0 0 1000 850" xmlns="http://www.w3.org/2000/svg">
<style>
/* Light Mode (Default) */
:root {{
    --bg-color: #fdfdfd;
    --text-main: #111827;
    --text-muted: #6b7280;
    --text-accent: #374151;
    --line-color: #e5e7eb;
    --font-fam: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}}

/* Dark Mode Override */
@media (prefers-color-scheme: dark) {{
    :root {{
        --bg-color: #0d1117;
        --text-main: #f9fafb;
        --text-muted: #9ca3af;
        --text-accent: #d1d5db;
        --line-color: #374151;
    }}
}}

* {{ font-family: var(--font-fam); }}

.bg {{ fill: var(--bg-color); }}
.sep {{ stroke: var(--line-color); stroke-width: 1px; }}

.h1-mega {{ font-weight: 800; font-size: 46px; fill: var(--text-main); letter-spacing: -2px; }}
.role-text {{ font-weight: 500; font-size: 18px; fill: var(--text-muted); letter-spacing: -0.5px; }}

.body-text {{ font-weight: 400; font-size: 15px; fill: var(--text-muted); line-height: 1.6; }}
.contact-label {{ font-weight: 600; font-size: 14px; fill: var(--text-main); letter-spacing: -0.2px; }}
.contact-val {{ font-weight: 400; font-size: 14px; fill: var(--text-muted); }}

.section-title {{ font-weight: 800; font-size: 24px; fill: var(--text-main); letter-spacing: -1px; }}

.block-title {{ font-weight: 700; font-size: 16px; fill: var(--text-main); letter-spacing: -0.5px; }}
.block-desc {{ font-weight: 400; font-size: 15px; fill: var(--text-muted); }}

.stat-lbl {{ font-weight: 500; font-size: 16px; fill: var(--text-muted); }}
.stat-val {{ font-weight: 800; font-size: 36px; fill: var(--text-main); letter-spacing: -1px; }}

.proj-title {{ font-weight: 800; font-size: 20px; fill: var(--text-main); letter-spacing: -0.5px; }}
.proj-desc {{ font-weight: 400; font-size: 15px; fill: var(--text-muted); }}
.proj-tech {{ font-weight: 600; font-size: 14px; fill: var(--text-accent); }}
</style>

<!-- BACKGROUND -->
<rect width="1000" height="850" class="bg" />

<!-- ======================= LEFT COLUMN: IDENTITY ======================= -->
<text x="50" y="100" class="h1-mega">Sarvesh</text>
<text x="50" y="145" class="h1-mega">Nakhale</text>
<text x="50" y="180" class="role-text">Backend Engineer</text>

<line x1="50" y1="210" x2="280" y2="210" class="sep" />

<text x="50" y="245" class="body-text">I build clean, functional</text>
<text x="50" y="270" class="body-text">backend systems and</text>
<text x="50" y="295" class="body-text">applications that solve</text>
<text x="50" y="320" class="body-text">real-world problems.</text>

<text x="50" y="375" class="contact-label">Contact Info</text>

<g stroke="var(--text-muted)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <!-- Location Icon -->
    <g transform="translate(50, 391) scale(0.65)">
        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
        <circle cx="12" cy="10" r="3" />
    </g>
    <text x="75" y="405" class="contact-val" stroke="none">Maharashtra, India</text>

    <!-- Email Icon -->
    <g transform="translate(50, 421) scale(0.65)">
        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
        <polyline points="22,6 12,13 2,6" />
    </g>
    <text x="75" y="435" class="contact-val" stroke="none">sarveshnakhale21@gmail.com</text>

    <!-- Globe/Link Icon -->
    <g transform="translate(50, 451) scale(0.65)">
        <circle cx="12" cy="12" r="10" />
        <line x1="2" y1="12" x2="22" y2="12" />
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
    </g>
    <text x="75" y="465" class="contact-val" stroke="none">sarvy.vercel.app</text>
</g>

<!-- Global Vertical Separator -->
<line x1="320" y1="50" x2="320" y2="800" class="sep" />

<!-- ======================= RIGHT COLUMN: PORTFOLIO ======================= -->

<!-- SECTION 1: KEY EXPERTISE -->
<text x="360" y="100" class="section-title">Key Expertise</text>
<line x1="360" y1="125" x2="950" y2="125" class="sep" />

<!-- Block 1 -->
<text x="360" y="165" class="block-title">Core Backend</text>
<text x="360" y="195" class="block-desc">Java, Spring Boot</text>

<line x1="550" y1="145" x2="550" y2="215" class="sep" />

<!-- Block 2 -->
<text x="580" y="165" class="block-title">Data Engineering</text>
<text x="580" y="195" class="block-desc">SQL, JSON, Rest APIs</text>

<line x1="770" y1="145" x2="770" y2="215" class="sep" />

<!-- Block 3 -->
<text x="800" y="165" class="block-title">Kernel &amp; Tooling</text>
<text x="800" y="195" class="block-desc">Linux, Git, System I/O</text>


<!-- SECTION 2: TELEMETRY -->
<text x="360" y="275" class="section-title">Activity &amp; Contributions</text>
<line x1="360" y1="300" x2="950" y2="300" class="sep" />

<text x="360" y="360" class="stat-lbl">Repositories</text>
<text x="360" y="405" class="stat-val">{repos}</text>

<line x1="550" y1="330" x2="550" y2="420" class="sep" />

<text x="580" y="360" class="stat-lbl">Star Gazers</text>
<text x="580" y="405" class="stat-val">{stars}</text>

<line x1="770" y1="330" x2="770" y2="420" class="sep" />

<text x="800" y="360" class="stat-lbl">Followers</text>
<text x="800" y="405" class="stat-val">{followers}</text>


<!-- SECTION 3: FEATURED ARCHITECTURE -->
<text x="360" y="485" class="section-title">Featured Architecture</text>
<line x1="360" y1="510" x2="950" y2="510" class="sep" />

<!-- Proj 1 -->
<text x="360" y="550" class="proj-title">Project: subtext</text>
<text x="360" y="575" class="proj-desc">High-performance offline relational DB mathematically embedding SQL in images.</text>
<text x="360" y="600" class="proj-tech">Rust, SQL</text>

<!-- Proj 2 -->
<text x="360" y="650" class="proj-title">Project: specter</text>
<text x="360" y="675" class="proj-desc">Zero-cost parasitic AI engine intercepting LLM API calls to run locally on hardware.</text>
<text x="360" y="700" class="proj-tech">TypeScript, WebGPU</text>

<!-- Proj 3 -->
<text x="360" y="750" class="proj-title">Project: voidNet</text>
<text x="360" y="775" class="proj-desc">The ICMP Ghost Protocol. Unstoppable network tunnel disguised as standard Pings.</text>
<text x="360" y="800" class="proj-tech">TypeScript, Network</text>

</svg>
"""
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml")
        self.send_header("Cache-Control", "public, max-age=1800")
        self.end_headers()
        self.wfile.write(svg.encode("utf-8"))


