"""
    Tournament winner challenge
"""
# competitions = [['html', 'c#'], ['c#', 'python'], ['python', 'html']]
competitions = [["Bulls", "Eagles"]]
competition1 = [["Java", "C#"]]
competition2 = [["CSS", "Php"]]
competition3 = [["Java", "C#"]]
results = [1]
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

WIN = 3
HOME_TEAM_WIN = 1


# def tournamentWinner(competitions, results):
#     scores = {}
#     overall_winner = ''
#
#
# for idx, competition in enumerate(competitions):
#     result = results[idx]
#     home_team, away_team = competition
#     winner = home_team if result == HOME_TEAM_WIN else away_team
#     update_scores(winner, scores)
#     score_values = scores.values()
#
#     if scores[winner] == max(score_values):
#         overall_winner = winner
# return overall_winner
#
#
# def update_scores(winner, scores):
#     if not winner in scores:
#         scores[winner] = WIN
#
#     else:
#         scores[winner] += WIN
