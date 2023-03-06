import sys
import random
from new_user import *
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QGuiApplication

from PyQt5.QtCore import pyqtSignal, QObject
import os
import webbrowser

######
#   Coded By Vitor Hugo Borges Dos Santos
#   github.com/vbsx
######

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.handle_paths = PathHandle()
        image_icon_path = 'user.png'
        self.github_icon = 'github.png'
        #config of the window
        self.setStyleSheet("padding :15px;background-color: #00008b;color: #FFFFFF ")
        self.setWindowIcon(QtGui.QIcon(image_icon_path))
        self.setWindowTitle('Password Generator')
        self.resize(400, 200)
        #
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 
             'v', 'w', 'x', 'y', 'z']
        self.especialchars = ['#', '@', '$', '%']
        self.button = QtWidgets.QPushButton("Gerar uma senha")                     
        self.btn = QtWidgets.QPushButton('Usar esta senha', clicked=self.password_to_user)
      
        self.text = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.text_user = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.text_user.setText("Coloque o nome da pessoa")
        self.user = QtWidgets.QLineEdit()
        self.cpf = QtWidgets.QLineEdit()
        self.text_cpf = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.text_cpf.setText("Coloque o cpf da pessoa")
        self.button.clicked.connect(self.magic)
        self.button_git = QtWidgets.QPushButton('Visite Meu Github', clicked=self.open_git_on_web)
        
        self.cpf.setStyleSheet("background-color: #008b8b;color: #000000")
        self.user.setStyleSheet("background-color: #FFFFFF;color: #000000")
        self.text_user.setStyleSheet("background-color: #008b8b;color: #000000")
        self.cpf.setStyleSheet("background-color: #FFFFFF;color: #000000")
        self.btn.setStyleSheet("background-color: #008b8b;color: #000000")
        self.button.setStyleSheet("background-color: #008b8b;color: #000000")
        self.text_cpf.setStyleSheet("background-color: #008b8b;color: #000000")
        self.button_git.setIcon(QtGui.QIcon(self.github_icon))
        self.button_git.setIconSize(QtCore.QSize(64,64))
        self.button_git.setStyleSheet("margin-top:20px;background-color: #008b8b;color: #000000")
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.text_user)
        self.layout.addWidget(self.user)
        self.layout.addWidget(self.text_cpf)
        self.layout.addWidget(self.cpf)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.button_git)
        
        
    def verify_user_and_password_not_empty(self, user, cpf):
        if user and cpf:
            return True 
        
        
        else:
            self.show_dialog("Coloque um usuário ou senha primeiro!")
            
            
    def password_to_user(self):
        password = self.text.text()
        user = self.user.text()
        cpf = self.cpf.text()
        self.segunda_tela = Second_Widget(self.user.text(), self.cpf.text(), self.text.text())
        if self.verify_user_and_password_not_empty(user, cpf) == True:
        
            
            if password:
                self.close()
                self.segunda_tela.show()


            else:
                self.show_dialog("Gere uma senha primeiro!")
                
        
    def magic(self):
        self.text.setText(str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          str(random.randrange(1, 10))+
                          random.choice(self.especialchars)+
                          random.choice(self.letters)+
                          random.choice(self.letters)+
                          random.choice(self.letters)+
                          random.choice(self.letters))
      
        
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
        
        
    def open_git_on_web(self):
        webbrowser.open_new_tab(
        'https://github.com/vbsx'
        )


class Second_Widget(QtWidgets.QWidget):
    def __init__(self, user, cpf, password):
        super().__init__()
        self.handle_paths = PathHandle()
        image_path = 'user.png'
        
        #config of the window
        self.resize(400, 200)
        self.setStyleSheet("padding :15px;background-color: #120458; color: #FFFFFF")
        self.setWindowIcon(QtGui.QIcon('user.png'))
        self.setWindowTitle('Novo Usuário')
        self.setWindowIcon(QtGui.QIcon(image_path))
        #
        self.new_user = Usuario(user, cpf)
        self.lbl = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.lbl.setText("")
        self.password = password

        self.button_copy_password = QtWidgets.QPushButton('Copiar a senha', clicked=self.copy_password)
        self.button_copy_username = QtWidgets.QPushButton('Copiar o nome', clicked=self.copy_username)
        self.button_copy_cpf = QtWidgets.QPushButton('Copiar cpf', clicked=self.copy_cpf)
        self.button_copy_reset_senha = QtWidgets.QPushButton('Copiar mensagem reset', clicked=self.copy_message_reset)
        self.button_copy_novo_user = QtWidgets.QPushButton('Copiar mensagem novo usuário', clicked=self.copy_message_new_user)
        self.close_window = QtWidgets.QPushButton("VOLTAR", clicked=self.open_first_window)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.close_window)
        self.layout.addWidget(self.lbl)
        self.layout.addWidget(self.button_copy_password)
        self.layout.addWidget(self.button_copy_username)
        self.layout.addWidget(self.button_copy_cpf)
        self.layout.addWidget(self.button_copy_reset_senha)
        self.layout.addWidget(self.button_copy_novo_user)
        
        
        self.button_copy_password.setStyleSheet("background-color: #008b8b;color: #000000")
        self.button_copy_username.setStyleSheet("background-color: #008b8b;color: #000000")
        self.button_copy_cpf.setStyleSheet("background-color: #008b8b;color: #000000")
        self.button_copy_novo_user.setStyleSheet("background-color: #008b8b;color: #000000")
        self.button_copy_reset_senha.setStyleSheet("background-color: #008b8b;color: #000000")
        self.close_window.setStyleSheet("background-color: #008b8b;color: #000000")
    
    
    def copy_password(self):
        clip = QGuiApplication.clipboard()
        clip.clear()
        clip.setText(self.password)

         
    def copy_username(self):
        user = self.new_user.filtrar_nome()
        clip = QGuiApplication.clipboard()
        clip.clear()
        clip.setText(user)
        

    def copy_cpf(self):
        cpf = self.new_user.filtrar_cpf()
        clip = QGuiApplication.clipboard()
        clip.clear()
        clip.setText(cpf)
        
        
    def copy_message_reset(self):
        message = self.new_user.reset_senha(self.password)
        clip = QGuiApplication.clipboard()
        clip.clear()
        clip.setText(message)
        self.show_dialog('O Conteúdo foi copiado para a area de transferência')
        
        
    def copy_message_new_user(self):
        message = self.new_user.novo_usuario(self.password)
        clip = QGuiApplication.clipboard()
        clip.clear()
        clip.setText(message)
        self.show_dialog('O Conteúdo foi copiado para a area de transferência')


    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
    
    def open_first_window(self):
        self.first_window = MyWidget()
        self.close()
        self.first_window.show()

class PathHandle():

    def resource_path(self,relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
