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
                "status": "Online"
            }
    except Exception:
        return {"repos": "?", "followers": "?", "status": "API Limit/Offline"}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        stats = get_github_stats("Sarvesh2005-code")
        
        # We split the URLs here so your rich-text editor doesn't accidentally format them!
        w3_namespace = "http://" + "www.w3.org/2000/svg"
        my_website = "https://" + "sarvy.vercel.app/"
        
        ascii_art_lines = [
            r"       g@M%@%%@N%Nw,,",
            r"     ,M*|`||*%gNM=]mM%g||%N,",
            r"     p!``  `! |``` ```|||jhlj%w",
            r"   ,@L     ,,       ```!`|j%M]%M",
            r"  ]j`` .,wp@pw,     `    ````|%Wg",
            r"/{||]@@@@@@@@@@pp.           |||||",
            r"` ' ]@@@@@@@@@@@@@p     ,  ,```",
            r"  :]%@@@@@%%%%%%k%h  '*||mkr    *",
            r"  j%M`      |jkk'  ~nrn=|i    ;`",
            r"!  jrr*^`           `\"! L'':!",
            r" j  lp;,.  ,/ @@    ,;\nmy  \" ,~",
            r" i r @@@@mmHM @@@@ `^****M*,p ;,",
            r" | ]@@@HHH]g@M%%%%%H,jmgpmb%  j",
            r" ;;;%%%%%%k%@[,.n|;.;j%%k|k%%',[",
            r"  H|%%k%%%j%k||,;;j;!!'|%ij}}]@",
            r"  \"djjmkL,\"]]][,,,,wwxw;|#kjk`",
            r"    %;%km%%%%M%M|%%jkkii|||[",
            r"     kjj%kkkl!|||||||j|||\"",
            r"      |jm%H@@@b%%kkmk%i|!,[",
            r"       @p|j%%%%jkk|||j*``;j[",
            r"       ]@@@g|```````   ,,;j%k",
            r"       @@@@@mgmp;,,,,:;jj%%k%",
            r"      @@@@@@@@@%%kgki!|jjjj%k%@ .",
            r" ^['' %@@@HH%b%k{illljkjj%%% ; `,.",
            r"=['` . %HH%%%%%H@gkilljjj%kk%\".  `'i"
        ]

        tspan_blocks = ""
        y_pos = 40
        for line in ascii_art_lines:
            clean_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            tspan_blocks += f'<tspan x="20" y="{y_pos}">{clean_line}</tspan>\n          '
            y_pos += 14  

        svg_content = f"""
        <svg width="850" height="420" xmlns="{w3_namespace}">
          <style>
            .text {{ font-family: 'Courier New', Courier, monospace; font-size: 13px; fill: #C9D1D9; }}
            .ascii {{ font-family: 'Courier New', Courier, monospace; font-size: 11px; fill: #58A6FF; }}
            .blue {{ fill: #58A6FF; }}
            .green {{ fill: #7EE787; }}
            .orange {{ fill: #FF9D00; }}
            .grey {{ fill: #8B949E; }}
          </style>
          <rect width="850" height="420" rx="10" fill="#0D1117" stroke="#30363D" stroke-width="1"/>
          
          <text class="ascii" xml:space="preserve">
          {tspan_blocks}
          </text>

          <text x="320" y="50" class="text" xml:space="preserve"><tspan class="blue">Sarvesh</tspan>@<tspan class="blue">Developer</tspan> <tspan class="grey">--------------------------------</tspan></text>
          
          <text x="320" y="80" class="text" xml:space="preserve">. <tspan class="orange">OS:</tspan> .......................... Windows 11, Kali Linux</text>
          <text x="320" y="100" class="text" xml:space="preserve">. <tspan class="orange">Uptime:</tspan> .................................... 20 years</text>
          <text x="320" y="120" class="text" xml:space="preserve">. <tspan class="orange">IDE:</tspan> ............................... Eclipse, VS Code</text>
          
          <text x="320" y="160" class="text" xml:space="preserve">. <tspan class="orange">Languages.Programming:</tspan> ......................... Java</text>
          <text x="320" y="180" class="text" xml:space="preserve">. <tspan class="orange">Languages.Computer:</tspan> ....... HTML, CSS, JS, SQL, JSON</text>
          
          <text x="320" y="220" class="text" xml:space="preserve">. <tspan class="orange">Hobbies.Software:</tspan> .... Backend Architecture, Spring Boot</text>
          <text x="320" y="240" class="text" xml:space="preserve">. <tspan class="orange">Hobbies.Security:</tspan> ........ NIST Frameworks, Custom Firewalls</text>

          <text x="320" y="280" class="text" xml:space="preserve"><tspan class="grey">- Contact ------------------------------------------</tspan></text>
          <text x="320" y="310" class="text" xml:space="preserve">. <tspan class="orange">Email:</tspan> ..................... sarveshnakhale21@gmail.com</text>
          <text x="320" y="330" class="text" xml:space="preserve">. <tspan class="orange">Website:</tspan> ...................... {my_website}</text>
          <text x="320" y="350" class="text" xml:space="preserve">. <tspan class="orange">LinkedIn:</tspan> ............................. in/sarveshnakhale</text>
          <text x="320" y="370" class="text" xml:space="preserve">. <tspan class="orange">X:</tspan> .......................................... @Sarvyx2005</text>

          <text x="320" y="410" class="text" xml:space="preserve"><tspan class="grey">- GitHub Stats [{stats['status']}] ------------------------</tspan></text>
          <text x="320" y="440" class="text" xml:space="preserve">. <tspan class="orange">Repos:</tspan> .... <tspan class="green">{stats['repos']}</tspan> | <tspan class="orange">Followers:</tspan> ....... <tspan class="green">{stats['followers']}</tspan></text>
        </svg>
        """

        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.send_header('Cache-Control', 's-maxage=3600, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(svg_content.encode('utf-8'))
