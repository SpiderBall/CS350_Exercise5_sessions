DROP DATABASE IF EXISTS session;
CREATE DATABASE session;
CREATE EXTENSION pgcrypto;
\c session;
-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE IF NOT EXISTS movies (
  id serial,
  movie varchar(70) NOT NULL,
  theater varchar(50) NOT NULL,
  zip int NOT NULL,
  PRIMARY KEY (id)
) ;

--
-- Dumping data for table `movies`
--

INSERT INTO movies (movie, theater, zip) VALUES
('Valentine''s Day', 'Regal Fredericksburg 15', 22401),
('Big Hero 6', 'Regal Fredericksburg 15', 22401),
('The Wolfman', 'Regal Fredericksburg 15', 22401),
('Project Almanac', 'Marquee Cinemas Southpoint 9', 22401),
('Birdman', 'Allen Cinema 4 Mesilla Valley', 88005),
('A Most Violent Year', 'Allen Cinema 4 Mesilla Valley', 88005),
('Avatar3D', 'Allen Cinema 4 Mesilla Valley', 88005);

-- --------------------------------------------------------

--
-- Table structure for table `stores`
--

CREATE TABLE IF NOT EXISTS stores (
  id serial,
  name varchar(25) NOT NULL,
  type varchar(25) NOT NULL,
  address varchar(30) NOT NULL,
  city varchar(25) NOT NULL,
  zip int NOT NULL,
  PRIMARY KEY (id)
) ;

--
-- Dumping data for table `stores`
--

INSERT INTO stores (name, type, address, city, zip) VALUES
('Starbucks', 'coffee', '2511 Lohman Ave', 'Las Cruces', 88005),
('Milagro Coffee Y Espresso', 'coffee', '1733 E. University Ave', 'Las Cruces', 88005),
('Starbucks', 'coffee', '1500 South Valley',  'Las Cruces', 88005),
('Bean', 'coffee', '2011 Avenida De Mesilla',  'Las Cruces', 88005),
('Hyperion Espresso', 'coffee', '301 William St.',  'Fredericksburg', 22401),
('Starbucks', 'coffee', '2001 Plank Road', 'Fredericksburg', 22401),
('Caribou Coffee', 'coffee', '1251 Carl D Silver Parkway', 'Fredericksburg',  22401),
('Pancho Villa Mexican Rest', 'Mexican restaurant', '10500 Spotsylvania Ave', 'Fredericksburg', 22401),
('Chipotle', 'Mexican restaurant', '5955 Kingstowne', 'Fredericksburg', 22401),
('El Comedor', 'Mexican restaurant', '2190 Avenida De  Mesilla', 'Las Cruces', 88005),
('Los Compas', 'Mexican restaurant', '603 S Nevarez St.',  'Las Cruces', 88005),
('La Fuente', 'Mexican restaurant', '1710 S Espina',  'Las Cruces', 88005),
('Peet''s', 'coffee', '2260 Locust',  'Las Cruces', 88005);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id serial,
  username varchar(12) NOT NULL,
  password varchar(126) NOT NULL,
  zipcode int NOT NULL,
  PRIMARY KEY (id)
)  ;

--
-- Dumping data for table `users`
--

INSERT INTO users (username, password, zipcode) VALUES
('raz', crypt('p00d13', gen_salt('bf')), 88005),
('ann', crypt('changeme', gen_salt('bf')), 22401),
('lazy', crypt('qwerty', gen_salt('bf')), 22401);
