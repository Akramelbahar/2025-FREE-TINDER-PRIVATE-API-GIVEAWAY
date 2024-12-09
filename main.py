import time
import json
from protobuf_decoder.protobuf_decoder import Parser 
from request_pb2 import MainRequest, RefreshAuth, AuthFlowVariant
import requests
import random
alphabets = "abcdefghijklmnopqrstwxyz0123456789"
def decode_protobuf_from_binary(binary_data):
    try:
        hex_data = " ".join([f"{byte:02x}" for byte in binary_data])
        parsed_data = Parser().parse(hex_data)
        for e in parsed_data.to_dict()["results"][0]["data"]["results"]:
            if(e["field"] == 2 ):
                return e["data"]
    except Exception as e:
        print(f"Error decoding Protobuf: {e}")
        return None
class TinderAccount:
    deviceId = ""
    refresh_token = ""
    auth_token = ""
    user_id = ""
    headers = {}
    proxies = None 
    def __init__(self ,refresh_token ,auth_token, deviceId , proxies=None ) -> None:
        self.proxies = proxies
        self.refresh_token = refresh_token
        self.auth_token = auth_token
        self.deviceId = deviceId
        self.headers = {
                "User-Agent": "Tinder Android Version 15.21.1",
                "os-version": "33",
                "app-version": "4683",
                "platform": "android",
                "platform-variant": "Google-Play",
                "accept-language": "en-US",
                "tinder-version": "15.21.1",
                "store-variant": "Play-Store",
                "x-device-ram": "7",
                "persistent-device-id": f"{"".join(random.choices(alphabets , k=16))}",
                "app-session-id": f"{"".join(random.choices(alphabets , k=9))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=12))}" or"131c1b5f-cfef-4017-9f5b-69d6e48df2b9",
                "user-session-id": f"{"".join(random.choices(alphabets , k=9))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=12))}" or"131c1b5f-cfef-4017-9f5b-69d6e48df2b9",
                "install-id": "c-WwwUpmHp8",
                "x-auth-token": auth_token,
                "content-type": "application/json; charset=UTF-8",
                "accept-encoding": "gzip",
            }
        pass
    def get_random_proxy(self):
        if(self.proxies):
            proxy = random.choice(self.proxies)
            return {"http": proxy, "https": proxy}
        else:
            return None
    def changeLocation(self,lat , long):
        url = "https://api.gotinder.com/v2/meta"

        payload = {
            "force_fetch_resources": True,
            "lat": lat,
            "lon": long
        }
        response = requests.post(url , headers=self.headers , json=payload , proxies=self.get_random_proxy())
        
        if (response.status_code != 200):
            raise Exception(response.json()["error"]["message"])
        print("Location Changed successfully")
        return response.json()
    def ageDistanceChange(self , age_filter_max , age_filter_min , distance_filter):
        url = "https://api.gotinder.com/v2/profile/user"
        payload = {
                    "age_filter_max": age_filter_max,
                    "age_filter_min": age_filter_min,
                    "auto_expansion": {
                        "age_toggle": False,
                        "distance_toggle": False
                    },
                    "distance_filter": distance_filter,
                    "show_same_orientation_first": {}
                }
        response = requests.post(url , json=payload , headers=self.headers , proxies=self.get_random_proxy())
        if(response.status_code == 200):
            print("age and distance updated successfully .")
        else :
            print("An error occured during changing age and distance")
    def interstedIn(self ,interested_in ):
        url = "https://api.gotinder.com/v2/profile/user"
        payload = {
                "interested_in": interested_in,
                "show_same_orientation_first": {
                    "checked": True,
                    "should_show_option": False
                }
            }
        response = requests.post(url , json=payload , headers=self.headers , proxies=self.get_random_proxy())
        if(response.status_code == 200):
            print("interst changed successfully .")
            return True
        else :
            return False
    def authGen(self):
        refresh_auth_message = RefreshAuth(refresh_token=self.refresh_token)
        auth_flow_variant_message = AuthFlowVariant(value="STANDARD")     
        main_request = MainRequest(
                                        refresh_auth=refresh_auth_message,
                                        auth_flow_variant=auth_flow_variant_message
                                    )  
        serialized_data = main_request.SerializeToString()
        url = "https://api.gotinder.com/v3/auth/login"
        try :
            headers = {
                        "appsflyer-id": "-5004160359472945568",
                        "advertising-id": "",
                        "funnel-session-id": "330790c7-210c-4aa5-a985-d34996a9438a",
                        "x-tinder-deeplink-token": "",
                        "user-agent": "Tinder Android Version 15.21.1",
                        "os-version": "28",
                        "app-version": "4683",
                        "platform": "android",
                        "platform-variant": "Google-Play",
                        "x-supported-image-formats": "webp",
                        "accept-language": "en-US",
                        "tinder-version": "15.21.1",
                        "store-variant": "Play-Store",
                        "x-device-ram": "8",
                        "persistent-device-id": self.deviceId,
                        "app-session-id": f"{"".join(random.choices(alphabets , k=9))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=12))}" or"131c1b5f-cfef-4017-9f5b-69d6e48df2b9",
                        "app-session-time-elapsed": "3066.498",
                        "user-session-id": f"{"".join(random.choices(alphabets , k=9))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=12))}" or"131c1b5f-cfef-4017-9f5b-69d6e48df2b9",
                        "user-session-time-elapsed": "967.876",
                        "install-id": "fLU2G6TuGkQ",
                        "x-auth-token": f"{"".join(random.choices(alphabets , k=9))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=4))}-{"".join(random.choices(alphabets , k=12))}" or"131c1b5f-cfef-4017-9f5b-69d6e48df2b9",
                        "content-type": "application/x-protobuf",
                        "accept-encoding": "gzip",
                    }
            response = requests.post(url , data=serialized_data , headers=headers, proxies=self.get_random_proxy())          
            if(response.status_code == 200):    
                self.auth_token = decode_protobuf_from_binary(response.content)
                print(self.auth_token)
            else :
                print("error during generating token")
        except:
            raise Exception(f"Error during generating token status code = {200} and content = {response.content}")
    def checkAuth(self):
        url ="https://api.gotinder.com/v2/profile"
        response = requests.get(url , headers=self.headers, proxies=self.get_random_proxy())
        if(response.status_code ==200):
            return
        else:
            print("regenerating Auth ...")
            self.auth_token = self.authGen()
            print("regenerated .")
    def search(self):
        url = "https://api.gotinder.com/v2/recs/core?locale=en&distance_setting=mi"
        response = requests.get(url , headers=self.headers, proxies=self.get_random_proxy())
        print(response.status_code)
        data = response.json()["data"]["results"]
        return data
    def refuse(self , user_id , content_hash , photoId , s_number):
        url = f"https://api.gotinder.com/pass/{user_id}"
        payload = {
                "content_hash": content_hash,
                "photoId": photoId,
                "s_number": s_number
            }
        response = requests.post(url , headers=self.headers , json=payload)
        print(response.status_code)
        if(response.status_code == 200):
            print("refused successfully")
    def passport(self , lat , long):
        url = f"https://api.gotinder.com/passport/user/travel"
        payload = {"lat":lat,"lon":long}
        response = requests.post(url , headers=self.headers , json=payload)
        
        if(response.status_code == 200):
            print(response.text)
            print("passport address changed successfully")
    def profileInfo(self):
        url = "https://api.gotinder.com/v2/profile?include=offerings%2Cfeature_access%2Cswipenote%2Cpaywalls%2Cnudge_rules%2Cboost%2Ccompliance%2Caccount%2Cuser%2Cspotify%2Conboarding%2Cexplore_settings%2Cinstagram%2Clikes%2Ctravel%2Cavailable_descriptors%2Cprofile_meter%2Ccampaigns%2Cemail_settings%2Ctop_photo%2Cpurchase%2Creadreceipts%2Csuper_likes%2Ctinder_u%2Ctutorials%2Conboarding%2Cplus_control"
        response = requests.get(url , headers=self.headers)
        if(response.status_code == 200):
            print("Profile Info")
            print(response.json())
            
woman = [1]
man = [0]
everyone = [0,1]
proxies_list = [
 
]
