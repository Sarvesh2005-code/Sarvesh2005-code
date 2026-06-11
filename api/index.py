# Ghost OS Terminal GitHub README Card API

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
:root {{
 --bg: #050505;
 --cyan-bright: #00f0ff;
 --cyan-dim: #008b94;
 --red-alert: #ff003c;
 --text-bright: #ffffff;
 --text-dim: #a3a3a3;
 --panel-bg: rgba(0, 240, 255, 0.02);
 --font-mono: 'Courier New', Courier, Consolas, 'Fira Code', monospace;
}}

* {{ font-family: var(--font-mono); }}

.bg {{ fill: var(--bg); }}

/* Terminal text styles */
.term-h1 {{ font-weight: 700; font-size: 18px; fill: var(--cyan-bright); letter-spacing: 2px; }}
.term-h2 {{ font-weight: 700; font-size: 16px; fill: var(--text-bright); letter-spacing: 1px; }}
.term-p {{ font-weight: 400; font-size: 15px; fill: var(--text-dim); }}
.term-glow {{ font-weight: 700; font-size: 15px; fill: var(--cyan-bright); }}
.term-alert {{ font-weight: 700; font-size: 15px; fill: var(--red-alert); }}

/* HUD paths */
.hud-panel {{ fill: var(--panel-bg); stroke: var(--cyan-dim); stroke-width: 1px; }}
.hud-corner {{ fill: none; stroke: var(--cyan-bright); stroke-width: 2px; }}
</style>

<defs>
<linearGradient id="radar-sweep" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.3"/>
    <stop offset="100%" stop-color="#050505" stop-opacity="0"/>
</linearGradient>

<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(0, 240, 255, 0.05)" stroke-width="1"/>
</pattern>
</defs>

<!-- BACKGROUND -->
<rect width="1000" height="850" class="bg"/>
<rect width="1000" height="850" fill="url(#grid)"/>

<!-- BACKGROUND RADAR (Animated) -->
<g>
    <animateTransform attributeName="transform" type="rotate" from="0 500 425" to="360 500 425" dur="15s" repeatCount="indefinite" />
    <circle cx="500" cy="425" r="350" fill="none" stroke="var(--cyan-dim)" stroke-width="1" stroke-dasharray="10 30" opacity="0.3"/>
    <circle cx="500" cy="425" r="200" fill="none" stroke="var(--cyan-dim)" stroke-width="1" stroke-dasharray="5 15" opacity="0.2"/>
    <path d="M500,425 L500,75 A350,350 0 0,1 850,425 Z" fill="url(#radar-sweep)"/>
</g>

<!-- CRT SCANNING LINE -->
<line x1="0" y1="0" x2="1000" y2="0" stroke="var(--cyan-bright)" stroke-width="2" opacity="0.3">
  <animate attributeName="y1" values="-10; 860; -10" dur="8s" repeatCount="indefinite" />
  <animate attributeName="y2" values="-10; 860; -10" dur="8s" repeatCount="indefinite" />
</line>

<!-- ===================== TOP HEADER ===================== -->
<text x="30" y="40" class="term-p">&gt; SYSTEM.BOOT_SEQUENCE... <tspan class="term-glow">OK</tspan></text>
<text x="30" y="65" class="term-p">&gt; AUTHENTICATION [NAKHALE_S]... <tspan class="term-glow">GRANTED</tspan></text>
<text x="30" y="90" class="term-p">&gt; LOADING GHOST_OS... 100%</text>

<!-- Blinking Cursor -->
<rect x="290" y="75" width="10" height="18" fill="var(--cyan-bright)">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
</rect>

<!-- ===================== LEFT PANEL: TELEMETRY ===================== -->
<path class="hud-panel" d="M30 140 L380 140 L380 800 L50 800 L30 780 Z" />
<!-- Top-Left Corner Accent -->
<polyline class="hud-corner" points="30,160 30,140 50,140" />
<!-- Bottom-Right Corner Accent -->
<polyline class="hud-corner" points="360,800 380,800 380,780" />

<text x="50" y="170" class="term-h1">[ SYSTEM TELEMETRY ]</text>

<text x="50" y="220" class="term-p">&gt; CLASS  : BACKEND_ENGINEER</text>
<text x="50" y="245" class="term-p">&gt; PING   : sarveshnakhale21@gmail.com</text>
<text x="50" y="270" class="term-p">&gt; LOC    : MAHARASHTRA_IND</text>
<text x="50" y="295" class="term-p">&gt; STATUS : <tspan class="term-glow">AVAILABLE_FOR_MISSION</tspan></text>

<text x="50" y="360" class="term-h2">[ GITHUB_DATALINK ]</text>
<text x="50" y="400" class="term-p">REPOS  : <tspan class="term-bright" style="fill:#fff;">{repos:03d}</tspan> <tspan class="term-glow">[ONLINE]</tspan></text>
<text x="50" y="425" class="term-p">STARS  : <tspan class="term-bright" style="fill:#fff;">{stars:03d}</tspan> <tspan class="term-glow">[SYNCED]</tspan></text>
<text x="50" y="450" class="term-p">FOLLOW : <tspan class="term-bright" style="fill:#fff;">{followers:03d}</tspan> <tspan class="term-glow">[ACTIVE]</tspan></text>

<text x="50" y="520" class="term-h2">[ NETWORK_PROTOCOLS ]</text>
<text x="50" y="560" class="term-p">&gt; ssh://github.user</text>
<text x="50" y="585" class="term-p">&gt; https://linkedin.auth</text>
<text x="50" y="610" class="term-p">&gt; ws://twitter.com/x</text>
<text x="50" y="635" class="term-p">&gt; rpc://discord.server</text>

<!-- ===================== RIGHT PANEL: SUBROUTINES ===================== -->
<path class="hud-panel" d="M430 140 L410 160 L410 800 L950 800 L970 780 L970 140 Z" />
<!-- Top-Right Corner Accent -->
<polyline class="hud-corner" points="950,140 970,140 970,160" />
<!-- Bottom-Left Corner Accent -->
<polyline class="hud-corner" points="410,780 410,800 430,800" />

<text x="440" y="170" class="term-h1">[ ACTIVE SUBROUTINES ]</text>

<text x="440" y="220" class="term-h2">[ CORE_OBJECTIVE ]</text>
<text x="440" y="250" class="term-p">&gt; I build offline relational databases embedded in images,</text>
<text x="440" y="275" class="term-p">&gt; parasitic AI engines intercepting LLM API calls,</text>
<text x="440" y="300" class="term-p">&gt; and ICMP ghost protocols.</text>

<text x="440" y="360" class="term-h2">[ ARCHITECTURE_LOG ]</text>
<text x="440" y="390" class="term-p">&gt; COMPILING_PAYLOADS : <tspan style="fill:#fff;">Java, Spring Boot, SQL</tspan></text>
<text x="440" y="415" class="term-p">&gt; FRONTEND_MATRIX    : <tspan style="fill:#fff;">HTML, CSS, JS</tspan></text>
<text x="440" y="440" class="term-p">&gt; KERNEL_ENV         : <tspan style="fill:#fff;">Linux, Git</tspan></text>
<text x="440" y="465" class="term-p">&gt; DISTRIBUTED_LEDGER : <tspan style="fill:#fff;">Blockchain</tspan></text>

<text x="440" y="530" class="term-h2">[ CLASSIFIED_MODULES ]</text>

<!-- Subroutine 1 -->
<text x="440" y="570" class="term-alert">[EXECUTING]</text>
<text x="550" y="570" class="term-p">-&gt; subtext.exe (Rust/SQL)</text>
<text x="440" y="595" class="term-p">&gt; High-performance offline relational DB that</text>
<text x="440" y="615" class="term-p">&gt; mathematically embeds SQL in images.</text>

<!-- Subroutine 2 -->
<text x="440" y="655" class="term-glow">[ACTIVE]</text>
<text x="525" y="655" class="term-p">-&gt; specter.ts (TypeScript/WebGPU)</text>
<text x="440" y="680" class="term-p">&gt; Zero-cost parasitic AI engine intercepting</text>
<text x="440" y="700" class="term-p">&gt; LLM API calls to run locally on hardware.</text>

<!-- Subroutine 3 -->
<text x="440" y="740" class="term-p" style="fill:#fff;">[STEALTH]</text>
<text x="535" y="740" class="term-p">-&gt; voidNet.sys (TypeScript/Network)</text>
<text x="440" y="765" class="term-p">&gt; The ICMP Ghost Protocol. Unstoppable network</text>
<text x="440" y="785" class="term-p">&gt; tunnel disguised as standard Pings.</text>

</svg>
"""
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml")
        self.send_header("Cache-Control", "public, max-age=1800")
        self.end_headers()
        self.wfile.write(svg.encode("utf-8"))


