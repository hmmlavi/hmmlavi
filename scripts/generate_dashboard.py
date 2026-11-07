import json
import os
import urllib.request
import xml.sax.saxutils as xml
from datetime import datetime, timezone

USER = "hmmlavi"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"

def api(path):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "hmmlavi-profile-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = urllib.request.Request(API + path, headers=headers)
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.load(response)

def esc(value):
    return xml.escape(str(value))

def short_date(value):
    if not value:
        return "—"
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        days = max(0, (datetime.now(timezone.utc) - dt).days)
        if days == 0:
            return "today"
        if days == 1:
            return "1d ago"
        if days < 30:
            return f"{days}d ago"
        return f"{days // 30}mo ago"
    except (TypeError, ValueError):
        return "—"

repos = []
for page in range(1, 6):
    batch = api(f"/users/{USER}/repos?type=owner&sort=pushed&per_page=100&page={page}")
    repos.extend(batch)
    if len(batch) < 100:
        break

owned = [r for r in repos if not r.get("fork") and not r.get("archived")]
stars = sum(r.get("stargazers_count", 0) for r in owned)
forks = sum(r.get("forks_count", 0) for r in owned)
recent = sorted(owned, key=lambda r: r.get("pushed_at") or "", reverse=True)[:3]

language_totals = {}
for repo in owned[:60]:
    try:
        for language, amount in api(f"/repos/{USER}/{repo['name']}/languages").items():
            language_totals[language] = language_totals.get(language, 0) + amount
    except Exception:
        continue

languages = sorted(language_totals.items(), key=lambda item: item[1], reverse=True)[:5]
language_total = sum(value for _, value in languages) or 1
palette = ["#C4B5FD", "#A78BFA", "#8B9CF6", "#79C7C5", "#E6A5C8"]
segments = []
labels = []
x = 64
bar_width = 1072
for index, (name, amount) in enumerate(languages):
    width = bar_width * amount / language_total
    segments.append(f'<rect x="{x:.1f}" y="292" width="{max(1, width):.1f}" height="12" rx="6" fill="{palette[index]}"/>')
    percent = amount * 100 / language_total
    labels.append(
        f'<circle cx="{x + 4:.1f}" cy="335" r="4" fill="{palette[index]}"/>'
        f'<text x="{x + 15:.1f}" y="339" class="lang">{esc(name)}</text>'
        f'<text x="{x + 15:.1f}" y="360" class="pct">{percent:.1f}%</text>'
    )
    x += width

if not languages:
    segments = ['<rect x="64" y="292" width="1072" height="12" rx="6" fill="#303342"/>']
    labels = ['<text x="64" y="339" class="lang">Language data unavailable</text>']

recent_rows = []
for index, repo in enumerate(recent):
    y = 421 + index * 27
    name = repo.get("name", "Untitled")
    if len(name) > 32:
        name = name[:29] + "..."
    recent_rows.append(
        f'<text x="64" y="{y}" class="repo">{esc(name)}</text>'
        f'<text x="1136" y="{y}" text-anchor="end" class="date">{short_date(repo.get("pushed_at"))}</text>'
    )
if not recent_rows:
    recent_rows = ['<text x="64" y="421" class="repo">No public project activity yet</text>']

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="520" viewBox="0 0 1200 520">
<defs>
  <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#C4B5FD" stop-opacity=".18"/>
    <stop offset="1" stop-color="#79C7C5" stop-opacity=".04"/>
  </linearGradient>
  <style>
    text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
    .muted {{ fill:#8B91A3; font-size:12px; letter-spacing:1.5px; }}
    .heading {{ fill:#F3F1FA; font-size:22px; font-weight:650; }}
    .number {{ fill:#F7F5FF; font-size:34px; font-weight:650; }}
    .metric {{ fill:#A6A9B8; font-size:11px; letter-spacing:1.2px; }}
    .lang {{ fill:#DAD7E8; font-size:13px; }}
    .pct {{ fill:#8B91A3; font-size:11px; }}
    .repo {{ fill:#E8E5F1; font-size:13px; }}
    .date {{ fill:#9297A8; font-size:12px; }}
  </style>
</defs>
<rect x="1" y="1" width="1198" height="518" rx="18" fill="#070910" stroke="#292D3A"/>
<rect x="2" y="2" width="1196" height="112" rx="17" fill="url(#glow)"/>
<text x="64" y="48" class="muted">HMMLAVI  /  DEVELOPER OVERVIEW</text>
<text x="64" y="82" class="heading">A little signal from what I build.</text>
<circle cx="1110" cy="49" r="4" fill="#79C7C5"/>
<text x="1125" y="53" text-anchor="end" class="muted">PUBLIC DATA</text>
<g>
  <rect x="64" y="130" width="338" height="112" rx="12" fill="#10131D" stroke="#292D3A"/>
  <rect x="431" y="130" width="338" height="112" rx="12" fill="#10131D" stroke="#292D3A"/>
  <rect x="798" y="130" width="338" height="112" rx="12" fill="#10131D" stroke="#292D3A"/>
  <text x="88" y="166" class="metric">ORIGINAL REPOSITORIES</text>
  <text x="88" y="215" class="number">{len(owned)}</text>
  <text x="455" y="166" class="metric">STARS EARNED</text>
  <text x="455" y="215" class="number">{stars}</text>
  <text x="822" y="166" class="metric">COMMUNITY FORKS</text>
  <text x="822" y="215" class="number">{forks}</text>
</g>
<text x="64" y="273" class="muted">LANGUAGE FINGERPRINT</text>
{''.join(segments)}
{''.join(labels)}
<line x1="64" y1="386" x2="1136" y2="386" stroke="#292D3A"/>
<text x="64" y="409" class="muted">RECENTLY TOUCHED</text>
{''.join(recent_rows)}
<text x="1136" y="498" text-anchor="end" class="muted">AUTO-REFRESHED DAILY  ·  GITHUB API</text>
</svg>'''

os.makedirs("profile", exist_ok=True)
with open("profile/dashboard.svg", "w", encoding="utf-8") as output:
    output.write(svg)
print(f"Generated dashboard for {USER}: {len(owned)} repositories, {stars} stars, {forks} forks.")
