from classes.League import League

class LeagueDAO:
  def __init__(self, connection):
    self.connection = connection

  def get_league(self, id):
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM league WHERE id = %s", (id,))
    league = cursor.fetchone()
    if league is None:
      return None
    return League(league[0], league[1], league[2])

  def get_all_leagues(self):
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM league")
    leagues = []
    for row in cursor:
      leagues.append(League(row[0], row[1], row[2]))
    return leagues

  def create_league(self, league: League):
    cursor = self.connection.cursor()
    cursor.execute("INSERT INTO league (name, country) VALUES (%s, %s)", (league.name, league.country))
    self.connection.commit()

  def update_league(self, league: League):
    cursor = self.connection.cursor()
    cursor.execute("UPDATE league SET name = %s, country = %s WHERE id = %s",
                  (league.name, league.country, league.id))
    self.connection.commit()

  def delete_league(self, id):
    cursor = self.connection.cursor()
    cursor.execute("DELETE FROM league WHERE id = %s", (id,))
    self.connection.commit()