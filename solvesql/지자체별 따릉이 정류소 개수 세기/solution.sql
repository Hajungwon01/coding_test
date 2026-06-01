select local, count(station_id) as num_stations
from station
group by local
ORDER by num_stations;