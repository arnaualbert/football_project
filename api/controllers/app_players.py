from flask import Blueprint, request
from dao.player_dao import PlayerDAO
from classes.Player import Player
from utils import object_to_dict, connection

app_players_controller = Blueprint('app_players_controller', __name__)
player_dao = PlayerDAO(connection)

@app_players_controller.route("/get_all_players", methods=['GET'])
def get_all_players():
    if request.method == 'GET':
        players_list_object: list[Player] = player_dao.get_all_players()
        player_list_dict: dict[Player] = [object_to_dict(player) for player in players_list_object]
        return player_list_dict
    

@app_players_controller.route("/get_players_by_team", methods=['GET'])
def get_players_by_team():
    if request.method == 'GET':
        get_team = request.get_json()
        team_id = get_team['team_id']
        players_list_object: list[Player] = player_dao.get_players_by_team(int(team_id))
        player_list_dict: dict[Player] = [object_to_dict(player) for player in players_list_object]
        return player_list_dict