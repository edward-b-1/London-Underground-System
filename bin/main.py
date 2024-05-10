#!/usr/bin/env python3

from datetime import datetime
from datetime import timezone


from lib_underground_system import UndergroundSystem


def main():

    underground_system = UndergroundSystem()

    underground_system.checkin(
        passenger_id=1,
        station_name='Kings Cross',
        datetime=datetime(year=2024, month=1, day=1, hour=9, minute=30, second=0, tzinfo=timezone.utc)
    )

    underground_system.checkout(
        passenger_id=1,
        station_name='Oxford Circus',
        time=datetime(year=2024, month=1, day=1, hour=10, minute=10, second=0, tzinfo=timezone.utc)
    )

    average_time = underground_system.get_average_time(
        station_name_start='Kings Cross',
        station_name_end='Oxford Circus',
    )
    print(f'Average time from Kings Cross to Oxford Circus: {average_time}')


if __name__ == '__main__':
    main()
