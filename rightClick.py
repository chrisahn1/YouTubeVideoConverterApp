# import tkinter
#
# class Test(tkinter.Text):
#     def __init__(self, master, **kw):
#         tkinter.Text.__init__(self, master, **kw)
#         self.bind('<Control-c>', self.copy)
#         self.bind('<Control-x>', self.cut)
#         self.bind('<Control-v>', self.paste)
#
#     def copy(self, event=None):
#         self.clipboard_clear()
#         text = self.get("sel.first", "sel.last")
#         self.clipboard_append(text)
#
#     def cut(self, event):
#         self.copy()
#         self.delete("sel.first", "sel.last")
#
#     def paste(self, event):
#         text = self.selection_get(selection='CLIPBOARD')
#         self.insert('insert', text)
#
#
# def test():
#     r = tkinter.Tk()
#     t = Test(r)
#     t.pack(fill='both', expand=1)
#     r.mainloop()
#
#
# if __name__ == '__main__':
#     test()



import tkinter
# from Tkinter import *
from tkinter import TclError

def rClicker(e):
    ''' right click context menu for all Tk Entry and Text widgets
    '''

    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()

        nclst=[
               (' Cut', lambda e=e: rClick_Cut(e)),
               (' Copy', lambda e=e: rClick_Copy(e)),
               (' Paste', lambda e=e: rClick_Paste(e)),
               ]

        rmenu = tkinter.Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print(' - rClick menu, something wrong')
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print(' - rClickbinder, something wrong')
        pass


if __name__ == '__main__':
    master = tkinter.Tk()
    ent = tkinter.Entry(master, width=50)
    ent.pack(anchor="w")

    #bind context menu to a specific element
    ent.bind('<Button-3>',rClicker, add='')
    #or bind it to any Text/Entry/Listbox/Label element
    #rClickbinder(master)

    master.mainloop()