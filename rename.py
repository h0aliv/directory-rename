from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os

def change_text(label, text):
    label.setText(text)

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Renamer")
        self.height = 300
        self.width = 300
        self.test_text = ""
        self.addprefix = "add prefix"
        self.addsuffix = "add suffix"
        self.entirename = "change entire name with sequence number"
        self.replace = "replace phrase"
        self.directory = ""
        self.previousName = []

    def setup_UI(self):
        self.frame = QFrame()
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.mid_layout = QHBoxLayout()
        self.mid_sublayout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.bottom_sublayout = QHBoxLayout()


        #Input textfield
        self.input_label = QLabel('Input text for action')
        self.input = QLineEdit()
        self.text_replace = QLineEdit()
        self.replace_indic = QLabel("the Pattern you want to replace")

        #indication text
        self.target_path = QLabel('Target Directory')

        #Textfield for specified extension
        self.extension_indic = QLabel('File Extension that you want to specify')
        self.extension_textfield = QLineEdit()
        self.hide_extension_widget()

        #drop down selection for rename action
        self.actiontype = QComboBox()
        self.actiontype.addItem(self.addprefix)
        self.actiontype.addItem(self.addsuffix)
        self.actiontype.addItem(self.entirename)
        self.actiontype.addItem(self.replace)

        #Directory update button
        self.button = QPushButton('Select Directory')
        self.button.setMinimumSize(50, 10)
        self.button.setMaximumSize(100, 20)
        self.button.clicked.connect(self.upadate_path)

        #Rename button
        self.rename_b = QPushButton('Rename!')
        self.rename_b.clicked.connect(self.rename)

        #Textfield for directory path
        self.textbox = QLineEdit(self)

        #Checkbox for specified extension
        self.specified =QCheckBox('Only rename file with specified extension')
        self.specified.stateChanged.connect(self.check_state)

        # set up layout
        self.top_layout.addWidget(self.target_path)
        self.top_layout.addWidget(self.textbox)
        self.top_layout.addWidget(self.button)

        self.mid_layout.addWidget(self.actiontype)
        self.mid_layout.addWidget(self.specified)

        self.mid_sublayout.addWidget(self.extension_indic)
        self.mid_sublayout.addWidget(self.extension_textfield)

        self.bottom_layout.addWidget(self.input_label)
        self.bottom_layout.addWidget(self.input)

        self.bottom_sublayout.addWidget(self.replace_indic)
        self.bottom_sublayout.addWidget(self.text_replace)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.mid_layout)
        self.main_layout.addLayout(self.mid_sublayout)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addLayout(self.bottom_sublayout)
        self.main_layout.addWidget(self.rename_b)

        self.frame.setLayout(self.main_layout)

        self.setCentralWidget(self.frame)

    #update the displayed path to selected path
    def upadate_path(self):
        self.file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        #.test_text = self.actiontype.currentText()
        self.textbox.setText(self.file)
        print(self.textbox.displayText())

    #check the state of extension specified checkbox to decide whether to show the widgets in mid sublayout
    def check_state(self):

        if self.specified.checkState() == 2:
            self.show_extension_widget()
        else:
            self.hide_extension_widget()

    def hide_extension_widget(self):
        self.extension_indic.hide()
        self.extension_textfield.hide()

    def show_extension_widget(self):
        self.extension_indic.show()
        self.extension_textfield.show()

    #main rename function, perform the aciton that is selected action
    def rename(self):
        self.previousName = []
        i = 0
        self.directory = self.textbox.displayText()

        self.state = self.specified.checkState() #check the state of specify checkbox
        print(self.actiontype.currentText())
        #entire name
        if self.actiontype.currentText() == self.entirename:
            for name in os.listdir(self.directory):
                try:
                    self.directory = self.textbox.displayText()
                    head, tail = os.path.splitext(name)
                    if self.state == 2:
                        if tail == self.extension_textfield.displayText():
                            os.rename(self.directory + "/" + name, self.directory + "/" + self.input.displayText() + tail)
                    else:
                        os.rename(self.directory + "/" + name, self.directory + "/" + self.input.displayText() + tail)

                    self.previousName.append(head)
                except FileExistsError:
                    os.rename(self.directory + "/" + name, self.directory + "/" + self.input.displayText() + str(i) + tail)
                    i += 1
                    continue
        #suffix
        elif self.actiontype.currentText() == self.addsuffix:
            for name in os.listdir(self.directory):
                head, tail = os.path.splitext(name)
                if self.state == 2:
                    if tail == self.extension_textfield.displayText():
                        os.rename(self.directory + "/" + name,
                                  self.directory + "/" + head + self.input.displayText() + tail)
                else:
                    os.rename(self.directory + "/" + name,
                              self.directory + "/" + head + self.input.displayText() + tail)

                self.previousName.append(head)
        #prefix
        elif self.actiontype.currentText() == self.addprefix:
            for name in os.listdir(self.directory):
                head, tail = os.path.splitext(name)
                if self.state == 2:
                    if tail == self.extension_textfield.displayText():
                        os.rename(self.directory + "/" + name, self.directory + "/" + self.input.displayText() + head + tail)
                else:
                    os.rename(self.directory + "/" + name, self.directory + "/" + self.input.displayText() + head + tail)

                self.previousName.append(head)
        #replace
        elif self.actiontype.currentText() == self.replace:
            for name in os.listdir(self.directory):
                head, tail = os.path.splitext(name)
                if self.state == 2:
                    if tail == self.extension_textfield.displayText():
                        head = head.replace(self.text_replace.displayText(), self.input.displayText())
                        os.rename(self.directory + "/" + name, self.directory + "/" + head + tail)
                else:
                    head = head.replace(self.text_replace.displayText(), self.input.displayText())
                    os.rename(self.directory + "/" + name, self.directory + "/" + head + tail)



                self.previousName.append(head)










class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window22222")



if __name__ == "__main__":
    app = QApplication([])
    window = main_window()
    window.setup_UI()

    window2 = Window2()

    window.show()
    app.exec_()