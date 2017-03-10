#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on: Feb 28, 2017

from forecastiopy import *
from datetime import datetime, timedelta

api_key_file = 'api_key.txt'
with open(api_key_file, 'r') as ifile:
    api_key = ifile.readline()
    print(api_key)

washington_dc = [38.9072, -77.0369]

fio = ForecastIO.ForecastIO(api_key,
                            latitude=washington_dc[0], longitude=washington_dc[1])

if fio.has_hourly() is True:
    hourly = FIOHourly.FIOHourly(fio)
    print('Hourly')
    print('Summary:', hourly.summary)
    print('Icon', hourly.icon)

    for hour in range(1, 13):
        epoch_time = hourly.get_hour(hour)['time']
        real_time = str(datetime.utcfromtimestamp(epoch_time) - timedelta(hours=5))
        time_str = datetime.strptime(real_time, "%Y-%m-%d %H:%M:%S")
        my_time = time_str.strftime("%m/%d %I %p")
        print(my_time, '\t', round(hourly.get_hour(hour)['apparentTemperature']), hourly.get_hour(hour)['icon'],
              'Precipitation', hourly.get_hour(hour)['precipProbability'],'%')
        # for item in hourly.get_hour(hour).keys():
        #     print(item + ' : ' + str(hourly.get_hour(hour)[item]))
        #     print(hourly.hour_3_time)
else:
    print('No Hourly data')

if fio.has_daily() is True:
    daily = FIODaily.FIODaily(fio)
    print('Daily')
    #print('Summary:', daily.summary)
    #print('Icon:', daily.icon)

    for day in range(1, daily.days()):
        print('Day', day, 'Summary: ', daily.get_day(day)['icon'])
        print(daily.get_day(day)['apparentTemperatureMin'], ' - ', daily.get_day(day)['apparentTemperatureMax'])
        # for item in daily.get_day(day).keys():
        #     print(item + ' : ' + str(daily.get_day(day)[item]))
        # Or access attributes directly for a given minute.
        # daily.day_7_time would also work
        #print(daily.day_5_time)
else:
    print('No Daily data')
# import forecastio
# from datetime import datetime, timedelta
#
#
# api_key_file = 'api_key.txt'
# with open(api_key_file, 'r') as ifile:
#     api_key = ifile.readline()
#     print(api_key)
#
# lat = 38.9191485
# lng = -77.0362967
# current_time = datetime.now() - timedelta(hours=5)
# print(current_time)
#
# forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)
# by_hour = forecast.hourly()
# by_day = forecast.daily()
# print('daily', by_day.summary)
# print(by_hour.summary)
# print(by_hour.icon)
#
#
# for hourly_data in by_hour.data:
#     utc_time = hourly_data.time
#     utc_time_str = str(utc_time)
#     utc_times = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S")
#     my_time = utc_times - timedelta(hours=5)
#     my_new_time = my_time.strftime("%m/%d %I %p")
#     diff = current_time - my_time
#     diff_hours = diff.total_seconds() / 60 / 60
#
#     if diff_hours <= -3:
#         print(my_new_time, round(hourly_data.temperature), hourly_data.icon)