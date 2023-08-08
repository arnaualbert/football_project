from flask import Blueprint, request
from dao.team_dao import TeamDAO
from classes.Team import Team
from utils import object_to_dict, connection


app_teams_controller = Blueprint('app_teams_controller', __name__)
team_dao = TeamDAO(connection)

@app_teams_controller.route("/get_all_teams", methods=['GET'])
def get_all_teams():
    if request.method == 'GET':
        teams_list_object: list[Team] = team_dao.get_all_teams()
        team_list_dict: dict[Team] = [object_to_dict(team) for team in teams_list_object]
        return team_list_dict
    
