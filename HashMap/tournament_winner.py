"""
    Tournament winner challenge
"""
competitions = [['html', 'c#'], ['c#', 'python'], ['python', 'html']]
results = [0, 0, 1]
HOME_WIN = 1
WIN = 3
scores = {}


def tournament_winner():
    """Tournament winner function"""
    overall_winner = ''
    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition
        winner = home_team if result == HOME_WIN else away_team
        update_score(winner)
        score_values = scores.values()
        if scores[winner] == max(score_values):
            overall_winner = winner
    print(overall_winner)


def update_score(winner):
    """ Update the scores dictionary """
    if winner not in scores:
        scores[winner] = 3
    else:
        scores[winner] += 3


tournament_winner()
