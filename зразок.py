import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Діалог відкриття файлів (і папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
 
from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
 
from PIL import Image
 
app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()
 
btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Відзеркалити")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")
 
row = QHBoxLayout()          # Головна лінія
col1 = QVBoxLayout()         # ділиться на два стовпці
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # в першому - кнопка вибору каталогу
col1.addWidget(lw_files)     # і список файлов
col2.addWidget(lb_image, 95) # в другому - картинка
row_tools = QHBoxLayout()    # і ряд кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)
 
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
 
win.show()
 
workdir = ''
 
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
 
def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()
 
def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
 
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)
 
btn_dir.clicked.connect(showFilenamesList)
 
class ImageProcessor():
   def __init__(self):
       pass #slide 27
 
   def loadImage(self, dir, filename):
       pass #slide 28, 30
 
   def do_bw(self):
       pass #slide 50
 
   def saveImage(self):
       pass #slide 53
       
 
   def showImage(self, path):
         #slide 31, 37
 
def showChosenImage():
   pass #slide 40
 
workimage = ImageProcessor() #поточне робоче зображення для роботи
lw_files.currentRowChanged.connect(showChosenImage)
 
btn_bw.clicked.connect(workimage.do_bw)
 
app.exec()
