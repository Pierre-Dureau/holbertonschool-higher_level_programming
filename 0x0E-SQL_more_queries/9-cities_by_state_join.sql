-- lists all cities
-- with the name of thier state
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id=states.id;
