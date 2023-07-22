from flask import Blueprint, request
from dao.league_dao import LeagueDAO
from classes.League import League
from utils import object_to_dict, connection

app_league_controller = Blueprint('app_league_controller', __name__)
league_dao = LeagueDAO(connection)


@app_league_controller.route("/get_all_leagues", methods=['GET'])
def get_all_leagues():
    if request.method == 'GET':
        leagues_list_object: list[League] = league_dao.get_all_leagues()
        league_list_dict: dict[League] = [object_to_dict(league) for league in leagues_list_object]
        return league_list_dict

@app_league_controller.route("/get_specific_league", methods=['GET'])
def get_specific_league():
    if request.method == 'GET':
        pass