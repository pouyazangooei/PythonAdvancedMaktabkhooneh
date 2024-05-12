teams = {
    "Spain": {"wins": 0, "losses": 0, "draws": 0, "goal_difference": 0, "points": 0},
    "Iran": {"wins": 0, "losses": 0, "draws": 0, "goal_difference": 0, "points": 0},
    "Portugal": {"wins": 0, "losses": 0, "draws": 0, "goal_difference": 0, "points": 0},
    "Morocco": {"wins": 0, "losses": 0, "draws": 0, "goal_difference": 0, "points": 0}
}

def teams_stats_update(team_name,goalsfor,goalsagainst):
    teams[team_name]['goal_difference'] += (goalsfor - goalsagainst)
    if goalsfor > goalsagainst:
        teams[team_name]['wins'] += 1
        teams[team_name]['points'] += 3
    elif goalsfor == goalsagainst:
        teams[team_name]['draws'] += 1
        teams[team_name]['points'] += 1
    else:
        teams[team_name]['losses'] += 1

matches = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco")
]

for home_team,away_team in matches:
    result = input()
    goals_home , goals_away = map(int, result.split('-'))
    teams_stats_update(home_team,goals_home,goals_away)
    teams_stats_update(away_team,goals_away,goals_home)

sorted_teams = sorted(teams.items(), key=lambda item: (-item[1]['points'], -item[1]['wins'], item[0]))
for team, stats in sorted_teams:
    print(f"{team} Wins: {stats['wins']}, Losses: {stats['losses']}, Draws: {stats['draws']}, Goal Difference: {stats['goal_difference']}, Points: {stats['points']}")
