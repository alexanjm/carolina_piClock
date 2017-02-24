#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on: Feb 6, 2017

import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime, time

# # Personal info goes here
# target_schools = ['Boston University', 'UCLA', 'UCSD']
# field_to_search = 'bioinformatics'
# path = ''
#

# site = "http://www.goheels.com/SportSelect.dbml?SPSID=668157&SPID=12965"
# request = urllib.request.Request(site)
# opener = urllib.request.build_opener()
# page = opener.open(request)
#
# soup = BeautifulSoup(page, 'lxml')
#
# win_scrape = soup.find_all('td' , class_ = 'results')[0:]
# wins = []
# for i in win_scrape:
# 	win_name = i.get_text()
# 	win_name = win_name.strip('\n\t\t\t\t\t\t')
# 	wins.append(win_name)
# print(wins)


#
#
# school_scrape = soup.find_all('td' , class_ = 'opponent')[0:]
# schools = []
# for i in school_scrape:
# 	school_name = i.get_text()
# 	school_name = school_name.strip('\n\t\t\t\t\t\t')
# 	schools.append(school_name)
# print(schools)
#
#
# date_scrape = soup.find_all('td' , class_ = 'date')
# dates = []
# for i in date_scrape:
# 	date_name = i.get_text()
# 	date_name = date_name.strip('\n\t\t\t\t\t')
# 	dates.append(date_name)
# print(dates)
#
# time_scrape = soup.find_all('td' , class_ = 'time')
# times = []
# for i in time_scrape:
# 	time_name = i.get_text()
# 	time_name = time_name.strip('\n\t\t\t\t\t')
# 	times.append(time_name)
# print(times)


schools = ['UNC Pembroke (exhibition)', 'Tulane', 'Chattanooga', 'Long Beach State', 'Hawaii (8:00 PM HT/1:00 AM ET)',
           'Chaminade', 'Oklahoma State', 'Wisconsin', 'Indiana', 'Radford', 'Davidson', 'Tennessee', 'Kentucky',
           'Northern Iowa', 'Monmouth', 'Georgia Tech *', 'Clemson *', 'N.C. State *', 'Wake Forest *',
           'Florida State *', 'Syracuse *', 'Boston College *', 'Virginia Tech *', 'Miami *', 'Pittsburgh *',
           'Notre Dame *', 'Duke *', 'N.C. State *', 'Virginia *', 'Louisville *', 'Pittsburgh *', 'Virginia *',
           'Duke *', 'ACC First Round', 'ACC Second Round', 'ACC Quarterfinal', 'ACC Semifinal', 'ACC Final']
dates = ['Fri, Nov 04', 'Fri, Nov 11', 'Sun, Nov 13', 'Tue, Nov 15', 'Fri, Nov 18', 'Mon, Nov 21', 'Tue, Nov 22',
         'Wed, Nov 23', 'Wed, Nov 30', 'Sun, Dec 04', 'Wed, Dec 07', 'Sun, Dec 11', 'Sat, Dec 17', 'Wed, Dec 21',
         'Wed, Dec 28', 'Sat, Dec 31', 'Tue, Jan 03', 'Sun, Jan 08', 'Wed, Jan 11', 'Sat, Jan 14', 'Mon, Jan 16',
         'Sat, Jan 21', 'Thu, Jan 26', 'Sat, Jan 28', 'Tue, Jan 31', 'Sun, Feb 05', 'Thu, Feb 09', 'Wed, Feb 15',
         'Sat, Feb 18', 'Wed, Feb 22', 'Sat, Feb 25', 'Mon, Feb 27', 'Sat, Mar 04', 'Tue, Mar 07', 'Wed, Mar 08',
         'Thu, Mar 09', 'Fri, Mar 10', 'Sat, Mar 11']
times = ['7:30 PM', '9:00 PM', '4:00 PM', '8:00 PM', '1:00 AM', '11:30 PM', '10:30 PM', '9:30 PM', '9:00 PM', '2:00 PM',
         '9:00 PM', '5:00 PM', '5:45 PM', '8:00 PM', '7:00 PM', '12:00 PM', '7:00 PM', '1:00 PM', '8:00 PM', '2:00 PM',
         '7:00 PM', '12:00 PM', '8:00 PM', '1:00 PM', '7:00 PM', '1:00 PM', '8:00 PM', '8:00 PM', '8:20 PM', '9:00 PM',
         '12:00 PM', '7:00 PM', '8:00 PM', 'TBA', 'TBA', 'TBA', 'TBA', 'TBA']
results = ['124 - 63', '95 - 75(W)', '97 - 57(W)', '93 - 67(W)', '83 - 68(W)', '104 - 61(W)', '107 - 75(W)',
           '71 - 56(W)', '67 - 76(L)', '95 - 50(W)', '83 - 74(W)', '73 - 71(W)', '100 - 103(L)', '85 - 42(W)',
           '102 - 74(W)', '63 - 75(L)', '89 - 86(W) OT', '107 - 56(W)', '93 - 87(W)', '96 - 83(W)', '85 - 68(W)',
           '90 - 82(W)', '91 - 72(W)', '62 - 77(L)', '80 - 78(W)', '83 - 76(W)', '78 - 86(L)', '97 - 73(W)',
           '65 - 41(W)', '74 - 63(W)', '', '', '', '', '', '', '', '']

###########################
# Function to put years on end of dates
# TO DO: -- TURN THIS INTO A FUNCTION
now = datetime.now()
# print(now)

season_year2 = now.year
season_year1 = now.year - 1
# print(season_year1, season_year2)
date_year = []
for x in dates:
    end_months = ['Oct', 'Nov', 'Dec']
    if end_months[0] in x:
        date_year_str = str(x) + ' ' + str(season_year1)
        date_year.append(date_year_str)
    # print(date_year_str)
    elif end_months[1] in x:
        date_year_str = str(x) + ' ' + str(season_year1)
        date_year.append(date_year_str)
    # print(date_year_str)
    elif end_months[2] in x:
        date_year_str = str(x) + ' ' + str(season_year1)
        date_year.append(date_year_str)
    # print(date_year_str)
    else:
        date_year_str = str(x) + ' ' + str(season_year2)
        date_year.append(date_year_str)
    # print(date_year_str)
    # print(date_year)
# print('length:', len(date_year))

dt_new = []
dt_raw = []
for x in date_year:
    dt = datetime.strptime(x, '%a, %b %d %Y')
    dt_raw.append(dt)
    dt_fmt = dt.strftime('%a %m/%d')
    dt_new.append(dt_fmt)


# print(dt_new)
# print(dt_raw)

####################### - Year function - ####################



def get_latest_time(date_list):
    diff_list = []
    now_time = datetime.now()
    for z in date_list:
        # print('date list', x, 'now', now)
        diff = z - now_time
        # print('diff', diff)
        diff_days = diff.days
        # print('days', diff_days)
        diff_list.append(diff_days)
    diff_list_abs = [abs(number) for number in diff_list]
    gameday = min(diff_list_abs)
    indice_num = diff_list_abs.index(gameday)
    if diff_list[indice_num] >= 0:
        # print('GAMEDAY:', dt_new[indice_num], '\n', schools[indice_num][:-2].center(18, ' '), '\n', times[indice_num].center(18, ' '))
        future_str = '\nGAMEDAY: %s\n%s\n%s\n' % (dt_new[indice_num], schools[indice_num][:-2].center(18, ' '),
                                                  times[indice_num].center(18, ' '))
        return future_str
    else:
        # print('RESULT:', dt_new[indice_num], '\n', schools[indice_num][:-2].center(18, ' '), '\n', results[indice_num].center(18, ' '))
        past_str = '\nRESULT: %s\n%s\n%s\n' % (dt_new[indice_num], schools[indice_num][:-2].center(18, ' '),
                                               times[indice_num].center(18, ' '))
        return past_str


print(get_latest_time(dt_raw))





# Store schools and dates together as a tuple
# big_list = list(zip(schools, dates))
#
# target_results = []
#
# # If one of your target schools is in the results, put it in the text file
# for i in big_list:
# 	for j in target_schools:
# 		if j in i[0]:
# 			target_results.append("Result found for {} as {} on {}".format(j, i[0], i[1]))
#
# def output_writer(title):
# 	with open(path + title + '.txt', 'w') as f:
# 		for line in target_results:
# 			f.write(str(line) + "\n")
# 	f.close()
#
# output_writer('new_results')
#
# # Check for output file, correct if first run
# try:
# 	f = open(path + 'old_results.txt', 'r')
# except:
# 	output_writer('old_results')
# 	print('This is your first time running the script.\n'
# 		'Check the website for now, the next time you run it you will get updates.')
#
# updates = []
#
# with open(path + 'new_results.txt', 'r') as n:
# 	n = n.read()
# 	# If there is an update that wipes all your schools from the first page,
# 	# rewrite the file to avoid false flags
# 	if n == '\n' or n == '\n\n' or n == '':
# 		output_writer('old_results')
# 	n_l = n.split('\n')
# 	n_l_size = len(n_l)
# 	with open(path + 'old_results.txt', 'r') as o:
# 		o = o.read()
# 		o_l = o.split('\n')
# 		o_l_size = len(o_l)
# 		# Check for new results even if the same number of lines are present
# 		if o_l_size == n_l_size:
# 			for i in range(n_l_size):
# 				if n_l[i] != o_l[i]:
# 					updates.append(n_l[i])
# 			output_writer('old_results')
# 		# Stuck only checking the same amount of lines as the smaller file
# 		if o_l_size < n_l_size:
# 			for i in range(o_l_size):
# 				if n_l[i] != o_l[i]:
# 					updates.append(n_l[i])
# 			updates.append('There may be additional updates.')
# 			output_writer('old_results')
#
# if updates != []:
# 	print(updates)
# else:
# 	print('No new updates.')

# # GNOME integration for other Linux nerds
# import subprocess

# gnome_update = []

# for i in updates:
# 	if i == 'There may be additional updates':
# 		gnome_update.append(' + more')
# 	else:
# 		gnome_update.append(i[17:24])

# msg = ", ".join(str(i) for i in gnome_update)

# def send_message(message):
# 	subprocess.Popen(['notify-send', message])
# 	return
# if updates != []:
# 	send_message(msg)

# # Email functionality, you'll have to set it up yourself
# import smtplib

# gmail_user = 'your_username' + '@gmail.com'  
# gmail_password = 'your_password'

# outgoing = gmail_user  
# to = gmail_user 
# subject = 'School Admissions Update'  
# body = str(updates)

# email_text = """\  
# outgoing: {}  
# To: {}  
# Subject: {}

# {}
# """.format(outgoing, ", ".join(to), subject, body)

# try:  
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
#     server.sendmail(outgoing, to, email_text)
#     server.close()

#     print 'Email sent!'
# except:  
#     print 'Something went wrong.'
