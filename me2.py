from linepy  import *
#from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from urllib.parse import urlencode
#from MySplit import *
from random import randint
#from toolshed.shell import execute_js
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
noobcoder = LineClient(authToken='ENyTnRXM7FloaTZi3Xc1.P+YYSHMJEwcBF7nhsJZ5mq.+WDozSiy9TUNRHxtLA6uHnNDwYcTjIXmXXBMWW7RYfA=')
noobcoder.log("Auth Token : " + str(noobcoder.authToken))
poll = LinePoll(noobcoder)
call = LineCall(noobcoder)
Imid = noobcoder.profile.mid
loop = asyncio.get_event_loop()
admin =["u4b15403057a60b50eeafae8be20805a0"]
botStart = time.time()
kuciyose = {}
mulai = time.time()

# BERANTAKAN

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}

sppam = {
  "list": [],
  "status": False
}
wait = {
  "autoJoin": True
   }
#=====================================================================
#=====================================================================
#=====================================================================
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "JAVA SCRIPT",
            "iconUrl": "https://i.ibb.co/yqF3RcJ/Screenshot-2019-03-31-21-47-08-964-com-UCMobile-intl-picsay.png",
            "linkUrl": "line://nv/profilePopup/mid=uf19862ec64ac060f75c771ef3f33f1e5"
        }
    }
    sendTemplate(to, data)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1643727178-0XPGAaRX', xyzz)
    token = noobcoder.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, '', annda, 13)    
#====================================================
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('khie/temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('khie/wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
async def noobcoderBot(op):
    try:
#        if settings["restartPoint"] != None:
 #           noobcoder.sendMessage(settings["restartPoint"], 'Activated♪')
  #          settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 13:
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in admin:
                        noobcoder.acceptGroupInvitation(op.param1)
                        xyz = noobcoder.getGroup(to)
                        mem = [c.mid for c in xyz.members]
                        targets = []
                        for x in mem:
                          if x not in ["ud9d27e76bcbf2a8a5bb324c09cf2cd29",noobcoder.profile.mid]:targets.append(x)
                        if targets:
                          imnoob = 'simple.js gid={} token={} app={}'.format(to, noobcoder.authToken, "CHROMEOS\t2.1.5\tDefrizal_OS\t1")
                          for target in targets:
                            imnoob += ' uid={}'.format(target)
                          success = execute_js(imnoob)
                          if success:noobcoder.sendMessage(to, "Success kick %i members." % len(targets))
#=====================================================================
#=====================================================================
        if op.type == 26:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType == 0:
                    if msg.toType == 0 or msg.toType == 2:
                        if cmd == "logout" and sender == noobcoderMID:
                            noobcoder.generateReplyMessage(msg.id)
                            noobcoder.sendReplyMessage(msg.id, to, "Your selfbot has been logout ♪")
                            sys.exit("Logout")
                        elif cmd == "help":
                            noobcoder.sendMessage(to, "Help Message :\n\n1. @kickall\n2. @kick <name>\n3. @bypass\n4. @target on/off\n5. @gc spam <name>\n6. @groups\n7. @reject all")
                        elif cmd == "@kickall":
                          xyz = noobcoder.getGroup(to)
                          mem = [c.mid for c in xyz.members]
                          targets = []
                          for x in mem:
                            if x not in ["ud9d27e76bcbf2a8a5bb324c09cf2cd29",noobcoder.profile.mid]:targets.append(x)
                          if targets:
                            imnoob = 'simple.js gid={} token={} app={}'.format(to, noobcoder.authToken, "CHROMEOS\t2.1.5\tDefrizal_OS\t1")
                            for target in targets:
                              imnoob += ' uid={}'.format(target)
                            success = execute_js(imnoob)
                            if success:noobcoder.sendMessage(to, "Success kick %i members." % len(targets))
                            else:noobcoder.sendMessage(to, "Failed kick %i members." % len(targets))
                          else:noobcoder.sendMessage(to, "Target not found.")
                        elif cmd == "@bypass":
                          xyz = noobcoder.getGroup(to)
                          if xyz.invitee == None:pends = []
                          else:pends = [c.mid for c in xyz.invitee]
                          targp = []
                          for x in pends:
                            if x not in ["ud9d27e76bcbf2a8a5bb324c09cf2cd29",noobcoder.profile.mid]:targp.append(x)
                          mems = [c.mid for c in xyz.members]
                          targk = []
                          for x in mems:
                            if x not in ["ud9d27e76bcbf2a8a5bb324c09cf2cd29",noobcoder.profile.mid]:targk.append(x)
                          imnoob = 'dual.js gid={} token={}'.format(to, noobcoder.authToken)
                          for x in targp:imnoob += ' uid={}'.format(x)
                          for x in targk:imnoob += ' uik={}'.format(x)
                          execute_js(imnoob)
                        elif cmd.startswith("@kick "):
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = noobcoder.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           imnoob = 'simple.js gid={} token={} app={}'.format(to, noobcoder.authToken, "CHROMEOS\t2.1.5\tDefrizal_OS\t1")
                           for x in members:
                               contact = noobcoder.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return noobcoder.sendMessage(to,"not found name "+midn)
                           for target in targets:
                             imnoob += ' uid={}'.format(target)
                           success = execute_js(imnoob)
                        elif cmd.startswith("@gc spam "):
                          nm = text.replace("@gc spam ","")
                          if sppam["list"] != []:
                            imnoob = "spam.js name={} token={}".format(nm,noobcoder.authToken)
                            for target in sppam["list"]:
                              noobcoder.findAndAddContactsByMid(target)
                              imnoob += " uid={}".format(target)
                            success = execute_js(imnoob)
                            if success:noobcoder.sendMessage(to,"Done")
                            else:noobcoder.sendMessage(to,"Error")
                          else:noobcoder.sendMessage(to,"target is empty.")
                        elif cmd == "@target on":
                          sppam["status"] = True
                          noobcoder.sendMessage(to,"send a contact.")
                        elif cmd == "@target off":
                          sppam["status"] = False
                          noobcoder.sendMessage(to,"done.")
                        elif cmd == "@reject all":
                          gids = noobcoder.getGroupIdsInvited()
                          xyzs = []
                          for x in gids:xyzs.append(x)
                          for x in gids:
                            noobcoder.acceptGroupInvitation(x)
                          for x in xyzs:
                            noobcoder.leaveGroup(x)
                          noobcoder.sendMessage(to, "Success reject %i invitation." % len(xyzs))
                        elif cmd == "@groups":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = noobcoder.getGroupIdsJoined()
                            sd = noobcoder.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                sendFooter(to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))

                if msg.contentType == 13 and sppam["status"] == True:
                  if msg.contentMetadata["mid"] not in sppam["list"]:
                    sppam["list"].append(msg.contentMetadata["mid"])
                    noobcoder.sendMessage(to,"user added to list.")
                  else:
                    noobcoder.sendMessage(to,"user already in list.")
#=====================================================================
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                _name = noobcoder.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)

        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
   

def run():
    while True:
        try:
            ops = poll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(noobcoderBot(op))
                   poll.setRevision(op.revision)
        except Exception as e:
            pass #logError(e)
            
if __name__ == "__main__":
    run()
#       ehun.log(error)
 #       traceback.print_tb(error.__trac
