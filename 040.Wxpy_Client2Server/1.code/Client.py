#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Frame2

modules ={'Frame2': [1, 'Main frame of Application', u'Frame2.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame2.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
