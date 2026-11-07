from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

PROJECTS = [
    ("SORTIFY DESKTOP", "Windows file organiser with smart naming, review and undo workflows.", "github.com/hmmlavi/sortify-desktop"),
    ("FACILITYFIX", "Campus issue reporting and resolution management.", "github.com/hmmlavi/FacilityFix"),
    ("PUSTAKALAYA LMS", "Library management for books, members, circulation and reports.", "github.com/hmmlavi/Pustakalaya-LMS"),
    ("VEYLO", "A focused space for daily habits, routines and personal progress.", "github.com/hmmlavi/Veylo"),
    ("SABUDDY", "Organise social content ideas, captions, scripts and plans.", "github.com/hmmlavi/SaBuddy"),
]


def terminal_svg():
    project_rows = []
    y = 570
    for name, description, url in PROJECTS:
        project_rows.append(
            f'<text class="project" x="76" y="{y}">{escape(name)}</text>'
            f'<text class="muted desc" x="300" y="{y}">{escape(description)}</text>'
            f'<text class="link" x="76" y="{y + 25}">{escape(url)}</text>'
        )
        y += 76

    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1120" viewBox="0 0 1000 1120" role="img" aria-labelledby="title desc">
<title id="title">Lakshit Singh Saini — Developer profile</title>
<desc id="desc">A terminal-style profile with about, selected projects, tools, interests and links.</desc>
<defs>
  <linearGradient id="lightBg" x1="0" y1="0" x2="1000" y2="1120"><stop stop-color="#F8FAFC"/><stop offset="1" stop-color="#E9EEF4"/></linearGradient>
  <linearGradient id="darkBg" x1="0" y1="0" x2="1000" y2="1120"><stop stop-color="#161B22"/><stop offset="1" stop-color="#0D1117"/></linearGradient>
  <style>
    text { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; }
    .window { fill: url(#lightBg); stroke: #D0D7DE; }
    .bar { fill: #E8EDF2; }
    .main { fill: #17212B; }
    .muted { fill: #657383; }
    .green { fill: #16845B; }
    .blue { fill: #2766A5; }
    .purple { fill: #8256B3; }
    .line { stroke: #D0D7DE; }
    .title { font-size: 31px; font-weight: 700; letter-spacing: -.8px; }
    .subtitle { font-size: 15px; }
    .body { font-size: 15px; }
    .project { font-size: 14px; font-weight: 700; }
    .desc { font-size: 12px; }
    .link { font-size: 11px; }
    .chip { font-size: 13px; }
    .prompt { font-size: 14px; font-weight: 700; }
    @media(prefers-color-scheme:dark) {
      .window { fill: url(#darkBg); stroke: #30363D; }
      .bar { fill: #21262D; }
      .main { fill: #E6EDF3; }
      .muted { fill: #9AA7B4; }
      .green { fill: #3FB98A; }
      .blue { fill: #79B8FF; }
      .purple { fill: #D2A8FF; }
      .line { stroke: #30363D; }
    }
  </style>
</defs>
<rect class="window" x="1" y="1" width="998" height="1118" rx="18"/>
<path class="bar" d="M19 1H981a18 18 0 0 1 18 18v48H1V19A18 18 0 0 1 19 1Z"/>
<circle cx="31" cy="34" r="7" fill="#FF6B6B"/><circle cx="56" cy="34" r="7" fill="#F5C451"/><circle cx="81" cy="34" r="7" fill="#45B982"/>
<text class="muted" x="500" y="39" text-anchor="middle" font-size="13">lakshit@github: ~/profile</text>

<text class="green prompt" x="52" y="111">$ whoami</text>
<text class="main title" x="52" y="157">Lakshit Singh Saini</text>
<text class="blue subtitle" x="52" y="188">Computer Science student · Developer · Curious mind</text>
<text class="muted body" x="52" y="225">India — exploring ideas, building useful software, and learning how things work.</text>

<path class="line" d="M52 252H948"/>
<text class="green prompt" x="52" y="286">$ cat about.txt</text>
<text class="main body" x="52" y="321">I enjoy exploring different fields and turning ideas into useful software.</text>
<text class="main body" x="52" y="348">Interested in AI, desktop applications, developer tools, web development,</text>
<text class="main body" x="52" y="375">and product development — without limiting myself to one area.</text>
<text class="muted body" x="52" y="414">Beyond tech: gaming, space, music, psychology, and whatever sparks curiosity.</text>

<path class="line" d="M52 443H948"/>
<text class="green prompt" x="52" y="478">$ ls ./selected-work</text>
\__PROJECT_ROWS__

<path class="line" d="M52 968H948"/>
<text class="green prompt" x="52" y="1001">$ cat toolkit.txt</text>
<text class="main chip" x="52" y="1032">Python · C · C++ · TypeScript · React · Next.js · Tailwind · Node.js · Express</text>
<text class="main chip" x="52" y="1057">PostgreSQL · SQLite · MongoDB · Supabase · Firebase · Git · GitHub · Vercel · Figma</text>
<text class="purple chip" x="52" y="1082">Exploring: AI engineering · systems programming · DSA · system design</text>
</svg>'''.replace("__PROJECT_ROWS__", "\n".join(project_rows))


def build():
    (ASSETS / "terminal.svg").write_text(terminal_svg(), encoding="utf-8")
    readme = '''<p align="center">
  <img src="./assets/terminal.svg" width="100%" alt="Lakshit Singh Saini — developer profile, selected work, tools and interests" />
</p>

<p align="center">
  <a href="https://github.com/hmmlavi">GitHub</a> ·
  <a href="https://lakshitss.vercel.app/">Portfolio</a> ·
  <a href="https://github.com/hmmlavi?tab=repositories">Repositories</a>
</p>
'''
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print("Generated the complete terminal-style profile README.")


if __name__ == "__main__":
    build()
