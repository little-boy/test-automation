import urllib.request
from datetime import datetime


def get_flight_infos_by_id(flight_id):
    pass


def sanity_check_on_flight_times(departure_time, arrival_time):
    pass


def get_elapsed_time_in_seconds(arrival_time, departure_time):
    pass


def calculate_flight_time(flight_id):
    # get flight by id
    # infos are already de-serialized (with correct data types)
    flight_infos = get_flight_infos_by_id(flight_id)

    # do validity check(s)
    sanity_check_on_flight_times(flight_infos.departure_time, flight_infos.arrival_time)

    flight_duration = get_elapsed_time_in_seconds(flight_infos.arrival_time, flight_infos.departure_time)

    # return calculation
    return {
        'flight': {
            'id': flight_id,
            'duration': flight_duration
        },
    }


flight_time = calculate_flight_time('68a3395a-603b-4f66-bffb-9945bc2f7ff8')

print(f'Flight time : {flight_time}')
