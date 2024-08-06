import wx
app = wx.App()
frm = wx.Frame(None,title="Hello World")
panel = wx.Panel(frm)
text = wx.StaticText(panel, label="Hello World", pos=(10,10))
frm.Show()
app.MainLoop()
