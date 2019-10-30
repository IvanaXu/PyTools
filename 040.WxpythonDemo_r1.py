# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()