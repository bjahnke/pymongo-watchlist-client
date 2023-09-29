import requests
import json


class MongoWatchlistClient:
    def __int__(self, api_key):
        self._api_key = api_key
        self._url = (
            "https://us-east-1.aws.webhooks.mongodb-realm.com/api/client/"
            "v2.0/app/data-vbrot/service/update_watchlist/incoming_webhook/{endpoint}"
        )

    def update_watchlist(self, watchlist, db):
        """
        Update the watchlist.
        :param db:
        :param watchlist:
        :return:
        """
        res = requests.post(
            self._url.format(endpoint='update_watchlist'),
            params={'db': db},
            data=json.dumps({'watchlist': watchlist}),
            headers={'Content-Type': 'application/json', 'apiKey': self._api_key}
        )
        return res.json()

    def get_latest(self, db):
        """
        Get the latest watchlist.
        :param db:
        :return:
        """
        res = requests.get(
            self._url.format(endpoint='get_latest'),
            params={'db': db},
            headers={'Content-Type': 'application/json', 'apiKey': self._api_key}
        )
        return res.json()