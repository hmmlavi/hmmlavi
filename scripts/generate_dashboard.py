import json
import os
import urllib.parse
import urllib.request
import xml.sax.saxutils as xml
from datetime import datetime, timezone

USER = "hmmlavi"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"

def request_json(url, method="GET", payload=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "hmmlavi-profile-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)

def api(path):
    return request_json(API + path)

def esc(value):
    return xml.escape(str(value))

def get_contributions():
    now = datetime.now(timezone.utc)
    start = now.replace(year=now.year - 1).strftime("%Y-%m-%dT00:00:00Z")
    end = now.strftime("%Y-%m-%dT23:59:59Z")
    query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar { totalContributions }
        }
      }
    }
    """
    try:
        result = request_json(
            "https://api.github.com/graphql",
            method="POST",
            payload={"query": query, "variables": {"login": USER, "from": start, "to": end}},
        )
        return result["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    except Exception as error:
        print(f"Contribution count unavailable: {error}")
        return 0

repos = []
for page in range(1, 6):
    batch = api(f"/users/{USER}/repos?type=owner&sort=pushed&per_page=100&page={page}")
    repos.extend(batch)
    if len(batch) < 100:
        break

public_repos = [repo for repo in repos if not repo.get("private", False)]
stars = sum(repo.get("stargazers_count", 0) for repo in public_repos)
contributions = get_contributions()

merged_query = urllib.parse.quote(f"author:{USER} is:pr is:merged")
merged_prs = api(f"/search/issues?q={merged_query}&per_page=1").get("total_count", 0)

language_totals = {}
for repo in public_repos[:100]:
    try:
        for language, amount in api(f"/repos/{USER}/{repo['name']}/languages").items():
            language_totals[language] = language_totals.get(language, 0) + amount
    except Exception as error:
        print(f"Skipping language data for {repo.get('name')}: {error}")

languages = sorted(language_totals.items(), key=lambda item: item[1], reverse=True)[:5]
language_total = sum(value for _, value in languages) or 1
palette = ["#C4B5FD", "#A78BFA", "#8B9CF6", "#79C7C5", "#E6A5C8"]
segments = []
labels = []
x = 64
bar_width = 1072

for index, (name, amount) in enumerate(languages):
    width = bar_width * amount / language_total
    segments.append(
        f'<rect x="{x:.1f}" y="326" width="{max(1, width):.1f}" height="12" rx="6" fill="{palette[index]}"/>'
    )
    percent = amount * 100 / language_total
    labels.append(
        f'<circle cx="{x + 4:.1f}" cy="369" r="4" fill="{palette[index]}"/>'
        f'<text x="{x + 15:.1f}" y="373" class="lang">{esc(name)}</text>'
        f'<text x="{x + 15:.1f}" y="394" class="pct">{percent:.1f}%</text>'
    )
    x += width

if not languages:
    segments = ['<rect x="64" y="326" width="1072" height="12" rx="6" fill="#303342"/>']
    labels = ['<text x="64" y="373" class="lang">Language data unavailable</text>']

metrics = [
    ("PUBLIC REPOSITORIES", len(public_repos)),
    ("CONTRIBUTIONS · 1 YEAR", contributions),
    ("STARS EARNED", stars),
    ("MERGED PULL REQUESTS", merged_prs),
]
card_x = [64, 338, 612, 886]
cards = []
for (label, value), x_pos in zip(metrics, card_x):
    cards.append(
        f'<rect x="{x_pos}" y="130" width="250" height="112" rx="12" fill="#10131D" stroke="#292D3A"/>'
        f'<text x="{x_pos + 22}" y="166" class="metric">{esc(label)}</text>'
        f'<text x="{x_pos + 22}" y="215" class="number">{value:,}</text>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440">
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
    .metric {{ fill:#A6A9B8; font-size:10px; letter-spacing:1px; }}
    .lang {{ fill:#DAD7E8; font-size:13px; }}
    .pct {{ fill:#8B91A3; font-size:11px; }}
  </style>
</defs>
<rect x="1" y="1" width="1198" height="438" rx="18" fill="#070910" stroke="#292D3A"/>
<rect x="2" y="2" width="1196" height="112" rx="17" fill="url(#glow)"/>
<text x="64" y="48" class="muted">HMMLAVI  /  DEVELOPER OVERVIEW</text>
<text x="64" y="82" class="heading">A little signal from what I build.</text>
<circle cx="1110" cy="49" r="4" fill="#79C7C5"/>
<text x="1125" y="53" text-anchor="end" class="muted">PUBLIC DATA</text>
<g>{''.join(cards)}</g>
<text x="64" y="294" class="muted">LANGUAGE FINGERPRINT</text>
{''.join(segments)}
{''.join(labels)}
<text x="1136" y="414" text-anchor="end" class="muted">AUTO-REFRESHED DAILY  ·  GITHUB API</text>
</svg>'''

os.makedirs("profile", exist_ok=True)
with open("profile/dashboard.svg", "w", encoding="utf-8") as output:
    output.write(svg)

print(
    f"Generated dashboard for {USER}: {len(public_repos)} public repositories, "
    f"{contributions} contributions (last year), {stars} stars, {merged_prs} merged PRs."
)
