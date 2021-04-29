import datetime
import socket
from models import *

#this is in the Influx line protocol, commas are only after the table name
table_name = """Screech_list,msgtype="bsc" """

class quest:
    def __init__(self, quest_port, quest_host):
        self.host = quest_host
        self.port = quest_port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def connect_tcp(self):
        self.s.connect((self.host, self.port))
        pass

    def send_screech_to_quest(self, screachs : List[Screech_data]):
        send_me = ''
        for payload in screachs:
            send_me += self.make_screach_Record(payload)

        print(send_me)
        self.send_record(bytes(send_me, "utf-8"))
        pass

    def make_screach_Record(self, myscreach : Screech_data):
        print(type(myscreach))
        out = table_name + 'author="' + myscreach.author + '",raw="' + myscreach.raw + '",HashTags="' + ','.join(myscreach.hashtags) + '",Users="' + ','.join(myscreach.users) + '",imgUrls="' + ','.join(myscreach.image_urls) + '"\n'
        return out
        pass

    def make_presence_record(self, my_presence_event :Presence_message):
        pass

    def send_record(self, byte_buffer):
        self.s.sendall(byte_buffer)
        print("writing to quest")
        pass


