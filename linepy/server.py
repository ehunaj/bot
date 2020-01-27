# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re, json, requests, urllib

class LineServer(object):
s Config(object):
    LINE_HOST_DOMAIN            = 'https://gd2.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gd2.line.naver.jp/mh'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
        'ANDROID': '8.14.2',
        'IOS': '9.18.1', #8.14.2',
        'ANDROIDLITE': '2.1.0',
        'BIZANDROID': '1.7.2',
        'BIZIOS': '1.7.5',
        'BIZWEB': '1.0.22',
        'DESKTOPWIN': '5.9.0',
        'DESKTOPMAC': '5.9.0',
        'IOSIPAD': '8.14.2',
        'CHROMEOS': '2.1.5',
        'WIN10': '5.5.5',
        'DEFAULT': '8.11.0'
    }
    USER_AGENT  = 'Line/9.18.1' #7.14.0'
    APP_TYPE    = ApplicationType.IOS
    APP_TYPE    = 'IOS'
    APP_NAME    = 'appName=IOS\t9.18.1\tIOS\t12.4.1'
   # APP_VER     = APP_VERSION[APP_TYPE] if APP_TYPE in APP_VERSION else APP_VERSION['DEFAULT']
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'Ehun'
    SYSTEM_VER  = '12.4.1' #11.2.5'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    #def __init__(self, appType=None):
       # if appType:
            #self.APP_TYPE = appType
            #self.APP_VER = self.APP_VERSION[self.APP_TYPE] if self.APP_TYPE in self.APP_VERSION else self.APP_VERSION['DEFAULT']
        #self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        #self.USER_AGENT = 'Line/%s' % self.APP_VER


  #  }

   # USER_AGENT  = 'Line/7.14.0'
   # APP_TYPE    = ApplicationType.IOS
 #   APP_NAME    = 'IOSIPAD\x097.14.0\x09iPhone_OS\x0911.2.5'
    #APP_NAME    = 'CHROMEOS\t7.14.1\tChrome_OS\t1'
    #APP_NAME    = 'DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0' #IOSIPAD\t7.14.0\tiPhone OS\t11.2.5'
  #  CARRIER     = '51089, 1-0'
    #SYSTEM_NAME = 'Ehun'
   # IP_ADDR     = '8.8.8.8'
  #  EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    _session    = requests.session()
    channelHeaders  = {}
    Headers         = {}

    def __init__(self):
        self.Headers = {}
        self.channelHeaders = {}

    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    def urlEncode(self, url, path, params=[]):
        try:        # Works with python 2.x
            return url + path + '?' + urllib.urlencode(params)
        except:     # Works with python 3.x
            return url + path + '?' + urllib.parse.urlencode(params)

    def getJson(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    def setHeadersWithDict(self, headersDict):
        self.Headers.update(headersDict)

    def setHeaders(self, argument, value):
        self.Headers[argument] = value

    def setChannelHeadersWithDict(self, headersDict):
        self.channelHeaders.update(headersDict)

    def setChannelHeaders(self, argument, value):
        self.channelHeaders[argument] = value

    def additionalHeaders(self, source, newSource):
        headerList={}
        headerList.update(source)
        headerList.update(newSource)
        return headerList

    def optionsContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.options(url, headers=headers, data=data)

    def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data, files=files)

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.get(url, headers=headers, stream=True)

    def deleteContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.delete(url, headers=headers, data=data)

    def putContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.put(url, headers=headers, data=data)
