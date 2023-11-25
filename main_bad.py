import urllib.request
from datetime import datetime


def calculate_flight_time(flight_id):
    # get flight by id
    flight_infos = urllib.request.urlopen(f"https://flight-times.api.com/{flight_id}").read()

    date_format = '%Y-%m-%d %H:%M:%S%z'

    # convert dates
    departure_time = datetime.strptime(flight_infos.departure_time, date_format)
    arrival_time = datetime.strptime(flight_infos.l, date_format)

    # do validity check(s)
    if departure_time > arrival_time:
        raise ValueError('Flight is arriving before departure. That\'s weird')

    # return calculation
    return {
        'flight': {
            'id': flight_id,
            'duration': arrival_time.now() - departure_time.now()
        },
    }


flight_time = calculate_flight_time('68a3395a-603b-4f66-bffb-9945bc2f7ff8')

print(f'Flight time : {flight_time}')