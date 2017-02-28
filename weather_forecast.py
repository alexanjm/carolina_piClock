#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on: Feb 28, 2017

import forecastio

api_key = "your api key"
lat = 38.9191485
lng = -77.0362967

forecast = forecastio.load_forecast(api_key, lat, lng)