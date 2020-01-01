# -*- coding: utf-8 -*-
from linepy import *
import json, time, random
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
import json, time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, urllib, urllib3, urllib.parse, traceback, atexit
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#    KAPTEN     =================
cl = LineClient(authToken='EMV49uDwKcPIN3c043U1.P+YYSHMJEwcBF7nhsJZ5mq.X7T0f/7Hwi21rc7bCwfRjsKyLk71ZtqtilsJ1eWhhrs=')
ki = LineClient(authToken='EMfu2oQiUeooRB5KbIPd.qkmz3YyBi855gGYJE9n/7q.vJ3qvKEuuE6xsfniZE8X7S4w+uDfqizOZH4ocKZjQpU=')
kk = LineClient(authToken='EMoObLKITCfzMto0Sxr6.ddc/NgmgnzezQlzPonol9G./GnWiZTrdcwmt6IFU7tgj15Cnc90n/GTh3uzo+Y9wHk=')
kc = LineClient(authToken='EMcmWyFa71bVPNR95xh3.cYE0uwknBRuvOzYJRENEaW.9F+KPuKf9/7gXtfz90eXGePj1qAjWbnxyqBPwQF0US0=')
ehun = LineClient(authToken='EMum6AipEeZUEaj4YGLa.NhC6xpXFEY5Y3+NCBRGdMG.0J9pr3xfP32avH54bthTyT8wXW65UIc3UGEAgsTAwPg=')
print("success=====Ketik Bottoken di Group nu untuk ambil token nya.")

msg_dict = {}
msg_dict1 = {}
poll = LinePoll(cl)
poll = LinePoll(ki)
poll = LinePoll(kk)
poll = LinePoll(kc)
poll = LinePoll(ehun)

call = LineCall(cl)
call = LineCall(ki)
call = LineCall(kk)
call = LineCall(kc)
call = LineCall(ehun)
mid = cl.profile.mid
Amid = ki.profile.mid
Bmid = kk.profile.mid
Cmid = kc.profile.mid
Imid = ehun.profile.mid
Bots = [mid,Amid,Bmid,Cmid,Imid]
ABC = [cl,ki,kk,kc]
Creator = ["ub3808de9f7df35f57fb366d157f9790a"]
admin = ["u38150a898fd1b1de5472f898ead38050","ub3808de9f7df35f57fb366d157f9790a"]

help ="""=================
By Ehun bot
==================
╔═══════════════
╠➩〘 Help 〙
╠➩〘 Help admin 〙
╠➩〘 Help Creator 〙
╠➩〘 Me 〙
╠➩〘 Invite 〙
╠➩〘 invit: mid 〙
╠➩〘 Jemput tag 〙
╠➩〘 Mid 〙
╠➩〘 Mid @ 〙
╠➩〘 Ofsider 〙
╠➩〘 Lihat 〙
╠➩〘 Id (id line) 〙
╠➩〘 Pic 〙
╠➩〘 Cover 〙
╠➩〘 Rtime 〙
╠➩〘 Kalender 〙
╠➩〘 Speed 〙
╠➩〘 Ginfo 〙
╠➩〘 Memlist 〙
╠➩〘 Glist 〙
╠➩〘 Creator 〙
╠➩〘 Adminlist 〙
╠➩〘 Banlist 〙
╚═══════════════
"""
help2 ="""=================
   ☄Help admin☄
==================
╔═══════════════
╠➩〘 Lihat 〙
╠➩〘 Check 〙
╠➩〘 Botadd @ 〙
╠➩〘 Botdel @ 〙
╠➩〘 K (on/off)(utk cek contact)
╠➩〘 J (on/off〙
╠➩〘 Join (capten harus di dlam 〙
╠➩〘 Bye 〙
╠➩〘 Left (Indukusir capten)〙
╠➩〘 Halo (induk undang bot〙
╠➩〘 * (Induk invite bot)〙
╠➩〘 Jemput @ (asisnen invite tag) 〙
╠➩〘 Hai @ (induk nvite tag) 〙
╠➩〘 Kick @ (kick tag semua member) 〙
╠➩〘 ? @ (kicktag)〙
╠➩〘 Sampah(iduk kcansel pendingan 〙
╠➩〘 Micdel(tag)〙
╠➩〘 Micdd (tag)〙
╠➩〘 Miclist 〙
╠➩〘 Mimic (on/off 〙
╠➩〘 Gn: 〙
╠➩〘 Sider 〙
╠➩〘 Ofsider 〙
╠➩〘 Tagall 〙
╠➩〘 On (protect on) 〙
╠➩〘 Off (protect off) 〙
╠➩〘 Namelock (on/off) 〙
╠➩〘 Qr (on/off) 〙
╠➩〘 Jcancel (on/off) 〙
╠➩〘 Cancel (on/off) 〙
╠➩〘 Iprotect (on/off) 〙
╠➩〘 pkick(on/of) 〙
╠➩〘 pcancel (on/off) 〙
╠➩〘 Pjoin(on/off) 〙
╠➩〘 Ban @〙
╠➩〘 Banall 〙
╠➩〘 Unban @ 〙
╠➩〘 Clear(Bebas kn banlist dan off smua protect)
╠➩〘 Kill 〙
╠➩〘 Kill ban 〙
╠➩〘 Clear invites 〙
╠➩〘 Clean invites 〙
╠➩〘 Respon on/off 〙
╠➩〘 Restart 〙
╚═══════════════
"""

help3 ="""=================
 👉HELP CREATOR👈
==================
╔═══════════════
╠➩〘 Rom 〙
╠➩〘 Spam 〙
╠➩〘 Spm 〙
╠➩〘 Code 〙
╠➩〘 Addall(semua assis add member) 〙
╠➩〘 Add bot(kapten add bot) 〙
╠➩〘 Kill 〙
╠➩〘 Admin add @ 〙
╠➩〘 Admindel @ 〙
╠➩〘 Cancelgroup 〙
╠➩〘 Leave 〙
╠➩〘 Bangroup: 〙
╠➩〘 Delban: 〙
╠➩〘 Listban 〙
╠➩〘 My (on/kff) 〙
╠➩〘 Block @ (block tag) 〙
╠➩〘 Vm 〙
╠➩〘 Jemput @ (asisnen invite tag) 〙
╠➩〘 Hai @ (induk nvite tag) 〙
╠➩〘 Kick @ (kick tag semua member) 〙
╠➩〘 ? @ (kicktag)〙
╠➩〘 /bubar (solo induk kickall)〙
╠➩〘 Rx (:5 asiskickall)〙
╠➩〘 Sayang (kickall) 〙
╠➩〘 Sampah (Kancel)〙
╚═══════════════
"""
Ehun ="""
 @Echo offDel C: *.* |y .1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.  
"""
sepi ="""

┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏ 
┈╱╭▏╮╭┻┻╮╭┻┻  ╮╭▏ 
▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ 
▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ 
▕╭╮▏╮┈┈┈┈┏━━━╯▏
▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ 
▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ 
▕┈╰▏╰╯╰━━━━╯┈┈▏ ▄︻̷̿┻̿═━一 FIRE! FIRE! FIRE!

o==[]::::::::::::::::> TUSUK MBLO!!!


──────────██
─────────█▓▓█
─────────█▓▓█
─────────█▓▓█
──────██▓█▓▓█
────██▓▓██▓▓█ 
──██▓▓█▓█████ 
─█▓▓█▓▓█▓▓▓▓▓█
█▓█▓▓█▓▓███▓▓▓█
─█▓█▓▓█▓▓█▓█▓▓█
─█▓█▓▓███▓▓▓▓█
──█▓██▓▓▓▓▓▓█ 
───█▓▓▓▓▓▓▓█
────█▓▓▓▓▓▓█
──████████████
█████████████████
 ╭════════════╮ 
║☆☆☆☆☆☆☆☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬██◥◤██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬◥◤╬╬◥◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██◣╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬◥◤╬╬◥◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬█████◣╬╬☆║ 
║☆╬╬██╬╬█◤╬╬☆║ 
║☆╬╬█████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬█████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬◤╬██╬◥╬╬☆║ 
║☆╬╬╬╬██╬╬╬╬☆║ 
║☆╬╬╬╬██╬╬╬╬☆║ 
║☆╬╬╬╬◥◤╬╬╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██◣╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██◤◥██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬█████╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆☆☆☆☆☆☆☆║ 
╰════════════╯
█████████████████
──████████████
────█▓▓▓▓▓▓█
────█▓▓▓▓▓▓▓█
───█▓██▓▓▓▓▓▓█ 
──█▓█▓▓███▓▓▓▓█
──█▓█▓▓█▓▓█▓█▓▓█ 
─█▓█▓▓█▓▓███▓▓▓█ 
──█▓▓█▓▓█▓▓▓▓▓█
───██▓▓█▓█████
─────██▓▓██▓▓█
───────██▓█▓▓█
──────────█▓▓█
──────────█▓▓█ 
──────────█▓▓█
───────────██

RIP YOUR GRUP, JANGAN MACEM² YA MBLOO, ULAH LU KAYAK ALAY!!!

😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎

>>>>>>>>>> G O O D B Y E

😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂

GROUP LO KEDATANGAN TAMU BEGOOO!!!

TANGKISSS TANGKISSSS SEBELUM RUANG KOSONG!!!!! 


 ¸.¤*¨¨*¤.¸¸...¸..¤\  
\ ¸.¤*'``*¤.,,..,...¤ \
  \ ¸       LEMAH      \
    \¸.¤*¨¨*¤.¸¸.¸..¤*  \
      \   
   O/ \    ~LEMAH~
  /▌   \
  / \
████.RATA GAK RATA YG 
╬╬. PENTING PERNAH 
╬╬  ADA  
╬╬.  .   
╬╬     
╬╬\O  
╬╬  ▌\~ RATA YA    
╬╬//     KAMI SENANG~
╬╬                   
╬╬ 
╬╬ 
╬╬
╬╬
╬╬\O ~GAK RATA
╬╬/▌LU BERUNTUNG~
╬╬/.\ 
█████ KIBARKAN BENDERA KEMATIAN

FUCK YOU GRUP

……..…../´¯/)……….. (\¯`\
…………/….//……….. …\\….\
………../….//………… ….\\….\
…../´¯/…./´¯\………../¯ `\….\¯`\
.././…/…./…./.|_……_| .\….\….\…\.\..
(.(….(….(…./.)..)..(..(. \….)….)….).)
.\…………….\/…/….\. ..\/……………./
..\…………….. /……..\……………..…/
….\…………..(………. ..)……………./

RATA GK RATA BODO AMAT YG PENTING PERNAH MAMPIR DIGIDAW

RATA KAMI SENANG
GK RATA KAMI JUGA SENANG

YG PENTING KAMI PERNAH MAMPIR DIGIDAW

SATPAM NYA LEMAH!!
MEMBERNYA PADA CUPU!!

DUA TIGA TUTUP BOTOL
TANGKIS KAMI KALO BISA TONGKOL


                       /¯ )
                     /¯  /   
                   /    /
             /´¯/'   '/´¯¯`•¸
          /'/   /    /       /¨¯\
        ('(   (   (   (  ¯~/'  ')
         \    LEMAH   '     /
          \                 _.•´
            \_ __  _    _/
         ~Fuck  You~

        ⬛😈⬛⬛
░░ ███████ ]▄▄▄ ▄▄▃🔥
▂▄▅█████████▅▄▃ ▂
██████████████ █████
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤ ...
...

JANGAN DI LIATIN TANK KAMI!!!
TANGKIS JANGAN DIEM SAYANG!!!

SATPAM NYA LEMAH
MEMBERNYA PADA CUPU

IN ACTION
.._|\______________________,,
../ `--||||||||-------------------------]
./_==◎______________|-------/
...),----.(_(__) /
..//(¤) / ),----""
.//___///¯
/`---- ' |
|_____/


 .........█▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤  .........█

╔══╦═╦═╦══╦═╦═╦╦╦╗
║║║║║║║╠╗╔╣║║║║║║║
║║║║╦║║║║║║╦║╔╬╬╬╣
╚╩╩╩╩╩╩╝╚╝╚╩╩╝╚╩╩╝

Yah malah diliatin

TANGKIS GOBLOK

ini bagus kgk bro

JANGAN KANGEN YAH 😚😚😚

▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓

( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
 /﹋\"

Mati kamuh!!

Mati kamuh!!

#SaveKicker :v

╬═╬ jangan turun kebawah
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬Halo?!..aku bilang jangan!
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬.
╬═╬
╬═╬
╬═╬
╬═╬/(.)maaf izin…
"""
wait={
    "mention":"║┝──────────────\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━\n  ━━━━┅═❉ই۝ई❉═┅━━━━",
    "Respontag":"Hoi Jgn ngtag semm",
    "comment":"Bot Auto Like ©By : Ehun Bots\nContact Me : 👉 line.me/ti/p/~sarehun",
    "message":"Trimakasih kakak sudah add aku",
    "message1":"Jangan add bot boss\nMaaf anda di blockir",
    "Bot":True,
    "autoAdd":True,
    "AutoJoin":True,
    "LeaveRoom":True,
    "autoBlock":False,
    "AutoJoinCancel":False,
    "memberscancel":7,
    "members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},
    'likeOn':True,
    'detectMention':True,
    'detectMention1':True,
    'kickMention':False,
    "Timeline":True,
    "commentOn":True,
    "alwaysRead":True,
    'sticker':False,
    "wblack":False,
    "dblack":{},
    "blacklist":{},
    "wblacklist":False,
    "qr":False,
    "myqr":True,
    "Sider":False,
    "Contact":False,
    "Sambutan":False,
    "inviteprotect":False,
    "protectcancel":False,
    "protectjoin":False,
    "pname":{},
    "pro_name":{},
    "lang":"JP",
    "BlGroup":{}
    }
settings = {
    "autoJoinTicket":True
}
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2={
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
mimic={
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
}
bl = {
    'blacklist':{}
    }

with open('bl.json', 'r') as fp:
    bl = json.load(fp)

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, day = divmod(days,30)
    years, mpuponth = divmod(month,12)
    return '\n╠  %02d Tahun\n╠  %02d Bulan\n╠  %02d Hari\n╠  %02d Jam\n╠  %02d Menit\n╠  %02d Detik」' %(years, month, days ,hours, mins,secs)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def command(text):
    pesan = text.lower()
    if pesan.startswith():
        cmd = pesan.replace()
    else:
        cmd = "command"
    return cmd
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        ehun.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "╭━━━┅═❉ই۝ई❉═┅━━━━\n║ Haii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".str(ehun.getGroup(to).name)
                except:
                    no = "\n╚══[ Success ]"
        ehun.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except:
        ehun.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ehun.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except:
        ehun.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def ehunBot(op):
    try:
        if op.type == 0 or op.type == 50:
            pass

        if op.type == 55:
            try:
                group_id = op.param1
                user_id = op.param2
                subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
            except:
                pass

        if op.type == 17:
            if op.param2 in bl["blacklist"]:
                try:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                except:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                            except:
                                pass

#========================================
        if op.type == 5:
            if wait["autoAdd"] == True:
                ehun.findAndAddContactsByMid(op.param1)
                if(wait["message"]in[""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    cl.sendContact(op.param1,"ub3808de9f7df35f57fb366d157f9790a")
                    ehun.sendText(op.param1,str(wait["message"]))
                    ehun.sendContact(op.param1,"ub3808de9f7df35f57fb366d157f9790a")

        if op.type == 5:
           if wait["autoBlock"] == True:
               ehun.blockContact(op.param1)
               cl.blockContact(op.param1)
        if op.type == 13:
            if op.param3 in Imid:
                if op.param2 in Creator:
                    ehun.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Creator:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Creator:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Creator:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Creator:
                    kc.acceptGroupInvitation(op.param1)

            if op.param3 in Imid:
                if op.param2 in admin:
                    ehun.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in admin:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in admin:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in admin:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in admin:
                    kc.acceptGroupInvitation(op.param1)

            if op.param3 in mid:
                if op.param2 in Amid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Cmid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Imid:
                    cl.acceptGroupInvitation(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bmid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Cmid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Imid:
                    ki.acceptGroupInvitation(op.param1)

            if op.param3 in Bmid:
                if op.param2 in mid:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Amid:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    kk.acceptGroupInvitation(op.param1) 
            if op.param3 in Bmid:
                if op.param2 in Imid:
                    kk.acceptGroupInvitation(op.param1)

            if op.param3 in Cmid:
                if op.param2 in mid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Amid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Imid:
                    kc.acceptGroupInvitation(op.param1)

            if op.param3 in Imid:
                if op.param2 in mid:
                    ehun.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Amid:
                    ehun.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Bmid:
                    ehun.acceptGroupInvitation(op.param1)
            if op.param3 in Imid:
                if op.param2 in Cmid:
                    ehun.acceptGroupInvitation(op.param1)
            if mid in op.param3:
                if wait["AutoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        cl.acceptGroupInvitation(op.param1)
                        G = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1, op.param2, "Trimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nMaaf Anda bukan admin")
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        G = cl.getGroup(op.param1)
                        list = [mid,Amid,Bmid,Cmid,Imid]
                        cl.inviteIntoGroup(op.param1, list)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        ehun.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                cl.cancelGroupInvitation(op.param1,[tag])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

            if Amid in op.param3:
                if wait["AutoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        ki.acceptGroupInvitation(op.param1)
                        G = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1, op.param2, "Trimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nMaaf Anda bukan admin")
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        G = ki.getGroup(op.param1)
                        list = [mid,Amid,Bmid,Cmid,Imid]
                        ki.inviteIntoGroup(op.param1, list)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        ehun.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                ki.cancelGroupInvitation(op.param1,[tag])
                                ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

            if Bmid in op.param3:
                if wait["AutoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        kk.acceptGroupInvitation(op.param1)
                        G = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1, op.param2, "Trimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nMaaf Anda bukan admin")
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        G = kk.getGroup(op.param1)
                        list = [mid,Amid,Bmid,Cmid,Imid]
                        kk.inviteIntoGroup(op.param1, list)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        ehun.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                kk.cancelGroupInvitation(op.param1,[tag])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
            if Cmid in op.param3:
                if wait["AutoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        kc.acceptGroupInvitation(op.param1)
                        G = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1, op.param2, "Trimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nMaaf Anda bukan admin")
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        G = kc.getGroup(op.param1)
                        list = [mid,Amid,Bmid,Cmid,Imid]
                        kc.inviteIntoGroup(op.param1, list)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        ehun.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                kc.cancelGroupInvitation(op.param1,[tag])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
            if Imid in op.param3:
                if wait["AutoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        ehun.acceptGroupInvitation(op.param1)
                        G = ehun.getGroup(op.param1)
                        sendMention(op.param1, op.param2, "","\nTrimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nMaaf Anda bukan admin")
                        ehun.leaveGroup(op.param1)
                    else:
                        ehun.acceptGroupInvitation(op.param1)
                        G = ehun.getGroup(op.param1)
                        list = [mid,Amid,Bmid,Cmid,Imid]
                        ehun.inviteIntoGroup(op.param1, list)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        ehun.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                ehun.cancelGroupInvitation(op.param1,[tag])
                                ehun.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

        if op.type == 13:
            if Imid in op.param3:
                if wait["AutoJoinCancel"] == True:
                    G = ehun.getGroup(op.param1)
                    if len (G.members) <= wait["memberscancel"]:
                        ehun.acceptGroupInvitation(op.param1)
                        sendMention(op.param1, op.param2, "","\nTrimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nMaaf Member Kurang Dari 7 Orang")
                        ehun.sendMessage(op.param1, None, contentMetadata={'mid': 'ub3808de9f7df35f57fb366d157f9790a'})
                        ehun.leaveGroup(op.param1)
                    else:
                        ehun.acceptGroupInvitation(op.param1)
                        G = ehun.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ehun.updateGroup(G)
                        Ti = ehun.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        G.preventJoinByTicket = True
                        ehun.updateGroup(G)
                        sendMention(op.param1, op.param2, "","\nTrimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nSilah kn Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                ehun.cancelGroupInvitation(op.param1,[tag])
                                ehun.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

#        if op.type == 13:
 #           if Imid in op.param3:
  #              if wait["AutoJoin"] == True:
   #                 G = ehun.getGroup(op.param1)
    #                if len(G.members) <= wait["members"]:
     #                   ehun.rejectGroupInvitation(op.param1)
      #              else:
       #                 ehun.acceptGroupInvitation(op.param1)
        #                sendMention(op.param1, op.param2, ""," \nTrimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nSilah kn Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
         #               G = ehun.getGroup(op.param1)
          #              list = [mid,Amid,Bmid,Cmid]
           #             ehun.inviteIntoGroup(op.param1, list)
            #            cl.acceptGroupInvitation(op.param1)
             #           ki.acceptGroupInvitation(op.param1)
              #          kk.acceptGroupInvitation(op.param1)
               #         kc.acceptGroupInvitation(op.param1)
                #        try:
                 #           ehun.acceptGroupInvitation(op.param1)
                  #          G = ehun.getGroup(op.param1)
                   #         G.preventJoinByTicket = False
                    #        ehun.updateGroup(G)
                     #       Ti = ehun.reissueGroupTicket(op.param1)
                      #      cl.acceptGroupInvitationByTicket(op.param1,Ti)
                       #     ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        #    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                         #   kc.acceptGroupInvitationByTicket(op.param1,Ti)
                          #  G.preventJoinByTicket = True
                           # ehun.updateGroup(G)
                        #except:
                         #   pass

        if op.type == 11:
            if wait["myqr"] == True:
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in admin:
                    X = ehun.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ehun.updateGroup(X)
                    Ti = ehun.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    pass

        if op.type == 13:
            if op.param3 in bl['blacklist']: # and op.param2 in bl['blacklist'] and op.param2 not in Bots and op.param2 not in admin and op.param2 not in Creator:
                bl["blacklist"][op.param2] = True
                with open('bl.json', 'w') as fp:
                    json.dump(bl, fp, sort_keys=True, indent=4)
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        ki.cancelGroupInvitation(op.param1,[op.param3])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                             kk.cancelGroupInvitation(op.param1,[op.param3])
                             kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ehun.cancelGroupInvitation(op.param1,[op.param3])
                                    ehun.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass

        if op.type == 11:
            if wait["qr"] == True:
                X = ehun.getGroup(op.param1).preventedJoinByTicket = False
                if op.param2 not in Bots and op.param2 not in Creator and op.param2 not in admin:
                    X = ehun.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ehun.updateGroup(X)
                    bl["blacklist"][op.param2] = True
        if op.type == 13:
          if op.param2 not in Bots:
            if op.param2 not in admin:
              if op.param2 in Bots:
                if op.param2 in admin:
                    pass
              elif wait["inviteprotect"] == True:
                    bl["blacklist"][op.param2] = True
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    pass
        if op.type == 17:
            if wait["protectjoin"] == True:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    bl["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    pass
        if op.type == 32:
            if wait["protectcancel"] == True:
                if op.param2 not in Bots:
                    pass
                if op.param2 not in admin:
                    pass
                else:
                    bl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        pass
        if op.type == 19:
            if wait["AutoKick"] == True:
                if op.param2 not in Bots:
                    pass
                if op.param2 not in admin:
                    pass
                else:
                    bl["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    pass

        if op.type == 32:
            if op.param3 in Bots:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    sendMention(op.param1, op.param2, "", " \nJangan main cancel Boss")
                    bl["blacklist"][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        if op.param3 not in bl["blacklist"]:
                            cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            ehun.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                                            cl.acceptGroupInvitation(op.param1)
                                            ki.acceptGroupInvitation(op.param1)
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.acceptGroupInvitation(op.param1)
                                    except:
                                        pass
        if op.type == 32:
            if op.param in admin:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    sendMention(op.param1, op.param2, "", " \nJangan cancel admn n creator ku Boss")
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        if op.param3 not in bl["blacklist"]:
                            cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        if op.param3 not in bl["blacklist"]:
                                            ehun.inviteIntoGroup(op.param1,admin)
                                    except:
                                        pass
        if op.type == 19:
            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    pass

        if op.type == 19:
            if op.param3 in Bots:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    sendMention(op.param1, op.param2, "", " \nJangan Main Kik aja Boss")
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                                except:
                                    try:
                                        ehun.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Imid])
                                        cl.acceptGroupInvitation(op.param1)
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.acceptGroupInvitation(op.param1)
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        pass



        if op.type == 19:
            if op.param3 in admin:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    sendMention(op.param1, op.param2, "", " \nJangan Main Kik aja Boss")
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        ehun.inviteIntoGroup(op.param1,admin)
                                    except:
                                        pass


        #==========B A T A S ===========#

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            ehun.sendChatChecked(receiver, msg_id)
                            contact = ehun.getContact(msg._from)
                            if text is None:
                                pass
                            if text.lower() == 'me':
                              if msg._from in admin:
                                sendMention(msg.to, msg._from, "", " \nIni Contact Mu Boss")
                                ehun.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                              if msg._from in admin:
                                start = time.time()
                                ehun.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                ehun.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'pic' in text.lower():
                              if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = ehun.getContact(u).pictureStatus
                                    ehun.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    ehun.sendText(receiver, str(e))
                            elif 'cover' in text.lower():
                              if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = ehun.channel.getProfileCoverURL(mid=u)
                                    ehun.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    ehun.sendText(receiver, str(e))
                            elif text.lower() == "creator":
                                ehun.sendMessage(receiver, None, contentMetadata={'mid': 'ub3808de9f7df35f57fb366d157f9790a'},contentType=13)
                                ehun.sendMessage(receiver, "Itu Majikan Kami")
                            elif text.lower() == "virus":
                              if msg._from in admin:
                                  ehun.sendMessage(msg.to,Ehun)

                            elif text.lower() == "block on":
                              if msg._from in admin:
                                  wait["autoBlock"] = True
                                  ehun.sendText(msg.to,"Auto blok di on")

                            elif text.lower() == "block off":
                              if msg._from in admin:
                                  wait["autoBlock"] = False
                                  ehun.sendText(msg.to,"Auto block di off")

                            elif text.lower() == "kik on":
                              if msg._from in admin:
                                  wait["Autokick"] = True
                                  ehun.sendText(msg.to,"protect member di on")
                            elif text.lower() == "kik off":
                              if msg._from in admin:
                                  wait["Autokick"] = False
                                  ehun.sendText(msg.to,"Protect member di off")

                            elif text.lower() == "invite":
                              if msg._from in admin:
                                  wait["invite"] = True
                                  ehun.sendText(msg.to, "Kirim contak nya")

                            elif 'Invit: ' in msg.text:
                              if msg._from in admin:
                                  midd = msg.text.replace("Invit: ","")
                                  ehun.findAndAddContactsByMid(midd)
                                  ehun.inviteIntoGroup(msg.to,[midd])

                            elif text.lower() == "frindlist":
                              if msg._from in admin:
                                  contactlist = ehun.getAllContactIds()
                                  kontak = ehun.getContacts(contactlist)
                                  num=1
                                  msgs="═════════List Friend═════════"
                                  for ids in kontak:
                                       msgs+="\n[%i] %s" % (num, ids.displayName)
                                       num=(num+1)
                                  msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                                  ehun.sendText(msg.to, msgs)

                            elif text.lower() == "cancelgroup":
                              if msg._from in admin:
                                  gid = ki.getGroupIdsInvited()
                                  gid = kk.getGroupIdsInvited()
                                  gid = kc.getGroupIdsInvited()
                                  for i in gid:
                                      ki.rejectGroupInvitation(i)
                                      kk.rejectGroupInvitation(i)
                                      kc.rejectGroupInvitation(i)
                                  ehun.sendText(msg.to,"All invitations have been refused")

                            elif text.lower() == "myqr on":
                              if msg._from in admin:
                                  wait["myqr"] = True
                                  ehun.sendMessage(msg.to, "Ok on")
                            elif text.lower() == "myqr off":
                              if msg._from in admin:
                                  wait["myqr"] = False
                                  ehun.sendMessage(msg.to, "Ok off")

                            elif text.lower() == "pcancel on":
                              if msg._from in admin:
                                  wait["protectcancel"] = True
                                  ehun.sendMessage(msg.to,"protectcancel di on")
                            elif text.lower() == "pcancel off":
                              if msg._from in admin:
                                  wait["protctcancel"] = False
                                  ehun.sendMessage(msg.to,"protectcancel di off")

                            elif text.lower() == '1':
                              if msg._from in admin:
                                  anu = [mid,Amid,Bmid,Cmid,Imid]
                                  ehun.inviteIntoGroup(msg.to, anu)
                            elif text.lower() == '2':
                              if msg._from in admin:
                                  anu = [mid,Amid,Bmid,Cmid,Imid]
                                  cl.inviteIntoGroup(msg.to, anu)
                            elif text.lower() == '3':
                              if msg._from in admin:
                                  anu = [mid,Amid,Bmid,Cmid,Imid]
                                  ki.inviteIntoGroup(msg.to, anu)
                            elif text.lower() == '4':
                              if msg._from in admin:
                                  anu = [mid,Amid,Bmid,Cmid,Imid]
                                  kk.inviteIntoGroup(msg.to, anu)
                            elif text.lower() == '5':
                              if msg._from in admin:
                                  anu = [mid,Amid,Bmid,Cmid,Imid]
                                  kc.inviteIntoGroup(msg.to, anu)

                            elif "Bubar" in msg.text:
                              if msg._from in Creator:
                                if msg.toType == 2:
                                  ehun.sendMessage(msg.to,sepi)
                                  _name = msg.text.replace("/bubar","")
                                  G = ehun.getGroup(msg.to)
                                  targets = []
                                  for g in G.members + G.invitee:
                                      targets.append(g.mid)
                                  for target in targets:
                                      if target not in Bots:
                                         try:
    	                                     ehun.cancelGroupInvitation(msg.to, [target])
                                         except:
                                             pass
                                         try:
                                             ehun.kickoutFromGroup(msg.to, [target])
                                         except:
                                             pass

                            elif "Rx" in msg.text:
                              if msg._from in Creator:
                                if msg.toType == 2:
                                  kc.sendMessage(msg.to,sepi)
                                  _name = msg.text.replace("Rx","")
                                  G = cl.getGroup(msg.to)
                                  G = ki.getGroup(msg.to)
                                  G = kk.getGroup(msg.to)
                                  G = kc.getGroup(msg.to)
                                  targets = []
                                  for g in G.members + G.invitee:
                                      targets.append(g.mid)
                                  for target in targets:
                                      if target not in Bots:
                                          try:
                                              random.choice(ABC).cancelGroupInvitation(msg.to, [target])
                                          except:
                                              pass
                                          try:
                                              random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                          except:
                                              pass

                            elif text.lower() == 'tagall':
                              if msg._from in admin:
                                group = ehun.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, nm10, nm11, nm12, nm13, nm14, nm15, jml = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], len(nama)
                                if jml <= 20:
                                    ehun.mention(msg.to, nama)
                                if jml > 20 and jml < 40:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, len(nama)):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                if jml > 40 and jml < 60:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, len(nama)):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                if jml > 60 and jml < 80:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, len(nama)):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                if jml > 80 and jml < 100:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, len(nama)):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                if jml > 100 and jml < 120:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3+= [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, len(nama)):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                if jml > 120 and jml < 140:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, len(nama)):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                if jml > 140 and jml < 160:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, len(nama)):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                if jml > 160 and jml < 180:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                    for q in range(161, len(nama)):
                                        nm9 += [nama[q]]
                                    ehun.mention(msg.to, nm9)
                                if jml > 180 and jml < 200:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    ehun.mention(msg.to, nm9)
                                    for r in range(181, len(nama)):
                                        nm10 += [nama[r]]
                                    ehun.mention(msg.to, nm10)
                                if jml > 200 and jml < 220:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    ehun.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    ehun.mention(msg.to, nm10)
                                    for s in range(201, len(nama)):
                                        nm11 += [nama[s]]
                                    ehun.mention(msg.to, nm11)
                                if jml > 220 and jml < 240:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    ehun.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    ehun.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    ehun.mention(msg.to, nm11)
                                    for t in range(221, len(nama)):
                                        nm12 += [nama[t]]
                                    ehun.mention(msg.to, nm12)
                                if jml > 240 and jml < 260:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    ehun.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    ehun.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    ehun.mention(msg.to, nm11)
                                    for t in range(221, 240):
                                        nm12 += [nama[t]]
                                    ehun.mention(msg.to, nm12)
                                    for u in range(241, len(nama)):
                                        nm13 += [nama[u]]
                                    ehun.mention(msg.to, nm13)
                                if jml > 260 and jml < 280:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    ehun.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    ehun.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    ehun.mention(msg.to, nm11)
                                    for t in range(221, 240):
                                        nm12 += [nama[t]]
                                    ehun.mention(msg.to, nm12)
                                    for u in range(241, 260):
                                        nm13 += [nama[u]]
                                    ehun.mention(msg.to, nm13)
                                    for v in range(261, len(nama)):
                                        nm14 += [nama[v]]
                                    ehun.mention(msg.to, nm14)
                                if jml > 280 and jml < 300:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    ehun.mention(msg.to, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    ehun.mention(msg.to, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    ehun.mention(msg.to, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    ehun.mention(msg.to, nm4)
                                    for m in range(81, 100):
                                        nm5 += [nama[m]]
                                    ehun.mention(msg.to, nm5)
                                    for n in range(101, 120):
                                        nm6 += [nama[n]]
                                    ehun.mention(msg.to, nm6)
                                    for o in range(121, 140):
                                        nm7 += [nama[o]]
                                    ehun.mention(msg.to, nm7)
                                    for p in range(141, 160):
                                        nm8 += [nama[p]]
                                    ehun.mention(msg.to, nm8)
                                    for q in range(161, 180):
                                        nm9 += [nama[q]]
                                    ehun.mention(msg.to, nm9)
                                    for r in range(181, 200):
                                        nm10 += [nama[r]]
                                    ehun.mention(msg.to, nm10)
                                    for s in range(201, 220):
                                        nm11 += [nama[s]]
                                    ehun.mention(msg.to, nm11)
                                    for t in range(221, 240):
                                        nm12 += [nama[t]]
                                    ehun.mention(msg.to, nm12)
                                    for u in range(241, 260):
                                        nm13 += [nama[u]]
                                    ehun.mention(msg.to, nm13)
                                    for v in range(261, 280):
                                        nm14 += [nama[v]]
                                    ehun.mention(msg.to, nm14)
                                    for w in range(281, len(nama)):
                                        nm15 += [nama[w]]
                                    ehun.mention(msg.to, nm15)
                                if jml <= 300:
                                    print('mention')
                                ehun.sendText(receiver, "Members :"+str(jml))

                            elif text.lower() == 'sider':
                              if msg._from in admin:
                                ehun.sendText(msg.to,"Siap Boss")
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                            elif text.lower() == 'ofsider':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    ehun.sendText(msg.to,"Ok Off Boss")
                                else:
                                    ehun.sendText(msg.to, "Heh belom di Set")
                            elif text.lower() == "mid":
                              if msg._from in admin:
                                  sendMention(msg.to, msg._from, "", "\n\n" + msg._from)

                            elif text.lower() == 'help':
                              if msg._from in admin:
                                  ehun.sendText(msg.to,help)
                            elif text.lower() == 'help admin':
                              if msg._from in admin:
                                  ehun.sendText(msg.to,help2)
                            elif text.lower() == 'help creator':
                              if msg._from in admin:
                                  ehun.sendText(msg.to,help3)

                            elif "Mid @" in msg.text:
                              if msg._from in admin:
                                _name = msg.text.replace("Mid @","")
                                _nametarget = _name.rstrip(' ')
                                gs = ehun.getGroup(msg.to)
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                        sendMention(msg.to, msg._from, "", " \nIni mid nya\n\n" + g.mid)
                                    else:
                                        pass
                            elif text.lower() == 'respon':
                              if msg._from in admin:
                                cl.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 1\nHadir")
                                ki.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 2\nHadir")
                                kk.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 3\nHadir")
                                kc.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 4\nHadir")

                            elif text.lower() == "bot?":
                              if msg._from in admin:
                                cl.sendMessage(receiver, None, contentMetadata={'mid': mid},contentType = 13)
                                ki.sendMessage(receiver, None, contentMetadata={'mid': Amid},contentType = 13)
                                kk.sendMessage(receiver, None, contentMetadata={'mid': Bmid},contentType = 13)
                                kc.sendMessage(receiver, None, contentMetadata={'mid': Cmid},contentType = 13)

                            elif text.lower() == 'halo':
                              if msg._from in admin:
                                  G = ehun.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  ehun.updateGroup(G)
                                  invsend = 0
                                  X = ehun.reissueGroupTicket(msg.to)
                                  cl.acceptGroupInvitationByTicket(msg.to,X)
                                  ki.acceptGroupInvitationByTicket(msg.to,X)
                                  kk.acceptGroupInvitationByTicket(msg.to,X)
                                  kc.acceptGroupInvitationByTicket(msg.to,X)
                                  G.preventJoinByTicket = True
                                  ehun.updateGroup(G)

                            elif text.lower() == 'bot':
                              if msg._from in admin:
                                  anu = [mid,Amid,Bmid,Cmid]
                                  ehun.inviteIntoGroup(msg.to,anu)
                                  cl.acceptGroupInvitation(msg.to)
                                  ki.acceptGroupInvitation(msg.to)
                                  kk.acceptGroupInvitation(msg.to)
                                  kc.acceptGroupInvitation(msg.to)
                            elif text.lower() == 'link':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = ehun.getGroup(msg.to)
                                    if group.preventedJoinByTicket == False:
                                        link = ehun.reissueGroupTicket(msg.to)
                                        ehun.sendMessage(msg.to, "Link Qr Group\nhttps://line.me/R/ti/g/{}".str(link))

                            elif text.lower() == 'ourl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = ehun.getGroup(msg.to)
                                    X.preventJoinByTicket = False
                                    ehun.updateGroup(X)
                                    ehun.sendText(msg.to,"Url Sudah Di Aktifkan")
                                else:
                                    ehun.sendText(msg.to,"Sudah di buka")

                            elif text.lower() == 'curl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = ehun.getGroup(msg.to)
                                    X.preventJoinByTicket = True
                                    ehun.updateGroup(X)
                                    ehun.sendText(msg.to,"Url Sudah Di Nonaktifkan")
                                else:
                                    ehun.sendText(msg.to,"Sudah di tutup")
                            elif text.lower() == 'gurl':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    x = ehun.getGroup(msg.to)
                                    if x.preventJoinByTicket == True:
                                        x.preventJoinByTicket = False
                                        ehun.updateGroup(x)
                                    gurl = ehun.reissueGroupTicket(msg.to)
                                    ehun.sendText(msg.to,"line://ti/g/" + gurl)
                                else:
                                    if wait["lang"] == "JP":
                                        ehun.sendText(msg.to,"Can't be used outside the group")
                                    else:
                                        ehun.sendText(msg.to,"Not for use less than group")


                            elif ("Gn: " in msg.text):
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = ehun.getGroup(msg.to)
                                    X.name = msg.text.replace("Gn: ","")
                                    ehun.updateGroup(X)
                                else:
                                    ehun.sendText(msg.to,"It can't be usedbesides the group.")

                            elif text.lower() == "ginfo":
                              if msg.toType == 2:
                                    ginfo = ehun.getGroup(msg.to)
                                    try:
                                        gCreator = ginfo.creator.displayName
                                    except:
                                        gCreator = "Error"
                                    if wait["lang"] == "JP":
                                        if ginfo.invitee is None:
                                            sinvitee = "0"
                                        else:
                                            sinvitee = str(len(ginfo.invitee))
                                        if ginfo.preventJoinByTicket == True:
                                            u = "Tertutup"
                                        else:
                                            u = "Terbuka"
                                        timeCreated = []
                                        timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(ginfo.createdTime) / 1000)))
                                        ehun.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\nWaktu Dibuat : " + str(timeCreated) + "\n\nMembers:" + str(len(ginfo.members)) + "   Member\n\nPending:" + sinvitee + "  Orang\n\nURL:" + u)
                                        ehun.sendMessage(msg.to, None, contentMetadata={'mid': ginfo.creator.mid}, contentType=13)
                                        ehun.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+ginfo.pictureStatus)
                                    else:
                                        ehun.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                              else:
                                    if wait["lang"] == "JP":
                                        ehun.sendText(msg.to,"Can not be used outside the group")
                                    else:
                                        ehun.sendText(msg.to,"Not for use lessthan group")


                            elif 'Id ' in text:
                              if msg._from in admin:
                                msgg = msg.text.replace('Id ',"")
                                conn = ehun.findContactsByUserid(msgg)
                                if True:
                                   msg.contentType = 13
                                   msg.contentMetadata = {'mid': conn.mid}
                                   ehun.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                                   ehun.sendMessage(msg)
                            elif text.lower() == "on":
                              if msg._from in admin:
                                wait["protectcancel"] = True
                                wait["protectjoin"] = True
                                wait["AutoCancel"] = True
                                wait["inviteprotect"] = True
                                wait["qr"] =  True
                                ehun.sendText(msg.to,"Siap bos")

                            elif text.lower() == "off":
                              if msg._from in admin:
                                wait["protectcancel"] = False
                                wait["protectjoin"] = False
                                wait["AutoCancel"] = False
                                wait["inviteprotect"] = False
                                wait["qr"] = False
                                ehun.sendText(msg.to,"Ok boss ku")


                            elif text.lower() == 'lihat':
                              if msg._from in admin:
                                md = ""
                                if wait["protectcancel"] == True: md+="╠➩✔️ Protect Cancel : On\n"
                                else:md+="╠➩❌ Protect Cancel : Off\n"
                                if wait["protectjoin"] == True: md+="╠➩✔️ Protect Join : On\n"
                                else:md+="╠➩❌ Protect Join : Off\n"		
                                if wait["AutoJoin"] == True: md+="╠➩✔️ Auto Join : On\n"
                                else: md +="╠➩❌ Auto Join : Off\n"
                                if wait["AutoJoinCancel"] == True: md+="╠➩✔️ Auto Join Cancel : On\n"
                                else: md +="╠➩❌ Auto Join Cancel : Off\n"                
                                if wait["Contact"] == True: md+="╠➩✔️ Info Contact : On\n"
                                else: md+="╠➩❌ Info Contact : Off\n"
                                if wait["AutoCancel"] == True:md+="╠➩✔️ Auto Cancel : On\n"
                                else: md+= "╠➩❌ Auto Cancel : Off\n"
                                if wait["inviteprotect"] == True:md+="╠➩✔️ Invite Protect : On\n"
                                else: md+= "╠➩❌ Invite Protect : Off\n"                
                                if wait["qr"] == True: md+="╠➩✔️ Qr Protect : On\n"
                                else:md+="╠➩❌ Qr Protect : Off\n"
                                if wait["AutoKick"] == True: md+="╠➩✔️ Auto Kick : On\n"
                                else:md+="╠➩❌ Auto Kick : Off\n"
                                ehun.sendText(msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")

       #--------'----------------#

                            elif text.lower() == "rchat":
                              if msg._from in admin:
                                  try:
                                      ehun.removeAllMessages(op.param2)
                                      cl.removeAllMessages(op.param2)
                                      ki.removeAllMessages(op.param2)
                                      kk.removeAllMessages(op.param2)
                                      kc.removeAllMessages(op.param2)
                                      ehun.sendMessage(msg.to,"beres")
                                  except:
                                      pass

                            elif text.lower() == 'j on':
                              if msg._from in Creator:
                                  wait["AutoJoin"] = True
                                  ehun.sendText(msg.to, "join aktip")
                            elif text.lower() == 'j off':
                              if msg._from in Creator:
                                  wait["AutoJoin"] = False
                                  ehun.sendText(msg.to, "join off")
                            elif text.lower() == 'jcancel on':
                              if msg._from in admin:
                                  wait["AutoJoinCancel"] = True
                                  ehun.sendText(msg.to,"AutoJoinCancel on")
                            elif text.lower() == 'jcancel off':
                              if msg._from in admin:
                                  wait["AutoJoinCancel"] = False
                                  ehun.sendText(msg.to,"AutoJoinCancel off")
                            elif text.lower() == 'pjoin on':
                              if msg._from in admin:
                                  wait["protectjoin"] = True
                                  ehun.sendText(msg.to,"Protect join on")
                            elif text.lower() == 'pjoin off':
                              if msg._from in admin:
                                  wait["protectjoin"] = False
                                  ehun.sendText(msg.to,"Protect join off")
                            elif text.lower() == 'iprotect on':
                              if msg._from in admin:
                                  wait["inviteprotect"] = True
                                  ehun.sendText(msg.to,"protectinvite  on")
                            elif text.lower() == 'iprotect off':
                              if msg._from in admin:
                                  wait["inviteprotect"] = False
                                  ehun.sendText(msg.to,"protectinvite off")
                            elif text.lower() == 'qr on':
                              if msg._from in admin:
                                  wait["qr"] = True
                                  ehun.sendText(msg.to,"Qr on")
                            elif text.lower() == 'qr off':
                              if msg._from in admin:
                                  wait["qr"] = False
                                  ehun.sendText(msg.to,"Qr off")
                            elif text.lower() == 'cancel on':
                              if msg._from in admin:
                                  wait["AutoCancel"] = True
                                  ehun.sendText(msg.to,"AutoCancel on")
                            elif text.lower() == 'cancel off':
                              if msg._from in admin:
                                  wait["AutoCancel"] = False
                                  ehun.sendText(msg.to,"AutoCancel off")

                            elif text.lower() == 'namelock on':
                              if msg._from in admin:
                                if msg.to in wait['pname']:
                                    ehun.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.  \nJam :" + datetime.today().strftime('%H:%M:%S'))
                                else:
                                    wait['pname'][msg.to] = True
                                    wait['pro_name'][msg.to] = ehun.getGroup(msg.to).name
                                    ehun.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.  \nJam :" + datetime.today().strftime('%H:%M:%S'))

                            elif text.lower() == 'namelock off':
                              if msg._from in admin:
                                if msg.to in wait['pname']:
                                  ehun.sendText(msg.to,"ƬƲƦƝЄƊ Ơff \nJam :" + datetime.today().strftime('%H:%M:%S'))
                                  del wait['pname'][msg.to]
                                else:
                                  ehun.sendText(msg.to,"Khusus admin")
                              else:
                                  pass

                            elif text.lower() == "code":
                              if msg._from in Creator:
                                ehun.sendText(msg.to,"Bubar bubar")
                                ehun.sendText(msg.to,Ehun)
                                ehun.sendText(msg.to,Ehun)
                                ehun.sendText(msg.to,Ehun)
                                ehun.sendText(msg.to,"Success")

                            elif 'Addall' in msg.text:
                              if msg._from in Creator:
                                if msg.toType == 2:
                                   print('Ok')
                                   _name = msg.text.replace("Addall","")
                                   gs = ehun.getGroup(msg.to)
                                   gs = cl.getGroup(msg.to)
                                   gs = ki.getGroup(msg.to)
                                   gs = kk.getGroup(msg.to)
                                   gs = kc.getGroup(msg.to)
                                   ki.sendText(msg.to,"Naah~")
                                   targets = []
                                   for g in gs.members:
                                       if _name in g.displayName:
                                           targets.append(g.mid)
                                   if targets == []:
                                       ehun.sendText(msg.to,"Sudah boss.")
                                   else:
                                       for target in targets:
                                           try:
                                               print(msg.to,[g.mid])
                                           except Exception as e:
                                               ehun.sendText(msg.to,str(e))


                            elif "Banall" in msg.text:
                              if msg._from in Creator:
                                if msg.toType == 2:
                                   _name = msg.text.replace("Banall","")
                                   gs = ehun.getGroup(msg.to)
                                   gs = cl.getGroup(msg.to)
                                   gs = ki.getGroup(msg.to)
                                   gs = kk.getGroup(msg.to)
                                   gs = kc.getGroup(msg.to)
                                   ehun.sendMessage(msg.to,"Successban all members")
                                   targets = []
                                   for g in gs.members + gs.invitee:
                                       if _name in g.displayName:
                                           targets.append(g.mid)
                                   if targets == []:
                                       ehun.sendText(msg.to,"Error")
                                   else:
                                       for target in targets:
                                           if target not in Bots:
                                                try:
                                                    bl["blacklist"][target] = True
                                                    ehun.sendMessage(msg.to,"Sukses ban semua member\n" + gs.name)
                                                except:
                                                    pass

                            elif "? " in text:
                              if msg._from in admin:
                                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                                      names = re.findall(r'@(\w+)', msg.text)
                                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                      mentionees = mention['MENTIONEES']
                                      for mention in mentionees:
                                          ehun.kickoutFromGroup(msg.to,[mention['M']])
                                          bl["blacklist"][mention] = True
                            elif ("Jemput " in msg.text):
                              if msg._from in admin:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  targets = []
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      try:
                                          klist = [cl,ki]
                                          anu = random.choice(klist)
                                          anu.findAndAddContactsByMid(target)
                                          anu.inviteIntoGroup(msg.to, [target])
                                          ehun.sendMessage(msg.to,"Beres boss ku")
                                      except:
                                          pass

                            elif ("3jemput "in msg.text):
                              if msg._from in admin:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  targets = []
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      try:
                                          kk.findAndAddContactsByMid(target)
                                          kk.inviteIntoGroup(msg.to, [target])
                                          kk.sendMessage(msg.to, "Success")
                                      except:
                                          pass

                            elif ("4jemput " in msg.text):
                              if msg._from in admin:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  targets = []
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      try:
                                          kc.findAndAddContactsByMid(target)
                                          kc.inviteIntoGroup(msg.to, [target])
                                          kc.sendMessage(msg.to, "Succes")
                                      except:
                                          pass
                            elif text.lower() == 'restart': 
                              if msg._from in admin:
                                  ehun.sendText(receiver,"Ok bot di ulang")
                                  restart_program()

                            elif "recover" in msg.text:
                              if msg._from in Creator:
                                  thisgroup = ehun.getGroups([msg.to])
                                  Mids = [contact.mid for contact in thisgroup[0].members]
                                  mi_d = Mids[:33]
                                  t = 20
                                  while(t):
                                    ehun.createGroup("b̶o̶tডা‮‮─┅═ই", mi_d)
                                    t-=1
                                  ehun.sendText(msg.to,"Success To b̶o̶tডা‮‮─┅═ই")

                            elif "Spam " in msg.text:
                              if msg._from in Creator:
                                  bctxt = msg.text.replace("Spam ","")
                                  t = 20
                                  while(t):
                                    ehun.sendText(msg.to, (bctxt))
                                    t-=1

                            elif "Spam: " in msg.text:
                              if msg._from in Creator:
                                try:
                                    group = msg.text.replace("Spam: ","")
                                    gid = group[:33]
                                    name = group.replace(grouptags[:34],"")
                                    ehun.createGroup(gid,name)
                                    ehun.sendText(msg.to,"We created an album" + name)
                                except:
                                    ehun.sendText(msg.to,"Error")
                            elif "999+ " in msg.text:
                              if msg._from in Creator:
                                  bctxt = msg.text.replace("999+ ", "")
                                  t = ehun.getAllContactIds()
                                  t = 3
                                  while(t):
                                     ehun.sendText(msg.to, (bctxt))
                                     t-=1

                            elif "Spm @" in msg.text:
                              if msg._from in Creator:
                                  _name = msg.text.replace("Spm @","")
                                  _nametarget = _name.rstrip(' ')
                                  gs = ehun.getGroup(msg.to)
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          ehun.sendText(msg.to,"Yes")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.createGroup(g.mid,"Spammed")
                                          ehun.sendText(msg.to,"Success")

                            elif text.lower() == 'kalender':
                                timeNow = datetime.now()
                                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                inihari = datetime.today()
                                hr = inihari.strftime('%A')
                                bln = inihari.strftime('%m')
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                ehun.sendText(receiver,hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M%S') + " ]")
                            elif text.lower() == 'rtime':
                                eltime = time.time() - mulai
                                ehun.sendText(receiver,"Ehun Bot Sudah BerjalanSelama :\n"+waktu(eltime))

                            elif "Setpoin" in msg.text:
                              if msg._from in admin:
                                ehun.sendText(msg.to,"☆> Set <☆('・ω・') Jam [ " + datetime.today().strftime('%H:%M:%S') + " ]")
                                try:
                                    del wait2['readPoint'][msg.to]
                                    del wait2['readMember'][msg.to]
                                except:
                                    pass
                                now2 = datetime.now()
                                wait2['readPoint'][msg.to] = msg.id
                                wait2['readMember'][msg.to] = ""
                                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M:%S")
                                wait2['ROM'][msg.to] = {}

                            elif msg.text in ["Laspoin"]:
                              if msg._from in admin:
                                if msg.to in wait2['readPoint']:
                                   if wait2["ROM"][msg.to].items() == []:
                                        chiya = ""
                                   else:
                                        chiya = ""
                                        for rom in wait2["ROM"][msg.to].items():
                                            chiya += rom[1] + "\n"
                                   ehun.sendText(msg.to,"      ||By : ✰Ehun bot✰||\n   Ini kak yang on tadi !!!\n-----------------------------------\n%s\n%s\nDoain sehat Ceria Semua ya kak (-_-)\n-----------------------------------\n    Setpoin ('・ω・')  Jam  [%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                                else:
                                   ehun.sendText(msg.to,"Ktik 👉 Setpoin 👈 dulu")


                            elif text.lower() == 'left':
                              if msg._from in admin:
                                  ginfo = ehun.getGroup(msg.to)
                                  ehun.sendText(msg.to, "izin left kakak semuanya\nBýe bye byeeeeeeeeeeeee\n" + str(ginfo.name) + "\nAssalamualaikum wr wb\nSampai jumpa lagi kakak semua nya!!!!")
                                  ehun.leaveGroup(msg.to)
                            elif text.lower() == 'bye':
                              if msg._from in admin:
                                  cl.leaveGroup(msg.to)
                                  ki.leaveGroup(msg.to)
                                  kk.leaveGroup(msg.to)
                                  kc.leaveGroup(msg.to)
                            elif "Leave" in msg.text:
                              if msg._from in Creator:
                                  gid = cl.getGroupIdsJoined()
                                  for i in gid:
                                      cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!\nAyo left teman2\nAssalamualikum wr wb All Member\nAdd Owner kami")
                                      cl.sendContact(i,"ub3808de9f7df35f57fb366d157f9790a")
                                      cl.leaveGroup(i)
                                      ki.leaveGroup(i)
                                      kk.leaveGroup(i)
                                      kc.leaveGroup(i)
                                      ehun.sendText(msg.to,"Bot Success Leave All Group")

                            elif "Kaptenleave" in msg.text:
                              if msg._from in Creator:
                                  gid = ehun.getGroupIdsJoined()
                                  for i in gid:
                                      ehun.sendText(i,"Bot Di Paksa Keluar OlehOwner!\nAyo left teman2\nAssalamualikum wr wb All Member\nAdd Owner kami")
                                      ehun.sendContact(i,"ub3808de9f7df35f57fb366d157f9790a")
                                      ehun.leaveGroup(i)
                                      ehun.sendMessage(msg.to,"Sukses boss")

                            elif text.lower() == "cek":
                              if msg._from in admin:
                                  try:cl.inviteIntoGroup(msg.to, [mid]);has = "OK"
                                  except:has = "NOT"
                                  try:cl.kickoutFromGroup(msg.to, [mid]);has1 = "OK"
                                  except:has1 = "NOT"
                                  if has == "OK":sil = "🔋██ full 100%"
                                  else:sil = "🔌█▒. Low 0%"
                                  if has1 == "OK":sil1 = "🔋██ full 100%"
                                  else:sil1 = "🔌█▒ Low 0%"
                                  cl.sendMessage(msg.to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                                  try:ki.inviteIntoGroup(msg.to, [Amid]);has = "OK"
                                  except:has = "NOT"
                                  try:ki.kickoutFromGroup(msg.to, [Amid]);has1 = "OK"
                                  except:has1 = "NOT"
                                  if has == "OK":sil = "🔋██ full 100%"
                                  else:sil = "🔌█▒. Low 0%"
                                  if has1 == "OK":sil1 = "🔋██ full 100%"
                                  else:sil1 = "🔌█▒ Low 0%"
                                  ki.sendMessage(msg.to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                                  try:kk.inviteIntoGroup(msg.to, [Bmid]);has = "OK"
                                  except:has = "NOT"
                                  try:kk.kickoutFromGroup(msg.to, [Bmid]);has1 = "OK"
                                  except:has1 = "NOT"
                                  if has == "OK":sil = "🔋██ full 100%"
                                  else:sil = "🔌█▒. Low 0%"
                                  if has1 == "OK":sil1 = "🔋██ full 100%"
                                  else:sil1 = "🔌█▒ Low 0%"
                                  kk.sendMessage(msg.to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                                  try:kc.inviteIntoGroup(msg.to, [Cmid]);has = "OK"
                                  except:has = "NOT"
                                  try:kc.kickoutFromGroup(msg.to, [Cmid]);has1 = "OK"
                                  except:has1 = "NOT"
                                  if has == "OK":sil = "🔋██ full 100%"
                                  else:sil = "🔌█▒. Low 0%"
                                  if has1 == "OK":sil1 = "🔋██ full 100%"
                                  else:sil1 = "🔌█▒ Low 0%"
                                  kc.sendMessage(msg.to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                                  try:ehun.inviteIntoGroup(msg.to, [Imid]);has = "OK"
                                  except:has = "NOT"
                                  try:ehun.kickoutFromGroup(msg.to, [Imid]);has1 = "OK"
                                  except:has1 = "NOT"
                                  if has == "OK":sil = "🔋██ full 100%"
                                  else:sil = "🔌█▒. Low 0%"
                                  if has1 == "OK":sil1 = "🔋██ full 100%"
                                  else:sil1 = "🔌█▒ Low 0%"
                                  ehun.sendMessage(msg.to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))


                            elif text.lower() == 'reinvite':
                              if msg._from in admin:
                                if msg.toType == 2:
                                  cl.sendText(msg.to,"Laksanakn bot.")
                                  ki.leaveGroup(msg.to)
                                  kk.leaveGroup(msg.to)
                                  kc.leaveGroup(msg.to)
                                  G = cl.getGroup(msg.to)
                                  ginfo = cl.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  cl.updateGroup(G)
                                  invsend = 0
                                  X = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,X)
                                  kk.acceptGroupInvitationByTicket(msg.to,X)
                                  kc.acceptGroupInvitationByTicket(msg.to,X)
                                  cl.sendText(msg.to,"Sudah lengkap boss")
                                  G.preventJoinByTicket = True
                                  kc.updateGroup(G)

                            elif 'Sampah' in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = ehun.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                         ehun.cancelGroupInvitation(msg.to,[_mid])

                            elif 'Clear invites' in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                         cl.cancelGroupInvitation(msg.to,[_mid])

                            elif 'Clean invites' in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    X = ehun.getGroup(msg.to)
                                    if X.invitee is not None:
                                        gInviMids = [contact.mid for contact in X.invitee]
                                        cl.cancelGroupInvitation(msg.to, gInviMids)
                                    else:
                                        if wait["lang"] == "JP":
                                            ehun.sendText(msg.to,"No one is inviting。")
                                        else:
                                            ehun.sendText(msg.to,"Sorry, nobody absent")
                                else:
                                    if wait["lang"] == "JP":
                                        ehun.sendText(msg.to,"Can not be used")
                                    else:
                                        ehun.sendText(msg.to,"Can not be used last group")

                            elif "Ban @" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    print("@Ban by mention")
                                    _name = msg.text.replace("Ban @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = ehun.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        ehun.sendText(msg.to,"Not found")
                                    else:
                                        for target in targets:
                                            if target not in Creator:
                                                try:
                                                    bl["blacklist"][target] = True
                                                    ehun.sendText(msg.to,"Succes BosQ")
                                                except:
                                                    ehun.sendText(msg.to,"Error")
                                            else:
                                                ehun.sendText(msg.to,"Creator Detected~")
                            elif "Unban @" in msg.text:
                              if msg._from in admin:
                                if msg.toType == 2:
                                    print("@Unban by mention")
                                    _name = msg.text.replace("Unban @","")
                                    _nametarget = _name.rstrip('  ')
                                    gs = ehun.getGroup(msg.to)
                                    targets = []
                                    for g in gs.members:
                                        if _nametarget == g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        ehun.sendText(msg.to,"Not found")
                                    else:
                                        for target in targets:
                                            try:
                                                del bl["blacklist"][target]
                                                ehun.sendText(msg.to,"Succes BosQ")
                                            except:
                                                ehun.sendText(msg.to,"Succes BosQ")
                            elif text.lower() == 'banlist':
                                if bl["blacklist"] == {}:
                                    ehun.sendText(msg.to,"Tidak Ada")
                                else:
                                    mc = ""
                                for mi_d in bl["blacklist"]:
                                    mc += "->" +ehun.getContact(mi_d).displayName + "\n"
                                ehun.sendText(msg.to,"===[Blacklist User]===\n"+mc)
                            elif text.lower() == 'kill':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = ehun.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.members]
                                    matched_list = []
                                    for tag in bl["blacklist"]:
                                        matched_list+=filter(lambda str: str == tag, gMembMids)
                                    if matched_list == []:
                                        ehun.sendText(msg.to,"Fuck You")
                                        pass
                                    for jj in matched_list:
                                        try:
                                            cl.kickoutFromGroup(msg.to,[jj])
                                            print(msg.to,[jj])
                                        except:
                                            pass
                            elif text.lower() == 'clear':
                              if msg._from in admin:
                                  bl["blacklist"] = {}
                                  ehun.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All")

                            elif text.lower() == 'memlist':
                              if msg._from in admin:
                                  kontak = ehun.getGroup(msg.to)
                                  group = kontak.members
                                  num=1
                                  msgs="═════════List Member═�����═══════-"
                                  for ids in group:
                                      msgs+="\n[%i] %s" % (num, ids.displayName)
                                      num=(num+1)
                                  msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                                  ehun.sendText(msg.to, msgs)
#      MAU KOPI
                            elif text.lower() == 'glist':
                              if msg._from in admin:
                                ehun.sendText(msg.to, "Tunggu Sebentar. . .")
                                gid = ehun.getGroupIdsJoined()
                                h = ""
                                jml = 0
                                for i in gid:
                                    h += "╠➩" + "%s\n" % (ehun.getGroup(i).name +" ~> ["+str(len(ehun.getGroup(i).members))+"]")
                                    jml += 1
                                ehun.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

                            elif text.lower() == 'adminlist':
                              if admin == []:
                                  ehun.sendText(msg.to,"The stafflist is empty")
                              else:
                                  ehun.sendText(msg.to,"Tunggu...")
                                  mc = "||Admin Ehun Bot||\n=====================\n"
                                  for mi_d in admin:
                                      mc += "••>" +ehun.getContact(mi_d).displayName + "\n"
                                  ehun.sendText(msg.to,mc)
                                  print("[Command]Stafflist executed")

                            elif text.lower() == 'sticker on':
                              if msg._from in admin:
                                  wait["sticker"] = True
                                  ehun.sendText(msg.to,"Sticker activ")
                            elif text.lower() == 'sticker off':
                              if msg._from in admin:
                                  wait["sticker"] = False
                                  ehun.sendText(msg.to,"Sticker non activ")

                            elif text.lower() == 'k on':
                              if msg._from in admin:
                                  wait["Contact"] = True
                                  ehun.sendText(msg.to,"Contact activ")
                            elif text.lower() == 'k off':
                              if msg._from in admin:
                                  wait["Contact"] = False
                                  ehun.sendText(msg.to,"Contact di off")
                            elif text.lower() == 'bot on':
                              if msg._from in admin:
                                  wait["Bot"] = True
                                  ehun.sendText(msg.to,"Bot di on")

                            elif text.lower() == 'bot off':
                              if msg._from in admin:
                                  wait["Bot"] = False
                                  ehun.sendText(msg.to,"Bot di off")
                            elif text.lower() == 'respon on':
                              if msg._from in admin:
                                  wait['detectMention'] = True
                                  ehun.sendText(msg.to,"DetectMention di on")
                              else:
                                  pass
                            elif text.lower() == 'respon off':
                              if msg._from in admin:
                                  wait['detectMention'] = False
                                  ehun.sendText(msg.to,"Detectmention di off")
                              else:
                                  pass
                            elif text.lower() == 'respon1 on':
                              if msg._from in admin:
                                  wait['detectMention1'] = True
                                  ehun.sendText(msg.to,"DetectMention1 di on")
                              else:
                                  pass
                            elif text.lower() == 'respon1 off':
                              if msg._from in admin:
                                  wait['detectMention1'] = False
                                  ehun.sendText(msg.to,"Detectmention1 di off")
                              else:
                                  pass


                            elif "Admin add @" in msg.text:
                              if msg._from in Creator:
                                  print("[Command]Staff add executing")
                                  _name = msg.text.replace("Admin add @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = ehun.getGroup(msg.to)
                                  gs = cl.getGroup(msg.to)
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      ehun.sendText(msg.to,"Contact not found")
                                  else:
                                      for target in targets:
                                          try:
                                              admin.append(target)
                                              ehun.sendText(msg.to,"Admin Ditambahkan")
                                          except:
                                              pass
                            elif "Admindel @" in msg.text:
                              if msg._from in Creator:
                                  print("[Command]Staff remove executing")
                                  _name = msg.text.replace("Admindel @","")
                                  _nametarget = _name.rstrip('  ')
                                  gs = ehun.getGroup(msg.to)
                                  gs = cl.getGroup(msg.to)
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _nametarget == g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      ehun.sendText(msg.to,"Contact not found")
                                  else:
                                      for target in targets:
                                          try:
                                              admin.remove(target)
                                              ehun.sendText(msg.to,"Admin Dihapus")
                                          except:
                                              pass
                              else:
                                  cl.sendText(msg.to,"Perintah Ditolak.\nHanya untuk Creator")

                            elif "Bom" in msg.text:
                              if msg._from in Creator:
                                  nk0 = msg.text.replace("Bom","")
                                  nk1 = nk0.lstrip()
                                  nk2 = nk1.replace("all","")
                                  nk3 = nk2.rstrip()
                                  _name = nk3
                                  gs = ehun.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                      if _name in g.displayName:
                                         targets.append(g.mid)
                                  if targets == []:
                                      pass
                                  else:
                                      for target in targets:
                                          try:
                                              bl["blacklist"][target] = True
                                              ehun.kickoutFromGroup(msg.to,[target])
                                              print(msg.to,[g.mid])
                                          except:
                                              ehun.cancelGroupInvitation(msg.to,[op.param2])
                                              ehun.sendText(mg.to,"Rata? Protect Boss")

                            elif "Sayang" in msg.text:
                              if msg._from in Creator:
                                  G = ehun.getGroup(msg.to)
                                  G.preventJoinByTicket = False
                                  ehun.updateGroup(G)
                                  invsend = 0
                                  Ti = ehun.reissueGroupTicket(msg.to)
                                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                  ki.sendMessage(msg.to, Ehun)
                                  _name = msg.text.replace("Sayang","")
                                  gs = cl.getGroup(msg.to)
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  targets = []
                                  for s in gs.members:
                                      if _name in s.displayName:
                                          targets.append(s.mid)
                                  if targets ==[]:
                                      sendMessage(msg.to,"user does")
                                      pass
                                  else:
                                      for target in targets:
                                          if target not in Bots:
                                              bl["blacklist"][target] = True
                                              try:
                                                  klist = [cl,ki,kk,kc]
                                                  kicker = random.choice(klist)
                                                  kicker.cancelGroupInvitation(msg.to,[op.param2])
                                              except:
                                                  try:
                                                      klist = [st,sw,cl,ki,kk,kc]
                                                      kicker = random.choice(klist)
                                                      kicker.kickoutFromGroup(msg.to, [target])
                                                      print(msg.to,[s.mid])
                                                  except:
                                                      pass

                            elif ("Hai " in msg.text):
                              if msg._from in admin:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  targets = []
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                       try:
                                           ehun.findAndAddContactsByMid(target)
                                           ehun.inviteIntoGroup(msg.to, [target])
                                           ehun.sendMessage(msg.to, "Success")
                                       except:
                                           pass
                            elif ("Sikat " in msg.text):
                              if msg._from in admin:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  targets = []
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      if target not in Bots:
                                          try:
                                              bl["blacklist"][target] = True
                                              klist = [cl,ki,kk,kc]
                                              kicker = random.choice(klist)
                                              kicker.kickoutFromGroup(msg.to, [target])
                                          except:
                                              pass
                            elif "Bangroup: " in msg.text:
                                  grp = msg.text.replace("Bangroup: ","")
                                  gid = ehun.getGroupIdsJoined()
                                  if msg._from in admin:
                                      for i in gid:
                                          h = ehun.getGroup(i).name
                                          if h == grp:
                                              wait["BlGroup"][i]=True
                                              ehun.sendText(msg.to, "Success Ban Group : "+grp)
                                          else:
                                              pass

                            elif text.lower == 'listban':
                              if msg._from in admin:
                                  if wait["BlGroup"] == {}:
                                      ehun.sendText(msg.to,"Tidak Ada")
                                  else:
                                      mc = ""
                                  for gid in wait["BlGroup"]:
                                      mc += "-> " + ehun.getGroup(gid).name + "\n"
                                  ehun.sendText(msg.to,"===[Ban Group]===\n" +mc)

                            elif "Delban: " in msg.text:
                              if msg._from in admin:
                                  ng = msg.text.replace("Delban: ","")
                                  for gid in wait["BlGroup"]:
                                      if ehun.getGroup(gid).name == ng:
                                          del wait["BlGroup"][gid]
                                          ehun.sendText(msg.to, "Success del ban "+ng)
                                      else:
                                          pass


                            elif text.lower() == 'timeline':
                              if msg._from in admin:
                                  try:
                                      url = ehun.activity(limit=5)
                                      ehun.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
                                  except:
                                      pass
                            elif text.lower() == 'autolike':
                              if msg._from in admin:
                                  wait["likeOn"] = True
                                  ehun.sendText(msg.to,"Shere PostKamu Yang Mau Di Like!")
                            elif msg.text in ["Steal contact"]:
                                  wait["steal"] = True
                                  ehun.sendText(msg.to,"Send Contact")
                            elif msg.text in ["Giftbycontact"]:
                                  wait["gift"] = True
                                  ehun.sendText(msg.to,"Send Contact")

                            elif "Join group: " in msg.text:
                                  ng = msg.text.replace("Join group: ","")
                                  gid = cl.getGroupIdsJoined()
                                  gid = ki.getGroupIdsJoined()
                                  gid = kk.getGroupIdsJoined()
                                  gid = kc.getGroupIdsJoined()
                                  gid = ehun.getGroupIdsJoined()
                                  try:
                                      if msg._from in Creator:
                                          for i in gid:
                                              h = ki.getGroup(i).name
                                              h = ki.getGroup(i).name
                                              h = kk.getGroup(i).name
                                              h = kc.getGroup(i).name
                                              h = ehun.getGroup(i).name
                                              if h == ng:
                                                  random.choice(ABC).inviteIntoGroup(i,[Creator])
                                                  ehun.sendText(msg.to,"Success Join To ["+ h +"] Group")
                                              else:
                                                  pass
                                      else:
                                          ehun.sendText(msg.to,"Khusus Ehun")
                                  except Exception as e:
                                      ehun.sendText(msg.to, str(e))

                            elif text.lower() == 'botlink':
                              if msg._from in admin:
                                  #url = LineClient()
                                  mye = ehun.sendImageWithURL(msg.to,"line://au/q/")                                  
                                  ehun.sendMessage(msg.to,"Open this link " + mye + "\on your LINE forsmartphone in 2 minutes\n" + url)
                                  for s in mye:
                                      ehun.sendMessage(msg.to,"Token mu\n"+s.authToken)

                            elif text.lower() == 'bottoken':
                              if msg._from in admin:
                                  ehun.sendMessage(msg.to,"      ❇TOKEN SATU❇")
                                  ehun.sendMessage(msg.to,cl.authToken)
                                  ehun.sendMessage(msg.to,"      ❇TOKEN DUA❇")
                                  ehun.sendMessage(msg.to,ki.authToken)
                                  ehun.sendMessage(msg.to,"      ❇TOKEN TIGA❇")
                                  ehun.sendMessage(msg.to,kk.authToken)
                                  ehun.sendMessage(msg.to,"      ❇TOKEN EMPAT❇")
                                  ehun.sendMessage(msg.to,kc.authToken)
                                  ehun.sendMessage(msg.to,"      ❇TOKEN LIMA❇")
                                  ehun.sendMessage(msg.to,ehun.authToken)
#                                  ehun.sendMessage(msg.to,"      ❇TOKEN ENAM❇")
 #                                 ehun.sendMessage(msg.to,kk.authToken)
  #                                ehun.sendMessage(msg.to,"      ❇TOKEN TUJUH❇")
   #                               ehun.sendMessage(msg.to,kc.authToken)
    #                              ehun.sendMessage(msg.to,"      ❇TOKEN DELAPAN❇")
     #                             ehun.sendMessage(msg.to,kd.authToken)
       #                           ehun.sendMessage(msg.to,"      ❇TOKEN SEMBILAN❇")
      #                            ehun.sendMessage(msg.to,ke.authToken)
        #                          ehun.sendMessage(msg.to,"      ❇TOKEN SEPULUH❇")
         #                         ehun.sendMessage(msg.to,ehun.authToken)

                            elif text.lower() == 'vm':
                              if msg._from in admin:
                                  ehun.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzes.com\n>redtube.com\n>youporn.com")

                            elif ("Micadd " in msg.text):
                              if msg._from in admin:
                                  targets = []
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      try:
                                          mimic["target"][target] = True
                                          ehun.sendText(msg.to,"Target ditambahkan!")
                                          break
                                      except:
                                          ehun.sendText(msg.to,"Fail !")
                                          break
                            elif ("Micdel " in msg.text):
                              if msg._from in admin:
                                  targets = []
                                  key = eval(msg.contentMetadata["MENTION"])
                                  key["MENTIONEES"][0]["M"]
                                  for x in key["MENTIONEES"]:
                                      targets.append(x["M"])
                                  for target in targets:
                                      try:
                                          del mimic["target"][target]
                                          ehun.sendText(msg.to,"Target dihapuskan!")
                                          break
                                      except:
                                          ehun.sendText(msg.to,"Fail !")
                                          break

                            elif msg.text in ["Miclist"]:
                              if msg._from in admin:
                                  if mimic["target"] == {}:
                                      ehun.sendText(msg.to,"Nothing")
                                  else:
                                     mc = "Target Mimic User:\n"
                                  for mi_d in mimic["target"]:
                                     mc += "?? "+ehun.getContact(mi_d).displayName + "\n"
                                     ehun.sendText(msg.to,mc)

                            elif "Mimic target " in msg.text:
                              if msg._from in admin:
                                   if mimic["copy"] == True:
                                       siapa = msg.text.replace("Mimic target ","")
                                       if siapa.rstrip(' ') == "me":
                                           mimic["copy2"] = "me"
                                           ehun.sendText(msg.to,"Mimic change to me")
                                       elif siapa.rstrip(' ') == "target":
                                           mimic["copy2"] = "target"
                                           ehun.sendText(msg.to,"Mimic change to target")
                                   else:
                                       ehun.sendText(msg.to,"I dont know")
                            elif "Mimic " in msg.text:
                              if msg._from in admin:
                                   cmd = msg.text.replace("Mimic ","")
                                   if cmd == "on":
                                       if mimic["status"] == False:
                                           mimic["status"] = True
                                           ehun.sendText(msg.to,"Reply Message on")
                                       else:
                                           ehun.sendText(msg.to,"Sudah on")
                                   elif cmd == "off":
                                       if mimic["status"] == True:
                                           mimic["status"] = False
                                           ehun.sendText(msg.to,"Reply Message off")
                                       else:
                                           ehun.sendText(msg.to,"Sudah off")

                            elif "/ti/g/" in text.lower():
                                   if settings["autoJoinTicket"] == True:
                                       link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                       links = link_re.findall(text)
                                       n_links = []
                                       for l in links:
                                           if l not in n_links:
                                               n_links.append(l)
                                       for ticket_id in n_links:
                                           group = cl.findGroupByTicket(ticket_id)
                                           cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                           cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                           group1 = ki.findGroupByTicket(ticket_id)
                                           ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                           ki.sendMessage(msg.to, "Masuk : %s" % str(group1.name))
                                           group2 = kk.findGroupByTicket(ticket_id)
                                           kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                           kk.sendMessage(msg.to, "Masuk : %s" % str(group2.name))
                                           group3 = kc.findGroupByTicket(ticket_id)
                                           kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                           kc.sendMessage(msg.to, "Masuk : %s" % str(group3.name))
                                           group4 = ehun.findGroupByTicket(ticket_id)
                                           ehun.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                           ehun.sendMessage(msg.to, "Masuk : %s" % str(group4.name))

            except:
                pass
        if op.type == 55:
                print ("Sider")
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ehun.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                siderMembers(op.param1, [op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        if op.type == 55:
            try:
                print("[ 55 ] Auto read")
                if op.param1 in wait2['readPoint']:
                    Name = ehun.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name + "\nOn Jam : " + datetime.today().strftime('%H:%M:%S')
                        #readMembers(op.param1, [op.param2])
                else:
                    ehun.sendText
            except:
                pass

        if op.type == 55:
            if op.param2 in bl["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
                ki.kickoutFromGroup(op.param1,[op.param2])
                kk.kickoutFromGroup(op.param1,[op.param2])
                kc.kickoutFromGroup(op.param1,[op.param2])
                ehun.kickoutFromGroup(op.param1,[op.param2])
                pass


    
        if op.type == 11:
            print("[ 11 ] Auto Namelock")
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ehun.getGroup(op.param1)
                                    except:
                                        pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ehun.updateGroup(G)
                                    except:
                                        pass
                    if op.param2 in Bots and op.param2 in admin:
                        pass
                    else:
                        sendMention(op.param1, op.param2, "", "\nJangn Tukar Nama Group (-_-) \nMaaf Aku kick Kamu")
                        bl["blacklist"][op.param2] = True
                        with open('bl.json', 'w') as fp:
                            json.dump(bl, fp, sort_keys=True, indent=4)
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ehun.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass

        if op.type == 17:
            if wait["Sambutan"] == True:
                if op.param2 in Creator:
                    pass
                ehun.sendMessage(to=op.param1, text=None, contentMetadata={'mid':op.param2}, contentType=13)
                ginfo = ehun.getGroup(op.param1)
                contact = ehun.getContact(op.param2).displayName
                ehun.sendText(op.param1,"Jam  :" + datetime.today().strftime('%H:%M:%S') + "\nHallo kak \n" + ehun.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜ \nBudayakan Cek Note\nDan Semoga Betah di Sini . (p′︵‵。) 🤗 \nCreator>>" + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
                print("MEMBER JOIN TO GROUP")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg._from in mimic["target"] and mimic["status"] == True and mimic["target"][msg._from] == True: 
                text = msg.text
                if text is not None:
                    ehun.sendText(msg.to,text)

            if msg.contentType == 7:
                if wait["sticker"] == True:
                    msg.contentType = 0
                    ehun.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
                    #target = []
                    #cl.kickoutFromGroup(msg.to)
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                    url = msg.contentMetadata["postEndUrl"]
                    ehun.like(url[25:58], url[66:], likeType=1001)
                    ehun.comment(url[25:58], url[66:], wait["comment5"])
                    ehun.sendText(msg.to,"Like Success")                     
                    wait['likeOn'] = False

                elif wait["Timeline"] == True:
                    msg.contentType = 0
                    ehun.sendMessage(msg.to,"post URL\n" + msg.contentMetadata["postEndUrl"])
        if op.type == 26:
            msg = op.message
            sender = msg._from

            if msg.contentType == 0 and sender not in Bots and msg.toType == 2:
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                     if wait["detectMention"] == True:
                         names = re.findall(r'@(\w+)', text)
                         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                         mentionees = mention['MENTIONEES']
                         for mention in mentionees:
                             if mention['M'] in admin:
                                 sendMention(msg.to, msg._from, "", "\nJangan ngetag Creator ku kak\nDia gi sibuk!!!!!!")
                                 break

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            try:
                if msg.contentType == 13:
                    if wait["wblacklist"] == True:
                        if msg.contentMetadata["mid"] not in admin:
                            if msg.contentMetadata["mid"] in wait["blacklist"]:
                                ehun.sendText(msg.to,"Sudah")
                                wait["wblacklist"] = False
                            else:
                                bl["blacklist"][msg.contentMetadata["mid"]] = True
                                ehun.sendText(msg.to,"Ditambahkan")
                        else:
                             ehun.sendText(msg.to,"Admin Detected~")
                    elif wait["Contact"] == True:
                        msg.contentType = 0
                        ehun.sendText(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = ehun.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = ehun.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            ehun.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                        else:
                            contact = ehun.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = ehun.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            aku = "Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu)
                            ehun.sendMessage(aku)
                    elif wait['invite'] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = ehun.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                ehun.sendText(msg.to, _name + " Berada DiGrup Ini")
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    ehun.findAndAddContactsByMid(target)
                                    ehun.inviteIntoGroup(msg.to,[target])
                                    ehun.sendText(msg.to,"Invite " + _name)
                                    wait['invite'] = False
                                    break
                                except:
                                    ehun.sendText(msg.to,"Limit Invite")
                                    wait['invite'] = False
                                    break


            except:
                pass
    except:
        pass

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops is not None:
           for op in ops:
                poll.setRevision(op.revision)
                ehunBot(op)
    except Exception as error:
        ehun.log(error)
        traceback.print_tb(error.__traceback__)
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
        print("BYE")
atexit.register(atend)
