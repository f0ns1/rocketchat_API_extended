from pprint import pprint
from rocketchat_API.rocketchat import RocketChat

proxy_dict = {
    "http"  : "http://127.0.0.1:8080",
    "https" : "https://127.0.0.1:8080",
}
id_user = 'ozRMWKjevXsDffALL'
id_session = 'S_Jue3738oX-9VxpHqhZzf7nso9BGp0DphJkz0LGENA'
user = None
password = None

print("Create Object ")
rocket = RocketChat(user, password, id_session ,id_user, server_url='https://open.rocket.chat')
print("rocket: ", rocket)
print("rocket.me() ", rocket.me())

#pprint(rocket.me().json())

#pprint(rocket.channels_list().json())

#pprint(rocket.chat_post_message('good news everyone!', channel='GENERAL', alias='Farnsworth').json())

#pprint(rocket.channels_history('GENERAL', count=5).json())

#pprint(rocket.groups_list().json())

pprint(rocket.subscriptions_get().json())
