from django.conf import settings
import requests


class EosBackend(object):
    api_actions_url = settings.NODE + "/v1/history/get_actions"
    base_account = settings.EOS_BASE_ACCOUNT

    def get_actions(self, account_name=base_account):
        url = self.api_actions_url

        payload = "{\"pos\":null,\"account_name\":\"%s\"}" % account_name
        response = requests.request("POST", url, data=payload)

        return response.text