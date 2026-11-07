from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

PROJECTS = [
    ("SORTIFY DESKTOP", "Windows file organiser with smart naming, review and undo workflows.", "Python · Desktop", "https://github.com/hmmlavi/sortify-desktop", "01"),
    ("FACILITYFIX", "Campus issue reporting and resolution management for students and coordinators.", "Flask · Web App", "https://github.com/hmmlavi/FacilityFix", "02"),
    ("PUSTAKALAYA LMS", "Library management for books, members, circulation, reservations and reports.", "Python · Flask", "https://github.com/hmmlavi/Pustakalaya-LMS", "03"),
    ("VEYLO", "A focused space for daily habits, routines and personal progress.", "Web App · Productivity", "https://github.com/hmmlavi/Veylo", "04"),
    ("SABUDDY", "Organise social content ideas, captions, scripts and publishing plans.", "Android · App", "https://github.com/hmmlavi/SaBuddy", "05"),
]


def make_card(project):
    title, description, stack, url, number = project
    title, description, stack = map(escape, (title, description, stack))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="190" viewBox="0 0 440 190" fill="none">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="440" y2="190"><stop stop-color="#F6F8FA"/><stop offset="1" stop-color="#EAEFF4"/></linearGradient>
  <linearGradient id="dark" x1="0" y1="0" x2="440" y2="190"><stop stop-color="#161B22"/><stop offset="1" stop-color="#0D1117"/></linearGradient>
  <style>
    .k{{font:600 10px Arial,sans-serif;letter-spacing:2px;fill:#66717D}}
    .t{{font:700 17px Arial,sans-serif;fill:#17212B}}
    .d{{font:400 12px Arial,sans-serif;fill:#596675}}
    .s{{font:500 10px monospace;fill:#52616F}}
    @media(prefers-color-scheme:dark){{.panel{{fill:url(#dark);stroke:#30363D}}.k{{fill:#8B949E}}.t{{fill:#E6EDF3}}.d{{fill:#AAB4BE}}.s{{fill:#8B949E}}}}
  </style>
</defs>
<rect class="panel" x="1" y="1" width="438" height="188" rx="13" fill="url(#bg)" stroke="#D7DEE6"/>
<text class="k" x="24" y="29">SELECTED PROJECT / {number}</text>
<text class="t" x="24" y="69">{title}</text>
<text class="d" x="24" y="101">{description}</text>
<path d="M24 133H416" stroke="#8996A3" stroke-opacity=".25"/>
<text class="s" x="24" y="158">{stack}</text>
<text class="k" x="416" y="158" text-anchor="end">OPEN REPOSITORY ↗</text>
</svg>'''


def build():
    cards = []
    for project in PROJECTS:
        title, description, stack, url, number = project
        filename = title.lower().replace(" ", "-") + ".svg"
        (ASSETS / filename).write_text(make_card(project), encoding="utf-8")
        cards.append(
            f'<a href="{url}" title="{title}"><img src="./assets/{filename}" '
            f'width="440" alt="{title}: {description}" /></a>'
        )

    project_grid = f"{cards[0]}{cards[1]}<br />{cards[2]}{cards[3]}<br />{cards[4]}"
    readme = f'''<p align="center">
  <img src="./assets/terminal.svg" width="900" alt="Lakshit — CSE student, developer and curious mind" />
</p>

<p align="center">
  <a href="https://github.com/hmmlavi">GitHub</a> ·
  <a href="https://lakshitss.vercel.app/">Portfolio</a> ·
  <a href="https://github.com/hmmlavi?tab=repositories">Repositories</a>
</p>

<p align="center"><img src="./assets/activity.svg" width="400" alt="Explore, build, improve" /></p>

## Selected work

<p align="center">
  {project_grid}
</p>

## A little about me

I'm a Computer Science student from India who enjoys exploring different fields and turning ideas into useful software. I'm interested in **AI, desktop applications, developer tools, web development, and product development** — but I don't want to limit myself to one area.

Outside technology, I'm usually exploring **gaming, space, music, or psychology**. I like learning how things work, why they work, and what I can make from that curiosity.

## Tools I use

<p align="center">
  <img src="./assets/stack-core.svg" width="400" alt="Core stack" />
  <img src="./assets/stack-more.svg" width="400" alt="Tools and platforms" />
</p>

## What I'm exploring

<p align="center"><img src="./assets/learning.svg" width="400" alt="Current learning interests" /></p>

---

<p align="center"><sub>Still exploring. Still building. Always curious.</sub></p>
'''
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print("README.md and project cards generated.")


if __name__ == "__main__":
    build()
