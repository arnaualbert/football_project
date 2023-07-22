from flask import Flask
from flask_cors import CORS

from controllers.app_teams import app_teams_controller
from controllers.app_players import app_players_controller
from controllers.app_league import app_league_controller

module_name = __name__
app = Flask(__name__)
CORS(app)

app.register_blueprint(app_teams_controller)
app.register_blueprint(app_players_controller)
app.register_blueprint(app_league_controller)


# print(app.url_map)
if __name__ == "__main__":
    app.run(debug=True)