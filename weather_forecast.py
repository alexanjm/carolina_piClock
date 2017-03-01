#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on: Feb 28, 2017

import forecastio
from datetime import datetime, timedelta


api_key_file = 'api_key.txt'
with open(api_key_file, 'r') as ifile:
    api_key = ifile.readline()
    print(api_key)

lat = 38.9191485
lng = -77.0362967
current_time = datetime.now() - timedelta(hours=5)
print(current_time)

forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)
by_hour = forecast.hourly()
print(by_hour.summary)
print(by_hour.icon)


for hourly_data in by_hour.data:
    utc_time = hourly_data.time
    utc_time_str = str(utc_time)
    utc_times = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S")
    my_time = utc_times - timedelta(hours=5)
    my_new_time = my_time.strftime("%m/%d %I %p")
    diff = current_time - my_time
    diff_hours = diff.total_seconds() / 60 / 60

    if diff_hours <= -3:
        print(my_new_time, round(hourly_data.temperature), hourly_data.icon)