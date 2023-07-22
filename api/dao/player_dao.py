from classes.Player import Player

class PlayerDAO:
  def __init__(self, connection):
    self.connection = connection

  def get_player(self, id):
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM players WHERE id = %s", (id,))
    player = cursor.fetchone()
    if player is None:
      return None
    return Player(player[0], player[1], player[2], player[3], player[4])

  def get_all_players(self):
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM players")
    players = []
    for row in cursor:
      players.append(Player(row[0], row[1], row[2], row[3], row[4]))
    return players

  def create_player(self, player):
    cursor = self.connection.cursor()
    cursor.execute("INSERT INTO players (name, team_id, position, age) VALUES (%s, %s, %s, %s)",
                  (player.name, player.team_id, player.position, player.age))
    self.connection.commit()

  def update_player(self, player):
    cursor = self.connection.cursor()
    cursor.execute("UPDATE players SET name = %s, team_id = %s, position = %s, age = %s WHERE id = %s",
                  (player.name, player.team_id, player.position, player.age, player.id))
    self.connection.commit()

  def delete_player(self, id):
    cursor = self.connection.cursor()
    cursor.execute("DELETE FROM players WHERE id = %s", (id,))
    self.connection.commit()