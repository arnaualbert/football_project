CREATE DATABASE IF NOT EXISTS tikitaka;
USE tikitaka;

CREATE TABLE IF NOT EXISTS league (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS teams (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  stadium VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  league_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (league_id) REFERENCES league (id)
);


CREATE TABLE IF NOT EXISTS players (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  team_id INT NOT NULL,
  position VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (team_id) REFERENCES teams (id)
);


INSERT INTO league (name, country) VALUES
  ("FA Women's Super League", 'England'),
  ('Primera Iberdrola', 'Spain'),
  ('Serie A Femminile', 'Italy'),
  ('Frauen-Bundesliga', 'Germany'),
  ('Division 1 Féminine', 'France');

INSERT INTO teams (name, stadium, city, league_id) VALUES
  ('Arsenal Women', 'Emirates Stadium', 'London', 1),
  ('Chelsea Women', 'Stamford Bridge', 'London', 1),
  ('Manchester City Women', 'Etihad Stadium', 'Manchester', 1),
  ('Liverpool Women', 'Anfield', 'Liverpool', 1),
  ('Manchester United Women', 'Old Trafford', 'Manchester', 1),
  ('Barcelona Women', 'Camp Nou', 'Barcelona', 2),
  ('Real Madrid Women', 'Santiago Bernabéu', 'Madrid', 2),
  ('Atlético Madrid Women', 'Wanda Metropolitano', 'Madrid', 2),
  ('Juventus Women', 'Juventus Stadium', 'Turin', 3),
  ('Inter Milan Women', 'San Siro', 'Milan', 3),
  ('Bayern Munich Women', 'Allianz Arena', 'Munich', 4),
  ('Borussia Dortmund Women', 'Signal Iduna Park', 'Dortmund', 4),
  ('Paris Saint-Germain Women', 'Parc des Princes', 'Paris', 5);

INSERT INTO players (name, team_id, position, age) VALUES
  ('Vivianne Miedema', 1, 'Forward', 25),
  ('Sam Kerr', 2, 'Forward', 28),
  ('Alexia Putellas', 3, 'Forward', 28),
  ('Marie-Antoinette Katoto', 5, 'Forward', 23),
  ('Beth Mead', 1, 'Forward', 26),
  ('Pernille Harder', 4, 'Forward', 29),
  ('Stina Blackstenius', 4, 'Forward', 26),
  ('Kim Little', 1, 'Midfielder', 33),
  ('Aitana Bonmatí', 3, 'Midfielder', 24),
  ('Jill Scott', 1, 'Midfielder', 35),
  ('Caroline Graham Hansen', 5, 'Midfielder', 27),
  ('Magdalena Eriksson', 1, 'Defender', 28),
  ('Irene Paredes', 3, 'Defender', 28),
  ('Sara Gama', 3, 'Defender', 33),
  ('Manuel Neuer', 4, 'Goalkeeper', 36),
  ('Christiane Endler', 5, 'Goalkeeper', 30);