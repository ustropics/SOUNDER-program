from datetime import datetime

def widget_values(widget_box):
    start_date = widget_box.children[1].children[0].value
    start_time = widget_box.children[1].children[1].value
    station = widget_box.children[2].value

    start_year = start_date.year
    start_month = start_date.month
    start_day = start_date.day

    return start_year, start_month, start_day, start_time, station