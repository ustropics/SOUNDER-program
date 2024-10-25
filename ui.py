import ipywidgets as widgets
import datetime as dt

from ipywidgets import Layout

def create_widgets():
    # Time dropdown options
    time_list = ['00', '06', '12', '18']
    
    label1 = widgets.Label(value='Select the start and end date/time for the radar loop:')

    widget_start_date = widgets.DatePicker(layout={'width': 'initial'}, description='Start Date/Time', disabled=False, value=dt.date.today())
    widget_start_time = widgets.Dropdown(layout={'width': 'initial'}, options=time_list)
    station = widgets.Text(value='OAX', description='Station:', disabled=False, layout=Layout(width='150px'))

    start = widgets.HBox([widget_start_date, widget_start_time], layout=Layout(justify_content='flex-start'))
    return widgets.VBox([label1, start, station], layout=Layout(justify_content='flex-start'))