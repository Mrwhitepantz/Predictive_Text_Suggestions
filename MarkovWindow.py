from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import os
from os import path

class MarkovWindow(QMainWindow):
		def __init__(self):
			super(MarkovWindow, self).__init__()
			self.setGeometry(800,500,600,400)
			self.setWindowTitle("Predictive Text Generator")

			widget = QWidget()
			self.setCentralWidget(widget)
			self.setStyleSheet("backgorund-color:#ECECEC")

			VLayout = QVBoxLayout()
			widget.setLayout(VLayout)
			ButtonLayout = QHBoxLayout()
			TopLayout = QVBoxLayout()
			ChoiceLayout = QHBoxLayout()
			font = QFont("Arial", 18)



			# -- Menu Options --
			menu = self.menuBar().addMenu("&Action")
			newAct = QAction("&New", self, shortcut=QKeySequence.New, triggered = self.newSentence)
			menu.addAction(newAct)
			menu.addSeparator()
			quitAct = QAction("&Quit", self, shortcut=QKeySequence.Quit, triggered = self.close)
			menu.addAction(quitAct)

			# -- Model Selection --
			self.model_dir = "models"
			self.comboBox = QComboBox(self)
			for file in os.listdir(self.model_dir):
				fname, ext = path.splitext(file)
				nameParts = fname.split('_')
				name = " ".join(nameParts)
				self.comboBox.addItem(str.title(name))
			self.comboBox.setFont(font)
			self.comboBox.setFixedWidth(200)
			self.comboBox.adjustSize()

			# -- Seed Creation --
			self.starterText = QTextEdit(self, placeholderText="Type a 2 word seed.")
			self.starterText.setFont(font)


			# -- Start Button --
			self.startBtn = QPushButton("Start generating...",self)
			self.startBtn.clicked.connect(self.start)

			# -- Typed Paragraph --
			self.sentenceBox = QLabel(self)
			self.sentenceBox.setFixedWidth(600)
			self.sentenceBox.setWordWrap(True)
			self.sentenceBox.setText("")
			self.sentenceBox.setFont(font)

			# -- Word Choice Buttons --
			self.buttons = []
			for i in range(3):
				button = QPushButton()
				button.clicked.connect(self.nextWord)
				button.setFont(font)
				button.setFixedWidth(200)
				button.setProperty("mySeq", "")
				self.buttons.append(button)
				ButtonLayout.addWidget(self.buttons[i])

			# -- Add Layouts --
			spacer = QLabel(self)
			ChoiceLayout.addWidget(self.comboBox,1)
			ChoiceLayout.addWidget(spacer,1)
			ChoiceLayout.addWidget(self.starterText,1)
			TopLayout.addLayout(ChoiceLayout,1)
			TopLayout.addWidget(self.startBtn,1)
			TopLayout.addWidget(self.sentenceBox,5)
			VLayout.addLayout(TopLayout)
			VLayout.addLayout(ButtonLayout)

			self.newSentence()
		
		def newSentence(self):
			self.sentenceBox.setText("")
			self.startBtn.show()
			self.comboBox.setCurrentIndex(0)
			for button in self.buttons:
				button.setEnabled(True)

		def start(self):
			self.sentence = ""
			self.seed = self.starterText.toPlainText()
			self.sentence = "".join(self.seed)
			if (len(self.seed.split()) == 2):
				self.startBtn.hide()
				self.sentenceBox.setText(self.sentence)
				self.populateSequences()
			else:
				self.startBtn.setText("Wrong number of starter words. Try again...")

		# populateSequences()
		# Adds all lines from the file specified in the
		# comboBox to a list

		def populateSequences(self):
		 	self.seq_list = []

		 	self.line1 = self.seed.lower()
		 	self.tModel = "models/" + self.comboBox.currentText().lower().replace(' ','_') + '.txt'
		 	with open(self.tModel,"r") as file:
		 		for line in file:
		 			self.seq_list.append(line)
		 	self.populateButtons()

		 # populateButtons()
		 # Finds lines that match the previous two words
		 # and suggests the next one

		def populateButtons(self):
			self.line2 = ""
			self.poss_seq = []
			seq_dict = {}
			count=1
			for seq in self.seq_list:
				if (self.line1.split()[0:2] == seq.split()[0:2]):
					self.poss_seq.append(seq)
			denylist = []
			for button in self.buttons:
				try:
					key = random.choice(self.poss_seq)
					count = 1
					while (key in denylist):
						key = random.choice(self.poss_seq)
						if (count > 50):
							key = ""
							break
						count+=1
					denylist.append(key)
					print(key)
					seq = " ".join(key.split()[-2:])
					word = "".join(key.split()[-1:])
					button.setText(word)
					button.setEnabled(True)
					button.setProperty("mySeq", seq)
				except:
					traceback.print_exc()
					button.setText("")
					button.setProperty("mySeq", "")
					button.setEnabled(False)
			denylist = []


		# nextWord()
		# Adds the chosen word to the end of the sentence
		# and calls for the buttons to populate again

		def nextWord(self):
			clicked = self.sender()
			seq = clicked.property("mySeq")
			self.line2 = " ".join(seq.split()[-2:])
			self.sentence = self.sentence + " " + "".join(self.line2.split()[-1:])
			self.sentenceBox.setText(self.sentence)
			self.line1 = self.line2
			self.populateButtons()