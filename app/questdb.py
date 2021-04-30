import datetime
import socket
from models import *

#this is in the Influx line protocol, commas are only after the table name then inbetween each value. Spaces are the important delimiter
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
        ILP_string = ''
        for payload in screachs:
            ILP_string += self.make_screach_Record(payload)

        print(ILP_string)
        self.send_record(bytes(ILP_string, "utf-8"))
        pass

        #shouly likely break this into an ILP making function at some point but it works for now...
    def make_screach_Record(self, my_screach : Screech_data):
        print(type(my_screach))
        out = table_name + 'author="' + my_screach.author + '",raw="' + my_screach.raw + '",HashTags="' + ','.join(my_screach.hashtags) + '",Users="' + ','.join(my_screach.users) + '",imgUrls="' + ','.join(my_screach.image_urls) + '"\n'
        return out
        pass

    def make_presence_record(self, my_presence_event :Presence_message):
        pass

    def send_record(self, byte_buffer):
        self.s.sendall(byte_buffer)
        print("writing to quest")
        pass


