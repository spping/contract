import requests
import wx
import wx.html2

from un1 import DBSession
from FutureContract import FutureContract

class MyBrowser(wx.Frame):
  def __init__(self, *args, **kwds):
    wx.Frame.__init__(self, None, -1, 'Button Example', 
                size=(300, 100))
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.browser = wx.html2.WebView.New(self)
    sizer.Add(self.browser, 1, wx.EXPAND, 10)
    self.SetSizer(sizer)
    self.SetSize((700, 700))

class ButtonFrame(wx.Frame):
    def __init__(self):
        self.frame = wx.Frame.__init__(self, None, -1, 'Button Example', 
                size=(800, 800))
        self.panel = wx.Panel(self, -1)

        self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyDown)
        
        self.button = wx.Button(self.panel, -1, "F10资料", pos=(680, 20))
        sampleList = [item[0] for item in  DBSession().query(FutureContract.交易品种).all()]
        print(sampleList)
        self.radio = wx.RadioBox(self.panel, -1, "A Radio Box", (10, 10), wx.DefaultSize,
                        sampleList, 2, wx.RA_SPECIFY_COLS)
        self.button.Bind(wx.EVT_BUTTON, self.OnClick)
        # self.button.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        
        self.Centre()
  
    def OnClick(self, event):
        print('click:', event)
        frame = MyBrowser()
        print(self.radio.GetStringSelection())
        r = requests.post('http://127.0.0.1:5000', data = {'variety': self.radio.GetStringSelection()})
        frame.browser.SetPage(r.text, "")
        frame.Show()
    
    
    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print('key:', event, keycode)
        if keycode == wx.WXK_F10:
            self.OnClick(event)
        else:
            print('skip')
            event.Skip()
          
if __name__ == '__main__':
    app = wx.App()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()