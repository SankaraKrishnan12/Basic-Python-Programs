
import wx

def onButtonClick(event):
    wx.MessageBox("Message is displayed!","info",wx.OK|wx.ICON_INFORMATION)

app1 = wx.App()
frame = wx.Frame(None, title ="wxpython app")
pa = wx.Panel(frame)
e = wx.Button(pa,-1, "Button1", pos = (120, 100))
e.Bind(wx.EVT_BUTTON,onButtonClick)
frame.Show()
app1.MainLoop()
