import typing

import requests
import json

WatchlistType = typing.List[typing.Dict]


class MongoWatchlistClient:
    def __int__(self, api_key):
        self._api_key = api_key
        self._url = (
            "https://us-east-1.aws.webhooks.mongodb-realm.com/api/client/"
            "v2.0/app/data-vbrot/service/update_watchlist/incoming_webhook/{endpoint}"
        )

    def update_watchlist(self, watchlist: WatchlistType, db: str):
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

    def get_latest(self, db: str):
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

    def add_records(self, watchlist_items: WatchlistType, db: str):
        """
        Add a records to the watchlist.
        :param watchlist_items:
        :param db:
        :return:
        """
        current_watchlist = self.get_latest(db).json()['watchlist']
        current_watchlist.extend(watchlist_items)
        return self.update_watchlist(current_watchlist, db)

    def remove_records(self, watchlist_items: WatchlistType, db: str):
        """
        Remove records from the watchlist.
        :param watchlist_items:
        :param db:
        :return:
        """
        current_watchlist = self.get_latest(db).json()['watchlist']
        current_watchlist = [item for item in current_watchlist if item not in watchlist_items]
        return self.update_watchlist(current_watchlist, db)
