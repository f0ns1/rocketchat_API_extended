import http.client as httplib
import urllib
import argparse
import os
import time
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat


class RequestServer():
    def __init__(self, host, user, password, id_user, id_session, session):
        print("Init class request server")
        self.HOST = host
        self.user= user
        self.id_session= id_session
        self.id_user = id_user
        self.password = password
        self.rocket = None
        self.session = session

    def login(self):
        self.rocket = RocketChat(self.user, self.password, self.id_session ,self.id_user, server_url=self.HOST, session=self.session)
        pprint(self.rocket)
        pprint(self.rocket.me())
        return self.rocket.me()

    def invoke(self, num):
        print("invoke method, operation number ", num)
        param=''
        if num == 1:
            print("\n\n Obtaining user data for authenticate user : ")
            pprint(self.rocket.me().json())
        elif num == 2:
            print("\n\n Obtaining channel list : ")
            pprint(self.rocket.channels_list().json())

        elif num == 3:
            print("\n\n Obtaining groups list : ")
            pprint(self.rocket.groups_list().json())

        elif num == 4:
            print("\n\n Obtaining subscriptios list : ")
            pprint(self.rocket.subscriptions_get().json())

        elif num == 5:
            print("\n\n Obtaining Channel History : ")
            channel = str(input("\t\t Channel Identifier: "))
            num_msg = int(input("\t\t Number of Messages: "))
            pprint(self.rocket.channels_history(channel, count=num_msg).json())
        elif num == 6:
            print("\n\n groups history: ")
            group = str(input("\t\t group identifier "))
            #num_msg = int(input("\t\t numer of messages: "))
            pprint(self.rocket.groups_history(group).json())
        elif num == 7:
            print("\n\n create group : ")
            name = str(input("\t\t group name "))
            pprint(self.rocket.groups_create(name).json())
        elif num == 8:
            print("\n\n add member to group : ")
            group = str(input("\t\t group identifier "))
            user = str(input("\t\t user dientifier "))
            pprint(self.rocket.groups_invite(group, user).json())
        elif num == 9:
            print("\n\n list users : ")
            pprint(self.rocket.users_list().json())
        elif num == 10:
            print("\n\n get subscriptions ")
            userid = str(input("Get userId : "))
            rid = str(input("get roomId " ))
            key = str(input("Key "))
            pprint(self.rocket.e2e_updateKey(userid, rid, key).json())
        else: 
            print("\n Operation not exists")

def operation_loop(auth, request):
    while(True):
        #os.system('cls' if os.name=='nt' else 'clear')
        print("Choose operation")
        print("\n\t\t 1. Authenticate user data: ")
        print("\n\t\t 2. Channel List: ")
        print("\n\t\t 3. Groups list: ")
        print("\n\t\t 4. Subscriptions list: ")
        print("\n\t\t 5. Channel History: ")
        print("\n\t\t 6. Get messages from groups: ")
        print("\n\t\t 7. Create Group: ")
        print("\n\t\t 8. Add member to Group: ")
        print("\n\t\t 9. Users list:  ")
        print("\n\t\t 10. Exit: ")
        print("\n: Select operation number: ")
        try:
            num = int(input())
            print("Selected operation : ", num)
            if num == 20:
                break
            else:
                request.invoke(num)
            time.sleep(1)
            cls = str(input("\n\n\t\t Clear window y/n:  "))
            if cls == 'y' or  cls == 'Y':
                os.system('cls' if os.name=='nt' else 'clear')
        except Exception as e:
            print(e)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', type=str, required=True)
    parser.add_argument('--user', type=str, required=False)
    parser.add_argument('--password', type=str, required=False)
    parser.add_argument('--x-user-id', type=str, required=False)
    parser.add_argument('--x-auth-token', type=str, required=False)
    args = parser.parse_args()
    print("\t\t RocketChat:::::::>  script")
    import requests
    session = requests.Session()
    session.verify = False
    if args.user and args.password:
        request = RequestServer(args.server, args.user, args.password, None,None,session=session )
    else:
        request = RequestServer(args.server, None, None, args.x_user_id, args.x_auth_token, session=session)
    control = request.login()
    if '[200]' in str(control):
        operation_loop(False, request)
        


if __name__ == "__main__":
    main()
