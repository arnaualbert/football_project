from classes.Team import Team


class TeamDAO:
  def __init__(self, connection):
    self.connection = connection

  def get_team(self, id)->Team | None:
    """Get a team by id
    Input:
      id: int
    Output:
      Team: Team object if found
      None: None if not found"""
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM teams WHERE id = %s", (id,))
    team = cursor.fetchone()
    if team is None:
      return None
    return Team(team[0], team[1], team[2], team[3], team[4])

  def get_all_teams(self)->list[Team]:
    """Get all teams
    Input:
      None: It's not needed
    Output: 
      list[Team]: list of Team objects""" 
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM teams")
    teams = []
    for row in cursor:
      teams.append(Team(row[0], row[1], row[2], row[3], row[4]))
    return teams

  def create_team(self, team: Team):
    cursor = self.connection.cursor()
    cursor.execute("INSERT INTO teams (name, stadium, city, league_id) VALUES (%s, %s, %s, %s)",
                  (team.name, team.stadium, team.city, team.league_id))
    self.connection.commit()

  def update_team(self, team: Team):
    cursor = self.connection.cursor()
    cursor.execute("UPDATE teams SET name = %s, stadium = %s, city = %s, league_id = %s WHERE id = %s",
                  (team.name, team.stadium, team.city, team.league_id, team.id))
    self.connection.commit()

  def delete_team(self, id):
    cursor = self.connection.cursor()
    cursor.execute("DELETE FROM teams WHERE id = %s", (id,))
    self.connection.commit()