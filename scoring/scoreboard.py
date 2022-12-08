import datetime
import json
import os.path
import sys
from collections import defaultdict, Counter

from tabulate import tabulate

import requests

# Ja, der Code von den Tagesaufgaben ist oft schon nicht schön, aber _dieser_ Code ist nochmal ne Nummer schlimmer.
# Ist halt so gewachsen...
path = os.path.join(sys.path[0], 'session_cookie')
if not os.path.isfile(path):
    print("Please provide a session_cookie file next to the script to be able to access the private leaderboard.")
    print("The session_cookie is set by the Advent of Code website, can be retrieved via the browser and should be 96 random hexadecimal chars.")
    sys.exit()

year = 2022
try:
    json_data = requests.get(f"https://adventofcode.com/{year}/leaderboard/private/view/486446.json", cookies={"session": open(path).read().strip()}).json()
except json.decoder.JSONDecodeError:
    print("Your session_cookie seems to be invalid, please double-check.")
    sys.exit()

today = datetime.datetime.now().day if len(sys.argv) == 1 else int(sys.argv[1])
today = min(25, max(1, today))
scores = {}
num_users = len(json_data["members"])
print(f"Day {today} results")
print("")

name_mapping = Counter([member["name"] for member in json_data["members"].values() if member["name"]])
name_mapping = {member["id"]: (member["name"] or f'anon # {member["id"]}') if name_mapping[member["name"]] <= 1 else f'{member["name"]} {member["id"]}' for member in json_data["members"].values()}

yesterday_scores = None
stars = defaultdict(lambda: 0)
for day in range(1, today + 1):
    solutions = []
    if day == today:
        yesterday_scores = scores.copy()
    for member in json_data["members"].values():
        if "completion_day_level" in member:
            if str(day) in member["completion_day_level"]:
                solutions.append({"member": name_mapping[member["id"]], **member["completion_day_level"][str(day)]})

    start = datetime.datetime(year, 12, day, 6, 00)

    if day == today:
        print("first star solution times")
    sols = sorted(solutions, key=lambda x: x.get('1', {}).get('get_star_ts', 99999999999999))
    o = 0
    for sol in sols:
        if '1' not in sol:
            continue
        o += 1
        stars[sol['member']] += 1
        scores[sol['member']] = scores.get(sol['member'], 0) + (num_users - o + 1)
        if day == today:
            print(f"{o}. {sol['member']} - {datetime.datetime.fromtimestamp(sol['1']['get_star_ts']) - start}")

    if day == today:
        print("")
        print("second star solution times")
    sols = sorted(solutions, key=lambda x: x.get('2', {}).get('get_star_ts', 99999999999999))
    o = 0
    for sol in sols:
        if '2' not in sol:
            continue
        o += 1
        stars[sol['member']] += 1
        scores[sol['member']] = scores.get(sol['member'], 0) + (num_users - o + 1)
        if day == today:
            print(f"{o}. {sol['member']} - {datetime.datetime.fromtimestamp(sol['2']['get_star_ts']) - start}")

    if day == today:
        print("")
        print("second star solution offset")
    sols = sorted(solutions, key=lambda x: x.get('2', {}).get('get_star_ts', 99999999999999) - x.get('1', {}).get('get_star_ts', 99999999999999))
    o = 0
    for sol in sols:
        if '2' not in sol:
            continue
        o += 1
        if day == today:
            print(f"{o}. {sol['member']} - {datetime.datetime.fromtimestamp(sol['2']['get_star_ts']) - datetime.datetime.fromtimestamp(sol['1']['get_star_ts'])}")

yesterday_scores = {user: (position + 1, score) for position, (user, score) in enumerate(sorted(yesterday_scores.items(), key=lambda x: x[1], reverse=True))}

print("")
print(f"Overall Scores after {today} days ({num_users} players, {len(scores)} non-zero)")
o = 0

table_data = []
for user, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    o += 1
    yesterday_pos, yesterday_score = yesterday_scores[user] if yesterday_scores else (1, 0)
    position_change = yesterday_pos - o
    position_change_str = "=0" if position_change == 0 else (f"+{position_change}" if position_change > 0 else position_change)
    missing_stars = today * 2 - stars[user]
    missing_stars_str = f"({missing_stars} part(s) missing)" if missing_stars else ""
    expected_stars = (num_users - (yesterday_pos - 1)) * 2
    actual_stars = score - yesterday_score
    relative_star = actual_stars - expected_stars
    relative_star_str = "=0" if relative_star == 0 else (f"+{relative_star}" if relative_star > 0 else relative_star)
    table_data.append([o, position_change_str, user, score, relative_star_str, missing_stars_str])


string = tabulate(
    table_data,
    headers=["Rank", "Change", "Name", "Score", "Relative score delta", "Missing parts"],
)
print(string)
