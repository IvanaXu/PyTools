#Boa:Frame:Server

import wx
import wx.lib.buttons
import wx.richtext
import time
import MySQLdb
import socket
import infomsg
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
import threading
from time import ctime,sleep
import des
import rsa

def create(parent):
    return Server(parent)

[wxID_SERVER, wxID_SERVERBUTTON1, wxID_SERVERBUTTON2, wxID_SERVERBUTTONMATCH, 
 wxID_SERVERBUTTONSELECT, wxID_SERVERRICHTEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

threads = []
[wxID_SERVERTIMER1] = [wx.NewId() for _init_utils in range(1)]

class Server(wx.Frame):
    def _init_utils(self):
        # generated method, don't edit
        self.timer1 = wx.Timer(id=wxID_SERVERTIMER1, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimer1Timer, id=wxID_SERVERTIMER1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SERVER, name=u'Server', parent=prnt,
              pos=wx.Point(852, 210), size=wx.Size(410, 533),
              style=wx.DEFAULT_FRAME_STYLE, title=u'-Server-')
        self._init_utils()
        self.SetClientSize(wx.Size(410, 505))

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_SERVERRICHTEXTCTRL1,
              parent=self, pos=wx.Point(5, 100), size=wx.Size(400, 400),
              style=wx.richtext.RE_MULTILINE, value=u'Input:')
        self.richTextCtrl1.SetLabel(u'')

        self.button1 = wx.Button(id=wxID_SERVERBUTTON1, label=u'Start',
              name='button1', parent=self, pos=wx.Point(10, 10),
              size=wx.Size(85, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_SERVERBUTTON1)

        self.buttonselect = wx.Button(id=wxID_SERVERBUTTONSELECT,
              label=u'Select', name=u'buttonselect', parent=self,
              pos=wx.Point(330, 10), size=wx.Size(64, 32), style=0)
        self.buttonselect.Bind(wx.EVT_BUTTON, self.OnButtonselectButton,
              id=wxID_SERVERBUTTONSELECT)

        self.buttonmatch = wx.Button(id=wxID_SERVERBUTTONMATCH, label=u'Exit',
              name=u'buttonmatch', parent=self, pos=wx.Point(330, 50),
              size=wx.Size(64, 32), style=0)
        self.buttonmatch.Bind(wx.EVT_BUTTON, self.OnButtonmatchButton,
              id=wxID_SERVERBUTTONMATCH)

        self.button2 = wx.Button(id=wxID_SERVERBUTTON2, label=u'Over',
              name='button2', parent=self, pos=wx.Point(10, 50),
              size=wx.Size(85, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_SERVERBUTTON2)

    def Inputs(self, string):
        times=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        self.richTextCtrl1.SetValue(self.richTextCtrl1.GetValue()+'\n'+times+' : '+string)

    #thread t1
    def serverf():
        factory = Factory()
        #socketT = IphoneChat()
        #socketT.sbutton(self.richTextCtrl1)
        #factory.protocol = module1.SocketT
        factory.protocol = With
        factory.clients = []
        reactor.listenTCP(8001, factory)
        reactor.run()
    
    t1 = threading.Thread(target=serverf,args=())
    threads.append(t1)
    
    #main
    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Inputs('Welcome')
        #running
        
        for t in threads:
            t.setDaemon(True)
            t.start()
            self.Inputs('Server started')

    def OnButtonselectButton(self, event):
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='xuyifan',db='infologin',port=3306)
            cur=conn.cursor()
            strout=cur.execute('select * from LoginTable')
            #print strout
            self.Inputs('There are '+str(strout)+' Users')
            
            #one to one
            info=cur.fetchmany(strout)
            for i in info:
                #print i
                self.Inputs(str(i))
            cur.close()
            conn.close()
        except Exception as e:
            self.Inputs('Mysql Error ')
        #___Sql_________
        event.Skip()

    def OnButtonmatchButton(self, event):
        wx.Exit()
        event.Skip()
    
    def OnButton1Button(self, event):
        self.timer1.Start(10)
        self.Inputs('Listening')
        event.Skip()
    
    def OnButton2Button(self, event):
        self.timer1.Stop()
        self.Inputs('UnListen')
        event.Skip()

    def OnTimer1Timer(self, event):
        if(infomsg.state):
            self.Inputs(infomsg.ing)
        infomsg.state=0
        event.Skip()

class With(Protocol):
    def connectionMade(self):
        self.factory.clients.append(self)
        print 'Clients are',self.factory.clients
    
    def connectionLost(self, reason):
        self.factory.clients.remove(self)
    
    def dataReceived(self, data):
        a = data.split(':')
        if len(a) > 1:
            count=a[0]
            command = a[1]
            content = a[2]
            
            #count
            #'change content to paw'
            if(count=='DES'):
                d=des.DES()
                d.input_key(des.key)#8
                paw=d.decode(content)
            elif(count=='RSA'):
                #paw=str(rsa.n+rsa.e+rsa.d)
                #paw=rsa.a()
                paw=rsa.decrypt(content,rsa.n,rsa.e,rsa.d)
            
            #str
            sqlkey=infomsg.sqlmatch(command,paw)
            if(sqlkey=='Y'):
                msg=command+' has joined!'
                pri=count+' "Usr:'+command+' Port:('+content+') Paw:'+paw+'" Logined'
            else:
                msg=sqlkey
                pri=count+' "Usr:'+command+' Port:('+content+') Paw:'+paw+'" Error!!'
            
            #printf
            infomsg.ing=pri
            infomsg.state=1
            #printf
            
            #message
            for c in self.factory.clients:
                c.message(msg)
            #message
            
    def message(self, message):
        self.transport.write(message + '\n')

        
