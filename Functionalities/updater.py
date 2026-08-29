import json
import urllib.request
import urllib.error
def update_checker(user_version):
    integer_user_version = user_version.split('.')
    GitHub_API = "https://api.github.com/repos/jovancherian-source/EnDek/releases/latest"
    try:
        request = urllib.request.Request(GitHub_API, headers={"User-Agent": "EnDek"})
        with urllib.request.urlopen(request, timeout=5) as whole_data_json:
            whole_data = json.loads(whole_data_json.read().decode())
        latest_verison = whole_data['tag_name'].strip('v').split('.')
        if latest_verison[0] > integer_user_version[0]:
            return "There is a major new release!!!"
        elif latest_verison[1] > integer_user_version[1]:
            return "you have a minor new release!!"
        elif latest_verison[2] > integer_user_version[2]:
            return "update available!"
        else:
            return("you are up to date!")
    except urllib.error.URLError:
        return("No internet connection. Unable to Check for Updates...")
    except Exception as e:
        print(e)
def intial_update_checker(user_version):
    integer_user_version = user_version.split('.')
    GitHub_API = "https://api.github.com/repos/jovancherian-source/EnDek/releases/latest"
    try:
        request = urllib.request.Request(GitHub_API, headers={"User-Agent": "EnDek"})
        with urllib.request.urlopen(request, timeout=5) as json_whole_data:
            whole_data = json.loads(json_whole_data.read().decode())
        latest_verison = whole_data["tag_name"].strip("v").split(".")
        
        if latest_verison[0] > integer_user_version[0]:
            return "There is a major new release!!!"
        elif latest_verison[1] > integer_user_version[1]:
            return "you have a minor new release!!"
        elif latest_verison[2] > integer_user_version[2]:
            return "update available!"
    except Exception as e:
        pass

