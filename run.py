import sounderpy as spy
from utils import *


def create_sounding(widget_box):
    start_year, start_month, start_day, start_time, station = widget_values(widget_box)

    year = start_year
    month = start_month
    day = start_day
    hour = start_time
    station = station

    clean_data = spy.get_obs_data(station, year, month, day, hour)
    spy.build_sounding(clean_data, color_blind=True)
