from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

TERMINAL_SVG = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="900" viewBox="0 0 1000 900" role="img" aria-labelledby="title desc">
<title id="title">Hi, I'm Lakshit Singh</title>
<desc id="desc">A terminal-style introduction and about section.</desc>
<defs>
  <linearGradient id="lightBg" x1="0" y1="0" x2="1000" y2="900"><stop stop-color="#F8FAFC"/><stop offset="1" stop-color="#E9EEF4"/></linearGradient>
  <linearGradient id="darkBg" x1="0" y1="0" x2="1000" y2="900"><stop stop-color="#161B22"/><stop offset="1" stop-color="#0D1117"/></linearGradient>
  <style>
    text { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; }
    .window { fill: url(#lightBg); stroke: #D0D7DE; }
    .bar { fill: #E8EDF2; }
    .main { fill: #17212B; }
    .muted { fill: #657383; }
    .green { fill: #16845B; }
    .blue { fill: #2766A5; }
    .line { stroke: #D0D7DE; }
    .title { font-size: 34px; font-weight: 700; letter-spacing: -.8px; }
    .body { font-size: 15px; }
    .prompt { font-size: 15px; font-weight: 700; }
    @media(prefers-color-scheme:dark) {
      .window { fill: url(#darkBg); stroke: #30363D; }
      .bar { fill: #21262D; }
      .main { fill: #E6EDF3; }
      .muted { fill: #9AA7B4; }
      .green { fill: #3FB98A; }
      .blue { fill: #79B8FF; }
      .line { stroke: #30363D; }
    }
  </style>
</defs>
<rect class="window" x="1" y="1" width="998" height="898" rx="18"/>
<path class="bar" d="M19 1H981a18 18 0 0 1 18 18v48H1V19A18 18 0 0 1 19 1Z"/>
<circle cx="31" cy="34" r="7" fill="#FF6B6B"/><circle cx="56" cy="34" r="7" fill="#F5C451"/><circle cx="81" cy="34" r="7" fill="#45B982"/>
<text class="muted" x="500" y="39" text-anchor="middle" font-size="13">lakshit@github: ~/profile</text>
<text class="green prompt" x="52" y="112">$ whoami</text>
<text class="main title" x="52" y="163">Hi, I'm Lakshit Singh :)</text>
<path class="line" d="M52 205H948"/>
<text class="green prompt" x="52" y="250">$ cat about.txt</text>
<text class="main body" x="52" y="294">I'm a Computer Science student from India who loves building things and exploring what technology can do.</text>
<text class="main body" x="52" y="322">I often find myself going down rabbit holes, experimenting with new ideas, or starting a project</text>
<text class="main body" x="52" y="350">just because something caught my attention.</text>
<text class="main body" x="52" y="398">I'm interested in a lot of things, especially AI, desktop applications, developer tools, web development,</text>
<text class="main body" x="52" y="426">and product development. I don't really want to limit myself to one field. There's always something new</text>
<text class="main body" x="52" y="454">to explore, something different to learn, or a better way to build something.</text>
<text class="main body" x="52" y="502">What excites me most is taking an idea that exists only in my head and slowly turning it into something</text>
<text class="main body" x="52" y="530">real. I enjoy every part of that process, from figuring out what to build and how it should work to</text>
<text class="main body" x="52" y="558">writing the code and seeing everything come together.</text>
<text class="main body" x="52" y="606">And it's not always about technology. I spend my time exploring gaming, space, music, and psychology,</text>
<text class="main body" x="52" y="634">too. I like learning about things that make me curious, even when they have nothing to do with what</text>
<text class="main body" x="52" y="662">I'm building.</text>
<text class="main body" x="52" y="710">I have plenty of ideas I'd love to bring to life. Someday, I want to build products that people around</text>
<text class="main body" x="52" y="738">the world genuinely enjoy using. Until then, you'll probably find me working on something new,</text>
<text class="main body" x="52" y="766">experimenting with an idea, or getting curious about something completely different.</text>
<path class="line" d="M52 818H948"/>
<text class="blue" x="52" y="856" font-size="13">END OF ABOUT SECTION</text>
</svg>'''

README = """<p align="center">
  <img src="./assets/terminal.svg" width="100%" alt="Hi, I'm Lakshit Singh — introduction and about section" />
</p>

<h2 align="center">Projects</h2>
<p align="center">A few things I've been building.</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Sortify Desktop</h3>
      <p>A Windows desktop app that scans file contents, suggests meaningful names, and helps organise files with review and undo controls.</p>
    </td>
    <td width="50%" valign="top">
      <h3>FacilityFix</h3>
      <p>A campus issue reporting system for students and coordinators to report, review, track, and resolve facility problems.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Pustakalaya LMS</h3>
      <p>A local-first library management system covering books, copies, members, circulation, reservations, fines, and reports.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Veylo</h3>
      <p>A habit tracker for organising daily routines, planning, and keeping an eye on progress over time.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <h3>SaBuddy</h3>
      <p>An Android social media content planner for ideas, captions, scripts, calendar planning, and saved content, with optional Gemini support.</p>
    </td>
  </tr>
</table>

<h2 align="center">Tools of Trade</h2>
<p align="center">The technologies and tools I use to bring ideas to life.</p>

<h3 align="center">Languages</h3>
<p align="center">
  <img src="https://skillicons.dev/icons?i=python,c,cpp,js,ts,html,css,bash" alt="Python, C, C++, JavaScript, TypeScript, HTML, CSS, Bash" />
</p>

<h3 align="center">Frameworks &amp; UI</h3>
<p align="center">
  <img src="https://skillicons.dev/icons?i=react,nextjs,tailwind,nodejs,express,flask" alt="React, Next.js, Tailwind CSS, Node.js, Express, Flask" />
</p>

<h3 align="center">AI &amp; Machine Learning</h3>
<p align="center">
  <img src="https://skillicons.dev/icons?i=openai,claude,gemini" alt="OpenAI, Claude, Gemini" />
</p>
<p align="center">LangChain · Codex · Gemini</p>

<h3 align="center">Databases</h3>
<p align="center">
  <img src="https://skillicons.dev/icons?i=postgres,sqlite,mongodb,supabase,firebase" alt="PostgreSQL, SQLite, MongoDB, Supabase, Firebase" />
</p>

<h3 align="center">Tools &amp; Platforms</h3>
<p align="center">
  <img src="https://skillicons.dev/icons?i=git,github,vercel,figma,vscode,npm,powershell" alt="Git, GitHub, GitHub Pages, Vercel, Figma, VS Code, npm, PowerShell" />
</p>

<p align="center">Still exploring. Still building. Always curious.</p>
"""

def build():
    (ASSETS / "terminal.svg").write_text(TERMINAL_SVG, encoding="utf-8")
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    print("Generated the terminal intro, projects, and tools sections.")

if __name__ == "__main__":
    build()
