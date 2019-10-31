#Boa:Frame:Client

import wx
import wx.lib.buttons
import socket
import time
import des
import rsa

def create(parent):
    return Client(parent)

[wxID_CLIENT, wxID_CLIENTBUTTONLOGIN, wxID_CLIENTGENTOGGLEBUTTONC, 
 wxID_CLIENTPRINTFTEXT, wxID_CLIENTSTATICTEXTPASSWORD, 
 wxID_CLIENTSTATICTEXTREV, wxID_CLIENTSTATICTEXTUSER, 
 wxID_CLIENTTEXTCTRLPASSWORD, wxID_CLIENTTEXTCTRLUSER, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Client(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_CLIENT, name=u'Client', parent=prnt,
              pos=wx.Point(187, 268), size=wx.Size(400, 400),
              style=wx.DEFAULT_FRAME_STYLE, title=u'-Client-')
        self.SetClientSize(wx.Size(400, 372))

        self.textCtrluser = wx.TextCtrl(id=wxID_CLIENTTEXTCTRLUSER,
              name=u'textCtrluser', parent=self, pos=wx.Point(160, 130),
              size=wx.Size(140, 32), style=0, value=u'')

        self.textCtrlpassword = wx.TextCtrl(id=wxID_CLIENTTEXTCTRLPASSWORD,
              name=u'textCtrlpassword', parent=self, pos=wx.Point(160, 190),
              size=wx.Size(140, 32), style=wx.TE_PASSWORD, value=u'')
        self.textCtrlpassword.SetToolTipString(u'textCtrlpassword')

        self.staticTextuser = wx.StaticText(id=wxID_CLIENTSTATICTEXTUSER,
              label=u'User:', name=u'staticTextuser', parent=self,
              pos=wx.Point(112, 136), size=wx.Size(36, 17), style=0)

        self.staticTextpassword = wx.StaticText(id=wxID_CLIENTSTATICTEXTPASSWORD,
              label=u'Password:', name=u'staticTextpassword', parent=self,
              pos=wx.Point(80, 196), size=wx.Size(71, 17), style=0)

        self.buttonlogin = wx.Button(id=wxID_CLIENTBUTTONLOGIN, label=u'Login',
              name=u'buttonlogin', parent=self, pos=wx.Point(290, 260),
              size=wx.Size(85, 32), style=0)
        self.buttonlogin.Bind(wx.EVT_BUTTON, self.OnButtonloginButton,
              id=wxID_CLIENTBUTTONLOGIN)

        self.genToggleButtonc = wx.lib.buttons.GenToggleButton(id=wxID_CLIENTGENTOGGLEBUTTONC,
              label=u'DES', name=u'genToggleButtonc', parent=self,
              pos=wx.Point(290, 30), size=wx.Size(85, 32), style=0)
        self.genToggleButtonc.SetToggle(True)
        self.genToggleButtonc.Bind(wx.EVT_BUTTON, self.OnGenToggleButtoncButton,
              id=wxID_CLIENTGENTOGGLEBUTTONC)

        self.printftext = wx.StaticText(id=wxID_CLIENTPRINTFTEXT,
              label=u'Client', name=u'printftext', parent=self, pos=wx.Point(30,
              36), size=wx.Size(40, 17), style=0)

        self.staticTextrev = wx.StaticText(id=wxID_CLIENTSTATICTEXTREV,
              label=u'', name=u'staticTextrev', parent=self, pos=wx.Point(30,
              64), size=wx.Size(1, 17), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButtonloginButton(self, event):
        times=time.strftime("%H:%M:%S", time.localtime())
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 8001))
            self.printftext.SetLabel('Client to Server:Connecting!'+times)
            
            #send
            if(self.genToggleButtonc.GetLabel()=='DES'):
                paw=self.textCtrlpassword.GetValue()
                #DES
                d=des.DES()
                d.input_key(des.key)#8
                paw=d.encode(paw) 
                #DES
                sock.send('DES:'+self.textCtrluser.GetValue()+':'+paw)
            
            elif(self.genToggleButtonc.GetLabel()=='RSA'):
                paw=self.textCtrlpassword.GetValue()
                #paws=str(rsa.n+rsa.e)
                #paws=rsa.a()
                pawing=str(paw)
                paws=rsa.encrypt(pawing,rsa.n,rsa.e)
                sock.send('RSA:'+self.textCtrluser.GetValue()+':'+paws)
            
            #recv
            self.staticTextrev.SetLabel(sock.recv(1024))
            #print sock.recv(1024)
            sock.close()
        except:
            self.printftext.SetLabel('Client to Server:Disconnected!')
            #print 'Error'
        #error input
        event.Skip()

    def OnGenToggleButtoncButton(self, event):
        if(1):
            if(self.genToggleButtonc.GetLabel()=='DES'):
                self.genToggleButtonc.SetLabel('RSA')
                self.genToggleButtonc.SetValue(0)
            elif(self.genToggleButtonc.GetLabel()=='RSA'):
                self.genToggleButtonc.SetLabel('DES')
                self.genToggleButtonc.SetValue(0)
        #turn change
        event.Skip()
