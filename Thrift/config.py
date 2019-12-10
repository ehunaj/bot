# -*- coding: utf-8 -*-
from dit.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN            = 'https://gw.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gw.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gw.line.naver.jp/mh'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440'
    }

    APP_TYPE = ApplicationType._VALUES_TO_NAMES[368]
    APP_VER = "2.1.5"
    CARRIER = '51089, 1-0'
    SYSTEM_NAME = 'LINEprotect'
    SYSTEM_VER = '11.2.5'
    IP_ADDR = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self):
        self.APP_NAME = 'IOS\t8.16.2\tIphone X\t8.1.0'
        self.USER_AGENT = 'Line/7.5.2'
