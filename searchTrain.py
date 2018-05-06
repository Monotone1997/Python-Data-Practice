"""
Usage:
    ����Ҫ��ѯ�Ļ����Ϳ��Զ�ѡ������d,����g,�ؿ�t,����k,ֱ��z��
    ��������ء�Ŀ�ĵء��������ڡ�
    ��ѯ�������������ʽ�Զ����֡�

Examples��
    Please input the trainType you want to search :dgz
    Please input the city you want leave :�Ͼ�
    Please input the city you will arrive :����
    Please input the date(Example:2017-09-27) :2018-03-01
"""
#coding = utf-8
#author = Lyon
#date = 2017-12-17
import json
import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
from stations import stations

class searchTrain:
    def __init__(self):
        self.trainOption = input('-d���� -g���� -k���� -t�ؿ� -zֱ��,Please input the trainType you want to search :')
        self.fromStation = input('Please input the city you want leave :')
        self.toStation = input('Please input the city you will arrive :')
        self.tripDate = input('Please input the date(Example:2017-09-27) :')
        self.headers = {
            "Cookie":"�Զ���",
            "User-Agent": "�Զ���",
            }
        self.available_trains,self.options = self.searchTrain()

    @property
    def trains(self):
        for item in self.available_trains:
            cm = item.split('|')
            train_no = cm[3]
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                train_no,
                '\n'.join([Fore.GREEN + cm[6] + Fore.RESET,
                          Fore.RED + cm[7] + Fore.RESET]),
                '\n'.join([Fore.GREEN + cm[8] + Fore.RESET,
                          Fore.RED + cm[9] + Fore.RESET]),
                cm[10],
                cm[32],
                cm[25],
                cm[31],
                cm[30],
                cm[21],
                cm[23],
                cm[28],
                cm[24],
                cm[29],
                cm[26],
                cm[22]   ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        header = '���� ��վ ʱ�� ��ʱ ������ �ص��� һ�� ���� �߼����� ���� Ӳ�� ���� Ӳ�� ���� ����'.split()
        pt._set_field_names(header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

    def searchTrain(self):
        arguments = {
        'option':self.trainOption,
        'from':self.fromStation,
        'to':self.toStation,
        'date':self.tripDate
        }
        options = ''.join([item for item in arguments['option']])
        from_station, to_station, date = stations[arguments['from']] , stations[arguments['to']] , arguments['date']
        url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(date,from_station,to_station)
        requests.packages.urllib3.disable_warnings()
        html = requests.get(url,headers = self.headers,verify=False)
        available_trains = html.json()['data']['result']
        return available_trains,options

if __name__ == '__main__':
    while True:
        asd = searchTrain()
        asd.pretty_print()