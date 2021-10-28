import requests
import pandas as pd
import datetime as dt


# GET-запрос на адрес https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod с параметрами
# Пример: https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod?dateFrom=2020-06-01&key=<ключ, выдаваемый поставщику>&limit=1000&rrdid=0&dateto=2020-
# 06-30


class WBExtract:
    default_start_date = dt.datetime(2020, 6, 1)
    service_url = None
    token = None
    limit = None
    rrdid = 0
    has_more = True
    headers = {'Content-Type': 'application/json'}
    client=None

    def __init__(self, url, token, limit =None):
        self.service_url = url
        self.token = token
        self.limit = limit

    def formated_date(self, d):
        return d.isoformat(timespec='milliseconds')

    def params(self):
        params = {'dateFrom': self.formated_date(self.default_start_date),
                  'key': self.token,
                  'dateto': self.formated_date(dt.datetime.now())}

        if self.limit is not None:
            params['limit'] = self.limit
            params['rrdid'] = self.rrdid

        return params

    def has_more_data(self):
       return self.has_more

    def open_session(self):
        self.client = requests.Session()

    def close_session(self):
        self.client.close()

    def read_data (self):

        response = self.client.get(url=self.service_url,
                              params=self.params(),
                              headers=self.headers)

        if response.status_code == 200:
            data_batch = pd.read_json(response.text)

            self.rrdid = data_batch.iloc[-1]['rrd_id']

            if self.limit is not None and data_batch.shape[0] % self.limit == 0:
                self.has_more = True
            else :
                self.has_more = False

            return data_batch

        return None
