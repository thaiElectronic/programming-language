import requests
import constant
from helper import debug


def get_station_config():
    debug("[INFO] SYNC CONFIG")
    response = requests.get(constant.URL_CONFIG, headers=constant.HEADER)
    sync_config = {"LLVD": 45, "HHTT": 50, "NUM_CURRENT_METER": 4}
    try:
        data = response.json()
        if not data["_error_code"]:
            sync_config = {"LLVD": data["LLVD"], "HHTT": data["HHTT"], "NUM_CURRENT_METER": data["HHTT"]}
    except:
        pass
    debug(response.status_code)
    debug(sync_config)
    return sync_config
