# -*- coding: utf-8 -*-
import sys
import os
import zipfile
from Tkinter import *
import tkFileDialog
import tkMessageBox

reload(sys)
sys.setdefaultencoding('utf-8')


def rename(path_extract=None, new_name=None):
    path_extract += '\\' + new_name
    drawables = os.listdir(path_extract)
    for drawable in drawables:
        path_drawable_src = path_extract + '\\' + drawable + '\\' + os.listdir(path_extract + '\\' + drawable)[0]
        path_drawable_dst = path_extract + '\\' + drawable + '\\' + new_name + '.png'
        os.rename(path_drawable_src, path_drawable_dst)


def unzip(path_file=None, path_extract=None, new_name=None):
    path_extract += '\\' + new_name
    if not os.path.exists(path_extract):
        os.makedirs(path_extract)
    if zipfile.is_zipfile(path_file):
        zf = zipfile.ZipFile(path_file)
        zf.extractall(path_extract)
        zf.close()


def get_name(path_file):
    list = path_file.split('\\')
    name = list[len(list) - 1].split('.')[0]
    return name


def start(path_file=None, path_extract=None, path_extract_name=None):
    unzip(path_file, path_extract, path_extract_name)
    rename(path_extract, path_extract_name)


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.selectOriginFileLabelHint = Label(self, text='请选择文件：')
        self.selectOriginFileLabelHint.grid(row=0, column=0)
        self.selectOriginFileEntry = Entry(self, width=50)
        self.selectOriginFileEntry.grid(row=0, column=1)
        self.selectOriginFileButton = Button(self, text='选择', command=self.selectOriginFile)
        self.selectOriginFileButton.grid(row=0, column=2)

        self.inputTargetDrawableNameLabelHint = Label(self, text='请输入目标名称：')
        self.inputTargetDrawableNameLabelHint.grid(row=1, column=0)
        self.inputTargetDrawableNameEntry = Entry(self, width=50)
        self.inputTargetDrawableNameEntry.grid(row=1, column=1)

        self.startButton = Button(self, text='开始', command=self.startRename, width=50)
        self.startButton.grid(row=2, column=1, pady=30)

    def selectOriginFile(self):
        filename = tkFileDialog.askopenfilename()
        if filename != '':
            path = filename
            path_file = path
            print path_file
            self.selectOriginFileEntry.delete(0, END)
            self.selectOriginFileEntry.insert(0, path_file)
        else:
            print '您没有选择任何文件'

    def startRename(self):
        path_file = self.selectOriginFileEntry.get()
        path_extract = os.path.dirname(path_file)
        path_extract_name = self.inputTargetDrawableNameEntry.get()
        if len(path_file) > 0 and len(path_extract) > 0 and len(path_extract_name) > 0:
            start(path_file, path_extract, path_extract_name)
        else:
            tkMessageBox.askquestion('提示', '请输入正确的数据')


app = Application()
app.master.title('Android Drawable重命名')
# app.master.geometry('600x600')
app.mainloop()
