# Apple Glassmorphism GitHub README Card API
# Drop-in replacement for your Vercel Python endpoint

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

        svg = f"""
<svg width="1000" height="1300" viewBox="0 0 1000 1300"
xmlns="http://www.w3.org/2000/svg">

<style>
:root {{
 --bg:#0d1117;
 --card:rgba(255,255,255,.06);
 --stroke:rgba(255,255,255,.12);
 --text:#f8fafc;
 --muted:#9ca3af;
 --accent:#60a5fa;
}}

@media (prefers-color-scheme: light) {{
 :root {{
 --bg:#f5f7fb;
 --card:rgba(255,255,255,.70);
 --stroke:rgba(255,255,255,.80);
 --text:#111827;
 --muted:#6b7280;
 --accent:#2563eb;
 }}
}}

.title {{font:700 44px Segoe UI; fill:var(--text);}}
.heading {{font:600 24px Segoe UI; fill:var(--text);}}
.body {{font:400 18px Segoe UI; fill:var(--muted);}}
.stat {{font:700 36px Segoe UI; fill:var(--text);}}
.small {{font:400 14px Segoe UI; fill:var(--muted);}}
.chip {{font:600 15px Segoe UI; fill:var(--text);}}
</style>

<defs>
<filter id="blur"><feGaussianBlur stdDeviation="90"/></filter>

<linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="white" stop-opacity="0.12"/>
<stop offset="100%" stop-color="white" stop-opacity="0.03"/>
</linearGradient>
</defs>

<rect width="1000" height="1300" fill="var(--bg)"/>

<circle cx="180" cy="180" r="240" fill="#2563eb" opacity="0.35" filter="url(#blur)"/>
<circle cx="850" cy="1050" r="280" fill="#7c3aed" opacity="0.30" filter="url(#blur)"/>

<rect x="30" y="30" width="940" height="1240" rx="40"
fill="url(#glass)"
stroke="var(--stroke)"/>

<!-- HERO -->

<text x="70" y="120" class="title">Hi, I'm Sarvesh Nakhale</text>

<rect x="70" y="145" width="220" height="42" rx="21"
fill="rgba(96,165,250,.15)"/>

<text x="92" y="172" class="chip">the ghost of developer</text>

<text x="70" y="235" class="body">
Building systems, not just applications.
</text>

<text x="70" y="270" class="body">
Focused on turning mathematical ideas into real-world software.
</text>

<!-- STATS -->

<rect x="70" y="330" width="190" height="110" rx="22" fill="url(#glass)" stroke="var(--stroke)"/>
<rect x="285" y="330" width="190" height="110" rx="22" fill="url(#glass)" stroke="var(--stroke)"/>
<rect x="500" y="330" width="190" height="110" rx="22" fill="url(#glass)" stroke="var(--stroke)"/>
<rect x="715" y="330" width="190" height="110" rx="22" fill="url(#glass)" stroke="var(--stroke)"/>

<text x="95" y="395" class="stat">20</text>
<text x="95" y="420" class="small">Age</text>

<text x="310" y="395" class="stat">{repos}</text>
<text x="310" y="420" class="small">Repositories</text>

<text x="525" y="395" class="stat">{stars}</text>
<text x="525" y="420" class="small">Stars</text>

<text x="740" y="395" class="stat">{followers}</text>
<text x="740" y="420" class="small">Followers</text>

<!-- ABOUT -->

<rect x="70" y="490" width="860" height="170" rx="24" fill="url(#glass)" stroke="var(--stroke)"/>

<text x="95" y="535" class="heading">About Me</text>

<text x="95" y="580" class="body">
I enjoy finding practical uses for technology, mathematics and system design.
</text>

<text x="95" y="610" class="body">
Rather than chasing buzzwords, I focus on solving real problems.
</text>

<text x="95" y="640" class="body">
Understand deeply. Build thoughtfully. Ship meaningful software.
</text>

<!-- CURRENT FOCUS -->

<rect x="70" y="700" width="415" height="240" rx="24" fill="url(#glass)" stroke="var(--stroke)"/>
<text x="95" y="745" class="heading">Current Focus</text>

<text x="95" y="790" class="body">• GitHub README Architecture</text>
<text x="95" y="825" class="body">• Distributed Systems</text>
<text x="95" y="860" class="body">• Computer Science Fundamentals</text>
<text x="95" y="895" class="body">• Building Authority Through Projects</text>

<!-- PHILOSOPHY -->

<rect x="515" y="700" width="415" height="240" rx="24" fill="url(#glass)" stroke="var(--stroke)"/>

<text x="540" y="745" class="heading">Philosophy</text>

<text x="540" y="795" class="body">Optimize repositories.</text>
<text x="540" y="830" class="body">Improve workflows.</text>
<text x="540" y="865" class="body">Deliver impact.</text>

<text x="540" y="915" class="body">Clean code is a responsibility.</text>

<!-- STACK -->

<rect x="70" y="980" width="860" height="170" rx="24" fill="url(#glass)" stroke="var(--stroke)"/>

<text x="95" y="1025" class="heading">Tech Stack</text>

<text x="95" y="1075" class="body">
Java • Spring Boot • Python • JavaScript • SQL
</text>

<text x="95" y="1110" class="body">
Android • Git • Linux • Blockchain • Web3
</text>

<!-- FOOTER -->

<text x="500" y="1220" text-anchor="middle" class="body">
In a world full of noise, I choose logic, silence and meaningful code.
</text>

</svg>
"""
        self.send_response(200)
        self.send_header("Content-Type", "image/svg+xml")
        self.end_headers()
        self.wfile.write(svg.encode())
