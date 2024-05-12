
from datetime import datetime
from datetime import timedelta


class UndergroundSystem():

    def __init__(self) -> None:
        # TODO: decide on what data structures should be used to hold the data
        self.pending_journeys = None
        self.completed_journeys = None

    def checkin(
        self,
        passenger_id: int,
        station_name: str,
        checkin_datetime: datetime,
    ) -> None:
        """Passenger check-in function

        Args:
            passenger_id (int): Unique identifier for passenger
            station_name (str): Starting station name
            checkin_datetime (datetime): Datetime of check-in event
        """

        # TODO: implement this function. A passenger cannot check in if they
        # have already checked in.
        # This function should raise a suitable exception in case of error.
        # Write a test case to test both the normal runtime path and the
        # error path.

        pass

    def checkout(
        self,
        passenger_id: int,
        station_name: str,
        checkout_datetime: datetime,
    ) -> None:
        """Passenger check-out function

        Args:
            passenger_id (int): Unique identifier for passenger
            station_name (str): Destination station name
            checkout_datetime (datetime): Datetime of check-out event
        """

        # TODO: implement this function. A passenger cannot check out if they
        # are not checked in.
        # This function should raise a suitable exception in case of error.
        # Write a test case to test both the normal runtime path and the
        # error path.

        pass

    def get_average_time(
        self,
        station_name_start: str,
        station_name_end: str,
    ) -> float:
        """Calculate the average time for journeys from starting station to
        final station

        Args:
            station_name_start (str): Starting station name
            station_name_end (str): Destination station name

        Returns:
            float: Average journey time duration in seconds
        """

        # TODO: implement this function. All possible journeys are initially
        # undefined. A journey becomes defined when a passenger checks into
        # a starting station and then checks out of a destination station.
        # This function must raise a RuntimeError if a journey is not defined.
        # (This is dictated by the contents of the
        # `test/test_underground_system.py` test file.)

        pass