# ⚽ Match Corna Live — Facebook Football Bot

Auto-posts live football updates to your Facebook page. **100% free** — no paid APIs. Present and future only — no historical "flashback" content.

## What gets posted
| Event | Example |
|-------|---------|
| 📋 Lineup | Starting XI ~1hr before KO (when available) for every game |
| ▶️ Kick-off | Stylish scoreboard card — team hex badges + KICK-OFF ribbon |
| ⚽ Goal | Scorer, minute, live score — name drawn under the scoring team's own crest |
| 🟥 Red card | Player + minute, posted the moment it's detected |
| ⏸️ Half time | Current score + scorers/assists so far |
| ⏱️ Extra time | Notifies when ET starts (knockout matches) |
| 🏁 Full time | Final score + all goals, each team's scorers under their own crest. AET/Penalties clearly labelled |
| 📅 Daily preview | Morning fixture list (9AM UTC) |

**Not posted:** cancelled/postponed games, or anything historical (old scores, past-season stats). No transfer/gossip news of any kind — this bot only covers live ESPN + SofaScore match data.

## Coverage
- **Club**: EPL, Bundesliga, La Liga, Serie A, Ligue 1, UCL, UEL, UECL, FA Cup + more (ESPN), plus anything SofaScore covers that ESPN doesn't (e.g. Malawi's FDH Bank Super League, regional cups, qualifiers)
- **International**: **ALL** country vs country games detected automatically — WC Qualifiers, AFCON, Nations League, Copa America, Friendlies, any FIFA series

## Card design
All cards are rendered with Pillow — no generative image model in the loop, so nothing can misspell a name or draw a wrong flag/crest.

- **Stadium backdrop**: floodlight beam fans from both top corners over a dark vignette + blurred pitch texture.
- **Hexagon team badges**: crests/flags sit in a light-bordered hex frame (falls back to a colored hex initials badge if a crest can't be fetched) instead of a plain circle.
- **Ribbon/chevron banners**: scorelines and status labels (`KICK-OFF`, `72' - LIVE`, `FULL TIME`) are drawn as pointed-end ribbon badges rather than flat rounded pills.
- **Side-anchored scorer/assist text**: goal and full-time scorer names are drawn under the *scoring team's own crest* rather than centered across the card, so it's immediately clear whose event it is.

## Data source
ESPN (primary — richer lineup/VAR support) + SofaScore (fills in matches ESPN's fixed league whitelist misses — qualifiers, cups, Malawi Super League, etc). No API keys, no paid tiers, 100% free.

## Files
```
bot.py          ← Run this
scraper.py      ← ESPN data layer + merges in SofaScore
sofascore.py    ← SofaScore data layer (2nd source)
poster.py       ← Facebook API + message formatters
graphics.py     ← Branded card rendering (Pillow)
config.py       ← All settings via env vars
requirements.txt
state_v2.json   ← Auto-created, tracks posted events
```

## Local run
```bash
pip install -r requirements.txt
python bot.py
# Without FB_PAGE_ID set, posts print to console instead
```

| Variable | Value |
|----------|-------|
| `FB_PAGE_ID` | Your Facebook Page ID |
| `FB_PAGE_ACCESS_TOKEN` | Your long-lived Page Access Token |
| `POLL_INTERVAL` | `60` |
| `POST_LINEUPS` | `true` |
| `LINEUP_LEAD_MINUTES` | `65` |
| `POST_KICKOFF` | `true` |
| `POST_GOALS` | `true` |
| `POST_RED_CARDS` | `true` |
| `POST_HALFTIME` | `true` |
| `POST_FULLTIME` | `true` |
| `POST_DAILY_PREVIEW` | `true` |
| `DAILY_PREVIEW_HOUR` | `9` |
| `MIN_POST_GAP` | `20` |
| `MAX_POSTS_PER_HOUR` | `25` |
| `MAX_EVENT_AGE_MINUTES` | `15` |

Start command: `python bot.py`

The bot binds an HTTP server to Railway's `PORT` automatically — no sleep issues.

## Adding leagues
Edit `ESPN_CLUB_LEAGUES` in `scraper.py` for ESPN-covered leagues, and `PRIORITY_TOURNAMENTS` / `SECONDARY_TOURNAMENTS` / `ALWAYS_INCLUDE_COUNTRIES` in `sofascore.py` for SofaScore-covered ones. Find ESPN slugs at `site.api.espn.com/apis/site/v2/sports/soccer/{slug}/scoreboard`.
International games need no changes — all country vs country is auto-included for live scores.
