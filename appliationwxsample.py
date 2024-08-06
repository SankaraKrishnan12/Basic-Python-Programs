import wx


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="Enhanced wxPython Application")
        frame.Show()
        return True


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))
        panel = wx.Panel(self)
        self.CreateStatusBar()

        # Add a menu
        fileMenu = wx.Menu()
        menuAbout = fileMenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        menuExit = fileMenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)

        # Widgets
        wx.StaticText(panel, label="Enter your name:", pos=(20, 20))
        self.text_ctrl = wx.TextCtrl(panel, value="", pos=(150, 20), size=(200, -1))
        self.btn = wx.Button(panel, label="Submit", pos=(150, 60))

        # Event bindings
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_BUTTON, self.OnSubmit, self.btn)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A small wxPython application", "About Hello wxPython", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)

    def OnSubmit(self, event):
        name = self.text_ctrl.GetValue()
        wx.MessageBox(f"Hello, {name}!", "Info", wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
