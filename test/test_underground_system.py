
import pytest

from lib_underground_system import UndergroundSystem


def test_get_average_time_no_data():
    with pytest.raises(RuntimeError) as error:
        underground_system = UndergroundSystem()

        station_name_start = 'Kings Cross'
        station_name_end = 'Liverpool St'

        # TODO: This function call should raise the exception type RuntimeError
        # because there are no journeys defined from 'Kings Cross' to
        # 'Liverpool St'
        underground_system.get_average_time(station_name_start, station_name_end)


def test_get_average_time():
    '''
    TODO: write an implementation for this test function. Unlike the above case,
    this should be a test case which succeeds. In order words, passengers
    need to check into and out of some stations, and then the average journey
    time between those stations can be calculated.
    '''
    pass
