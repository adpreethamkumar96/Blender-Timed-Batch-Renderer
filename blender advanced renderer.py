import subprocess
import os
import sys
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from pathlib import Path
import time

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

#import batchrendererNEWLAYOU_support

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Blender_Advanced_renderer_by_ranga (root)
    #batchrendererNEWLAYOU_support.init(root, top)
    init(root, top)
    root.mainloop()

w = None
def create_Blender_Advanced_renderer_by_ranga(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Blender_Advanced_renderer_by_ranga (w)
    batchrendererNEWLAYOU_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Blender_Advanced_renderer_by_ranga():
    global w
    w.destroy()
    w = None


class Blender_Advanced_renderer_by_ranga:
    fname=None
    dotblend=None
    newdotblend=None
    numberframe=None
    startframe=None
    endframe=None
    timeint=None


    def startrender(self):
           print(0, self.startframe, self.endframe, self.timeint)
    #       print("the type of start frame is ",type(self.startframe))
           os.chdir(self.fname)
           check = self.endframe
           start1 = self.startframe
           end1 = 0
           for i in range(self.startframe,check,self.numbframe):
               a = str(start1)
               b = str(end1)
               c=self.newdotblend
               om = ("blender -b " + c + " -E CYCLES -s " + a + " -e " + b + " -a")
               print(om)
               end1 = start1 + self.numbframe - 1
               if end1 < check:
                   if a == b and self.startframe == 0:
                       print("Program renders from 1")


                   else:
                       a = str(start1)
                       b = str(end1)
                       om = ("blender -b " + c + " -E CYCLES -s " + a + " -e " + b + " -a")
                       print(i)
                       os.system(om)
                       print(" main else blender rendering with %s start, %s end" % (start1, end1))
                       time.sleep(self.timeint)
                       start1 = end1 + 1
               else:
                   end1 = check
                   a = str(start1)
                   b = str(end1)
                   om = ("blender -b " + c + " -E CYCLES -s " + a + " -e " + b + " -a")
                   print(i)
                   print(om)
                   os.system(om)
                   print("second elese blender rendering with %s start, %s end" % (start1, end1))
                   time.sleep(self.timeint)
                   break

           print("completed successfully")
    #       #print(self.newdotblend)
    #       text_file = open("note.txt", "w")
    #       text_file.write('"'+self.fname+'"')
    #       text_file.write("\n")
    #       text_file.write('"'+self.dotblend+'"')
    #       text_file.write("\n")
    #       text_file.write(self.numbframe)
    #       text_file.write("\n")
    #       text_file.write(self.startframe)
    #       text_file.write("\n")
    #       text_file.write(self.endframe)
    #       text_file.write("\n")
    #       text_file.write(self.timeint)
    #       text_file.write("\n")
    #       subprocess.Popen([r"blendercmd.exe"])

#these are the try to run in the subprocess
          # c= " "+self.newdotblend
          # print("c value is "+c)
          # print(type(c))
          # om = "blender -b" + c + " -E CYCLES -s %d -e %d -a"
          # print("om is "+om)
          # subprocess.Popen(om, shell=True)


    #     #subprocess.Popen('start chrome  www.google.com', shell=True)
    #     subprocess.Popen(
    #         'blender -b newdotblend -E CYCLES -s 1 -e 10 -a',
    #         shell=True)
    #     subprocess.call(["pause"], shell=True)int

    def submitbutton(self):

      try:
         msgg = messagebox.askokcancel(title="Details",
                                      message="Your rendered files will be saved as per your blender settings, press Ok to continue")

         self.numbframe= self.noframetxt.get()
         self.startframe = self.startframetxt.get()
         self.endframe = self.endframetxt.get()
         self.timeint = self.timetxt.get()
         print(self.numbframe,self.startframe,self.endframe,self.timeint)
         #changing the got value to numb
         self.numbframe=int(self.numbframe)
         self.startframe=int(self.startframe)
         self.endframe=int(self.endframe)
         self.timeint=int(self.timeint)
         print(type(self.timeint))
         print(self.numbframe, self.startframe, self.endframe, self.timeint)
         if msgg:

             pass
             self.startrender()
         else:
             exit()
      except TypeError:
            messagebox.showwarning("Alert","Browse the blend.exe and dot blend file")
      except ValueError:
            messagebox.showwarning("Alert","Enter only number")



    def helpp(self):
        self.help=messagebox.showinfo("Help","browse the blender.exe and current .blend file & Enter the values in numbers and press submit Thank you")
    def browseblendexe(self):
        self.fname = askopenfilename(filetypes=(("All files", "*.*"),
                                           ("Blend files", "*.blend"),
                                           ("exe", "*.exe")))

        #print(self.fname)
        #print (type(self.fname))
        self.fname=(self.fname[0:-12])
        #print(self.fname)

       #newfname=fname.replace('/','\\') #hange the dirctory path understandable by python to cmd command but os accepts normally
       #blendfname=[newfname]
       #print(blendfname


        if self.fname:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
                self.bloctext.insert(END, self.fname)
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % self.fname)
            return
        return self.fname#fname is passed to the startrender method

    def aboutus(self):
        self.aboutuss=messagebox.showinfo("Website","to know more about us and our projects visit www.engineerthoughts.com")



    def browsedotblend(self):
            self.dotblend = askopenfilename(filetypes=(("All files", "*.*"),
                                               ("Blend files", "*.blend"),
                                               ("exe", "*.exe")))
            print(self.dotblend)
            print(type(self.dotblend))
            self.newdotblend = self.dotblend.replace('/', '\\\\')
            self.newdotblend='"'+self.newdotblend+'"'
            print(self.newdotblend)
            if self.dotblend:
                try:
                    print("""here it comes: self.settings["template"].set(dotblend)""")
                    self.dotblendtxt.insert(END, self.dotblend)
                except:  # <- naked except is a bad idea
                    showerror("Open Source File", "Failed to read file\n'%s'" % self.dotblend)
                return
            #return self.newdotblend

        #here newdotblend is sent to the start render

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {@Yu Gothic Medium} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font17 = "-family {Microsoft JhengHei} -size 19 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1130x916+430+59")
        top.title("Blender Advanced renderer by Aranganathan")
        top.configure(background="#f9f1b9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.08, rely=0.14, relheight=0.49, relwidth=0.85)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#eadfc8")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=965)

        self.blocexe = Label(self.Frame1)
        self.blocexe.place(relx=0.0, rely=0.16, height=26, width=472)
        self.blocexe.configure(activebackground="#f9f9f9")
        self.blocexe.configure(activeforeground="black")
        self.blocexe.configure(background="#eadfc8")
        self.blocexe.configure(disabledforeground="#b3d96c")
        self.blocexe.configure(font=font10)
        self.blocexe.configure(foreground="#000000")
        self.blocexe.configure(highlightbackground="#d9d9d9")
        self.blocexe.configure(highlightcolor="black")
        self.blocexe.configure(text='''Enter or Browse the blender installed location''')

        self.bloctext = Entry(self.Frame1)
        self.bloctext.place(relx=0.52, rely=0.16, relheight=0.08, relwidth=0.34)
        self.bloctext.configure(background="white")
        self.bloctext.configure(disabledforeground="#a3a3a3")
        self.bloctext.configure(font="TkFixedFont")
        self.bloctext.configure(foreground="#000000")
        self.bloctext.configure(highlightbackground="#d9d9d9")
        self.bloctext.configure(highlightcolor="black")
        self.bloctext.configure(insertbackground="black")
        self.bloctext.configure(selectbackground="#c4c4c4")
        self.bloctext.configure(selectforeground="black")

        self.blocexe1 = Label(self.Frame1)
        self.blocexe1.place(relx=-0.01, rely=0.39, height=26, width=302)
        self.blocexe1.configure(activebackground="#f9f9f9")
        self.blocexe1.configure(activeforeground="black")
        self.blocexe1.configure(background="#eadfc8")
        self.blocexe1.configure(disabledforeground="#b3d96c")
        self.blocexe1.configure(font=font10)
        self.blocexe1.configure(foreground="#000000")
        self.blocexe1.configure(highlightbackground="#d9d9d9")
        self.blocexe1.configure(highlightcolor="black")
        self.blocexe1.configure(text='''Enter the frames per batch''')

        self.blocexe2 = Label(self.Frame1)
        self.blocexe2.place(relx=0.0, rely=0.27, height=26, width=322)
        self.blocexe2.configure(activebackground="#f9f9f9")
        self.blocexe2.configure(activeforeground="black")
        self.blocexe2.configure(background="#eadfc8")
        self.blocexe2.configure(disabledforeground="#b3d96c")
        self.blocexe2.configure(font=font10)
        self.blocexe2.configure(foreground="#000000")
        self.blocexe2.configure(highlightbackground="#d9d9d9")
        self.blocexe2.configure(highlightcolor="black")
        self.blocexe2.configure(text='''Enter or Browse the .blend file''')

        self.noframetxt = Entry(self.Frame1)
        self.noframetxt.place(relx=0.52, rely=0.39, relheight=0.05
                , relwidth=0.34)
        self.noframetxt.configure(background="white")
        self.noframetxt.configure(disabledforeground="#a3a3a3")
        self.noframetxt.configure(font="TkFixedFont")
        self.noframetxt.configure(foreground="#000000")
        self.noframetxt.configure(highlightbackground="#d9d9d9")
        self.noframetxt.configure(highlightcolor="black")
        self.noframetxt.configure(insertbackground="black")
        self.noframetxt.configure(selectbackground="#c4c4c4")
        self.noframetxt.configure(selectforeground="black")

        self.dotblendtxt = Entry(self.Frame1)
        self.dotblendtxt.place(relx=0.52, rely=0.27, relheight=0.08
                , relwidth=0.34)
        self.dotblendtxt.configure(background="white")
        self.dotblendtxt.configure(disabledforeground="#a3a3a3")
        self.dotblendtxt.configure(font="TkFixedFont")
        self.dotblendtxt.configure(foreground="#000000")
        self.dotblendtxt.configure(highlightbackground="#d9d9d9")
        self.dotblendtxt.configure(highlightcolor="black")
        self.dotblendtxt.configure(insertbackground="black")
        self.dotblendtxt.configure(selectbackground="#c4c4c4")
        self.dotblendtxt.configure(selectforeground="black")

        self.blocbut = Button(self.Frame1)
        self.blocbut.place(relx=0.87, rely=0.16, height=43, width=76)
        self.blocbut.configure(activebackground="#d9d9d9")
        self.blocbut.configure(activeforeground="#000000")
        self.blocbut.configure(background="#b9f9f2")
        self.blocbut.configure(disabledforeground="#a3a3a3")
        self.blocbut.configure(foreground="#000000")
        self.blocbut.configure(highlightbackground="#d9d9d9")
        self.blocbut.configure(highlightcolor="black")
        self.blocbut.configure(pady="0")
        self.blocbut.configure(text='''Browse''')
        self.blocbut.configure(command=self.browseblendexe)

        self.dotblendbut = Button(self.Frame1)
        self.dotblendbut.place(relx=0.87, rely=0.27, height=43, width=76)
        self.dotblendbut.configure(activebackground="#d9d9d9")
        self.dotblendbut.configure(activeforeground="#000000")
        self.dotblendbut.configure(background="#f4ecbd")
        self.dotblendbut.configure(disabledforeground="#a3a3a3")
        self.dotblendbut.configure(foreground="#000000")
        self.dotblendbut.configure(highlightbackground="#d9d9d9")
        self.dotblendbut.configure(highlightcolor="black")
        self.dotblendbut.configure(pady="0")
        self.dotblendbut.configure(text='''Browse''')
        self.dotblendbut.configure(command=self.browsedotblend)

        self.blocexe3 = Label(self.Frame1)
        self.blocexe3.place(relx=0.0, rely=0.5, height=26, width=262)
        self.blocexe3.configure(activebackground="#f9f9f9")
        self.blocexe3.configure(activeforeground="black")
        self.blocexe3.configure(background="#eadfc8")
        self.blocexe3.configure(disabledforeground="#b3d96c")
        self.blocexe3.configure(font=font10)
        self.blocexe3.configure(foreground="#000000")
        self.blocexe3.configure(highlightbackground="#d9d9d9")
        self.blocexe3.configure(highlightcolor="black")
        self.blocexe3.configure(text='''Enter the Starting Frame''')

        self.endframetxt = Entry(self.Frame1)
        self.endframetxt.place(relx=0.52, rely=0.61, relheight=0.05
                , relwidth=0.34)
        self.endframetxt.configure(background="white")
        self.endframetxt.configure(disabledforeground="#a3a3a3")
        self.endframetxt.configure(font="TkFixedFont")
        self.endframetxt.configure(foreground="#000000")
        self.endframetxt.configure(highlightbackground="#d9d9d9")
        self.endframetxt.configure(highlightcolor="black")
        self.endframetxt.configure(insertbackground="black")
        self.endframetxt.configure(selectbackground="#c4c4c4")
        self.endframetxt.configure(selectforeground="black")

        self.startframetxt = Entry(self.Frame1)
        self.startframetxt.place(relx=0.52, rely=0.5, relheight=0.05
                , relwidth=0.34)
        self.startframetxt.configure(background="white")
        self.startframetxt.configure(disabledforeground="#a3a3a3")
        self.startframetxt.configure(font="TkFixedFont")
        self.startframetxt.configure(foreground="#000000")
        self.startframetxt.configure(highlightbackground="#d9d9d9")
        self.startframetxt.configure(highlightcolor="black")
        self.startframetxt.configure(insertbackground="black")
        self.startframetxt.configure(selectbackground="#c4c4c4")
        self.startframetxt.configure(selectforeground="black")

        self.timetxt = Entry(self.Frame1)
        self.timetxt.place(relx=0.52, rely=0.72, relheight=0.05, relwidth=0.34)
        self.timetxt.configure(background="white")
        self.timetxt.configure(disabledforeground="#a3a3a3")
        self.timetxt.configure(font="TkFixedFont")
        self.timetxt.configure(foreground="#000000")
        self.timetxt.configure(highlightbackground="#d9d9d9")
        self.timetxt.configure(highlightcolor="black")
        self.timetxt.configure(insertbackground="black")
        self.timetxt.configure(selectbackground="#c4c4c4")
        self.timetxt.configure(selectforeground="black")

        self.blocexe6 = Label(self.Frame1)
        self.blocexe6.place(relx=0.0, rely=0.61, height=26, width=262)
        self.blocexe6.configure(activebackground="#f9f9f9")
        self.blocexe6.configure(activeforeground="black")
        self.blocexe6.configure(background="#eadfc8")
        self.blocexe6.configure(disabledforeground="#b3d96c")
        self.blocexe6.configure(font=font10)
        self.blocexe6.configure(foreground="#000000")
        self.blocexe6.configure(highlightbackground="#d9d9d9")
        self.blocexe6.configure(highlightcolor="black")
        self.blocexe6.configure(text='''Enter the Ending Frame''')

        self.blocexe4 = Label(self.Frame1)
        self.blocexe4.place(relx=0.01, rely=0.72, height=26, width=482)
        self.blocexe4.configure(activebackground="#f9f9f9")
        self.blocexe4.configure(activeforeground="black")
        self.blocexe4.configure(background="#eadfc8")
        self.blocexe4.configure(disabledforeground="#b3d96c")
        self.blocexe4.configure(font=font10)
        self.blocexe4.configure(foreground="#000000")
        self.blocexe4.configure(highlightbackground="#d9d9d9")
        self.blocexe4.configure(highlightcolor="black")
        self.blocexe4.configure(text='''Enter the Time between each frame in seconds''')

        self.submitbut = Button(self.Frame1)
        self.submitbut.place(relx=0.8, rely=0.81, height=53, width=156)
        self.submitbut.configure(activebackground="#d9d9d9")
        self.submitbut.configure(activeforeground="#000000")
        self.submitbut.configure(background="#b8c0fa")
        self.submitbut.configure(disabledforeground="#a3a3a3")
        self.submitbut.configure(foreground="#000000")
        self.submitbut.configure(highlightbackground="#d9d9d9")
        self.submitbut.configure(highlightcolor="black")
        self.submitbut.configure(pady="0")
        self.submitbut.configure(text='''Submit''')
        self.submitbut.configure(command=self.submitbutton)

        self.cancelbut = Button(self.Frame1)
        self.cancelbut.place(relx=0.59, rely=0.81, height=53, width=156)
        self.cancelbut.configure(activebackground="#d9d9d9")
        self.cancelbut.configure(activeforeground="#000000")
        self.cancelbut.configure(background="#b8c0fa")
        self.cancelbut.configure(disabledforeground="#a3a3a3")
        self.cancelbut.configure(foreground="#000000")
        self.cancelbut.configure(highlightbackground="#d9d9d9")
        self.cancelbut.configure(highlightcolor="black")
        self.cancelbut.configure(pady="0")
        self.cancelbut.configure(text='''Cancel''')

        self.helpbut = Button(self.Frame1)
        self.helpbut.place(relx=0.87, rely=0.47, height=83, width=101)
        self.helpbut.configure(activebackground="#d9d9d9")
        self.helpbut.configure(activeforeground="#000000")
        self.helpbut.configure(background="#80ff00")
        self.helpbut.configure(disabledforeground="#a3a3a3")
        self.helpbut.configure(font=font17)
        self.helpbut.configure(foreground="#000000")
        self.helpbut.configure(highlightbackground="#d9d9d9")
        self.helpbut.configure(highlightcolor="black")
        self.helpbut.configure(pady="0")
        self.helpbut.configure(text='''HELP''')
        self.helpbut.configure(width=101)
        self.helpbut.configure(command=self.helpp)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.08, rely=0.01, relheight=0.11, relwidth=0.85)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#b6fcf9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=965)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.16, rely=0.1, height=56, width=642)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#b6fcf9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''BLENDER ADVANCED RENDERER''')

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.08, rely=0.64, relheight=0.22, relwidth=0.85)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#f9f1b9")
        self.Frame3.configure(highlightbackground="#f9f1b9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=965)

        self.Label2 = Label(self.Frame3)
        self.Label2.place(relx=0.24, rely=0.4, height=56, width=552)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#badca3")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''BY ENGINEER THOUGHTS''')

        self.blocexe5 = Label(self.Frame3)
        self.blocexe5.place(relx=0.0, rely=0.25, height=26, width=952)
        self.blocexe5.configure(activebackground="#f9f9f9")
        self.blocexe5.configure(activeforeground="black")
        self.blocexe5.configure(background="#f9f1b9")
        self.blocexe5.configure(disabledforeground="#b3d96c")
        self.blocexe5.configure(font=font10)
        self.blocexe5.configure(foreground="#000000")
        self.blocexe5.configure(highlightbackground="#d9d9d9")
        self.blocexe5.configure(highlightcolor="black")
        self.blocexe5.configure(text='''வாழ்க வளமுடன் All is well with GOD's blessings''')


        self.aboutbut1 = Button(self.Frame3)
        self.aboutbut1.place(relx=0.4, rely=0.06, height=33, width=171)
        self.aboutbut1.configure(activebackground="#d9d9d9")
        self.aboutbut1.configure(activeforeground="#000000")
        self.aboutbut1.configure(background="#c0c0c0")
        self.aboutbut1.configure(disabledforeground="#a3a3a3")
        self.aboutbut1.configure(foreground="#000000")
        self.aboutbut1.configure(highlightbackground="#d9d9d9")
        self.aboutbut1.configure(highlightcolor="black")
        self.aboutbut1.configure(pady="0")
        self.aboutbut1.configure(text='''Know more about us''')
        self.aboutbut1.configure(command=self.aboutus)

        self.blocexe7 = Label(self.Frame3)
        self.blocexe7.place(relx=0.35, rely=0.74, height=35, width=305)
        self.blocexe7.configure(activebackground="#f9f9f9")
        self.blocexe7.configure(activeforeground="black")
        self.blocexe7.configure(background="#f9f1b9")
        self.blocexe7.configure(disabledforeground="#b3d96c")
        self.blocexe7.configure(font=font10)
        self.blocexe7.configure(foreground="#000000")
        self.blocexe7.configure(highlightbackground="#f9f9f9")
        self.blocexe7.configure(highlightcolor="black")
        self.blocexe7.configure(text='''www.engineerthoughts.com''')
        self.blocexe7.configure(width=305)






if __name__ == '__main__':
    vp_start_gui()



