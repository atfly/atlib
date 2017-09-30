
#!usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib2
import subprocess
from ConfigParser import RawConfigParser
from config import *
from threading import Thread
import sys
import time

game_list = RawConfigParser()
game_list.read('gamelist.conf')
games = game_list.sections()
games.sort()

def get_location_data(location_file):
    """ get the database of ip to location from a file """

    patten = re.compile(r"'(.*)':'(.*)',?")

    try:
        f = open(location_file, 'r')
    except:
        print 'error when open file %s' % location_file

    location_data = {}
    for i in f.readlines():
        m = re.search(patten, i)
        if m:
            location_data[str(m.group(1))] = m.group(2)
    return location_data

def get_server_list(url, patten):
    """ Get server list of a game"""

    if not url or not patten:
        return [i for i in range(1, 101)]
    patten = re.compile(patten)
    server_list = set()

    f = urllib2.urlopen(url)
    for i in f.readlines():
        m = re.search(patten, i.decode('utf-8'))
        if m:
            server_list.add(int(m.group(1)))

    return server_list

def get_ip_address(domain_name, servers_ips):
    """ get the ip address of the given domain """

    patten = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
    ips = set()
    server = int(domain_name.split('.')[0][1:])

    for dns in [dns_lt, dns_dx]:
        cmd = 'dig +retry=%s +time=%s +short %s @%s' % (
               dns_retry, dns_timeout, domain_name, dns)
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, shell=True)
        for r in result.stdout.readlines():
            m = re.search(patten, r)
            if m:
                ips.add(m.group(1))
                #print m.group(1)
    servers_ips.append({server: ips})

def get_location_of_ip(ip):
    """ Get the location info of a given ip address """

    ip = ip.split('.')[0:3]
    ip = '.'.join(ip)
    location_data = get_location_data(location_file)
    if ip in location_data.keys():
        return location_data[ip]
    else:
        return 'No location Found NO'

def write_to_file(filename, data):
    """ Write data to file """

    try:
        f = open(filename, 'a+')
    except:
        print 'error when open %s' % filename
    f.writelines(data)
    f.close()

def generate_output(name, server, next_server, domain, platform,
                    ips, alerts, method='Ping', port='80'):
    """ generate output data"""

    output_string = ''
    server_name = domain % int(server)

    output_string += data_head % server
    for ip in ips:
        location = get_location_of_ip(ip)
        location_short = location[-2:]
        # locals() include:
        # name, location_short, server,
        # ip, location, method, alerts, port
        output_string += data_body[method.lower()] % locals()

    return ({server: output_string})

def update_game(game):
    """ update game, call generate_output """

    output = []

    name = game_list.get(game, 'name')
    url = game_list.get(game, 'url')
    domain = game_list.get(game, 'domain')
    output_file = game_list.get(game, 'output_file')
    patten = game_list.get(game, 'patten').decode('gb2312')
    platform = game_list.get(game, 'platform')
    method = game_list.get(game, 'method')
    alerts = game_list.get(game, 'alerts')
    port = game_list.get(game, 'port')

    f = open(output_file, 'w')
    f.close()

    print '%s-%s update is started' % (name, platform)

    server_list = get_server_list(url, patten)
    servers_ips = []
    while server_list:
        threads = []

        for i in range(min(MAX_THREAD, len(server_list))):

            server = server_list.pop()

            server_name = domain % server
            print server_name
            t = Thread(target=get_ip_address,
                       args=(server_name,servers_ips))
            threads.append(t)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
    servers_ips.sort()
  
    while servers_ips:
        server_ip = servers_ips.pop(0)
        server = server_ip.keys()[0]
        ips = server_ip.values()[0]
        next_server = server

        while servers_ips and (not servers_ips[0].values()[0] 
                or sorted(ips) == sorted(servers_ips[0].values()[0])):
            next_server += 1
            servers_ips.pop(0)

        server_output = generate_output(name, server, next_server, 
                                        domain, platform, ips,
                                        alerts, method, port)
        
        output.append(server_output)

    output.sort()
    for data in output:
        for key in data.keys():
            write_to_file(output_file, data[key])

    print '%s-%s update is done' % (name, platform)

def call_update_games(games_to_update):
    """ call update_game to update all game that needed """
    while games_to_update:
        threads = []
        for i in range(min(MAX_THREAD, len(games_to_update))):
            game = games_to_update.pop()
            t = Thread(target=update_game, args=(game,))
            threads.append(t)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

#www.iplaypy.com
def main():
    """ give a menu to user for which game to update """
    while True:
        games_to_update = set()
        print '-' * 40
        print ' Program for update information of game'
        print '-' * 40
        print '\nhere is the list of game'
        print '-' * 40
        for i in games:
            print '[%s] %s----%s' % (i, game_list.get(i, 'name'),
                                  game_list.get(i, 'platform'))
        print '-' * 40
        print 'Enter the num of game to update,\n0 to update all, ! to quit'
        choice = raw_input("game to update: ")

        while True:

            match = re.findall(r'(\S)', choice)
            if match[0] == '!':
                sys.exit()
            elif match[0] == '0':
                games_to_update = games
                break
            for i in match:
                if i in games:
                    games_to_update.add(i)
            if not len(games_to_update):
                choice = raw_input('input invalid, try again: ')
                continue
            break

        call_update_games(games_to_update)
        time.sleep(3)
        sys.exit()

if __name__ == '__main__':
    main()
