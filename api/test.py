from dao.player_dao import PlayerDAO
from dao.team_dao import TeamDAO
from dao.league_dao import LeagueDAO
from utils import connection, object_to_dict


player_dao = PlayerDAO(connection)
team_dao = TeamDAO(connection)
league_dao = LeagueDAO(connection)

players = player_dao.get_all_players()
for player in players:
    p = object_to_dict(player)
    print(p)

teams = team_dao.get_all_teams()
for team in teams:
    t = object_to_dict(team)
    print(t)

leagues = league_dao.get_all_leagues()
for league in leagues:
    l = object_to_dict(league)
    print(l)
