import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Main(QtGui.QMainWindow):
	def __init__(self, parent = None):
		QtGui.QMainWindow.__init__(self, parent)

		self.filename = ""

		self.initUI()

	def initToolbar(self):

		self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"), "New", self)
		self.newAction.setStatusTip("Create a new document from scratch.")
		self.newAction.setShortcut("Ctrl+N")
		self.newAction.triggered.connect(self.new)

		self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"), "Open", self)
		self.openAction.setStatusTip("Open a document.")
		self.openAction.setShortcut("Ctrl+N")
		self.openAction.triggered.connect(self.open)
		
		self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"), "Save", self)
		self.saveAction.setStatusTip("Save a document.")
		self.saveAction.setShortcut("Ctrl+S")
		self.saveAction.triggered.connect(self.save)
		
		self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"), "Print", self)
		self.printAction.setStatusTip("Print a document.")
		self.printAction.setShortcut("Ctrl+P")
		self.printAction.triggered.connect(self.print)
		
		self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"), "Preview", self)
		self.previewAction.setStatusTip("Preview document.")
		self.previewAction.setShortcut("Ctrl+Shift+P")
		self.previewAction.triggered.connect(self.preview)

		self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"), "Cut", self)
		self.cutAction.setStatusTip("Cut.")
		self.cutAction.setShortcut("Ctrl+X")
		self.cutAction.triggered.connect(self.text.cut)

		self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"), "Copy", self)
		self.copyAction.setStatusTip("Copy.")
		self.copyAction.setShortcut("Ctrl+C")
		self.copyAction.triggered.connect(self.text.copy)

		self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"), "Paste", self)
		self.pasteAction.setStatusTip("Paste.")
		self.pasteAction.setShortcut("Ctrl+V")
		self.pasteAction.triggered.connect(self.text.paste)

		self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"), "Undo", self)
		self.undoAction.setStatusTip("Undo.")
		self.undoAction.setShortcut("Ctrl+Z")
		self.undoAction.triggered.connect(self.text.undo)

		self.previewAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"), "Redo", self)
		self.previewAction.setStatusTip("Redo.")
		self.previewAction.setShortcut("Ctrl+Y")
		self.previewAction.triggered.connect(self.text.redo)

		bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"), "Insert bullet List", self)
		bulletAction.setStatusTip("Insert bullet list")
		bulletAction.setShortcut("Ctrl+Shift+B")
		bulletAction.triggered.connect(self.bulletList)

		numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"), "Insert numbered List", self)
		numberedAction.setStatusTip("Insert numbered list")
		numberedAction.setShortcut("Ctrl+Shift+L")
		numberedAction.triggered.connect(self.numberList)

		self.toolbar = self.addToolBar("Options")

		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)
		self.toolbar.addAction(self.printAction)
		self.toolbar.addAction(self.previewAction)
		self.toolbar.addAction(self.cutAction)
		self.toolbar.addAction(self.copyAction)
		self.toolbar.addAction(self.pasteAction)
		self.toolbar.addAction(self.undoAction)
		self.toolbar.addAction(self.redoAction)
		self.toolbar.addAction(bulletAction)
		self.toolbar.addAction(numberedAction)

		self.toolbar.addSeparator()

		# Makes the next Toolbar appear underneath this one
		self.addToolBarBreak()

	def initFormatbar(self):

		fontBox = QtGui.QFontComboBox(self)
		fontBox.currentFontChanged.connect(self.fontFamily)

		fontSize = QtGui.QFontComboBox(self)
		fontSize.setEditable(True)

		# Minimum number of chars displayed
		fontSize.setMinimumContentsLength(3)

		fontSize.activated.connect(self.fontSize)

		# Typical font sizes
		fontSizes = ['6','7','8','9','10','11','12','13','14',
					'15','16','18','20','22','24','26','28',
					'32','36','40','44','48','54','60','66',
					'72','80','88','96']
		
		for i in fontSizes:
			fontSize.addItem(i)

		fontColor = QtGui.QAction(QtGui.QIcon("icons/font-color.png"), "Change font color", self)
		fontColor.triggered.connect(self.fontColor)

		backColor = QtGui.QAction(QtGui.QIcon("icons/highlight.png"), "Change background", self)
		backColor.triggered.connect(self.backColor)

		boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"), "Bold", self)
		boldAction.triggered.connect(self.bold)

		italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"), "Italic", self)
		italicAction.triggered.connect(self.italic)	

		underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"), "Underline", self)
		underlAction.triggered.connect(self.underline)	

		strikeAction = QtGui.QAction(QtGui.QIcon("icons/strike.png"), "Strike-out", self)
		strikeAction.triggered.connect(self.strike)

		superAction = QtGui.QAction(QtGui.QIcon("icons/superscript.png"), "Superscript", self)
		superAction.triggered.connect(self.suerScript)	

		subAction = QtGui.QAction(QtGui.QIcon("icons/subscript.png"), "Subscript", self)
		subAction.triggered.connect(self.subScript)

		alignLeft = QtGui.QAction(QtGui.QIcon("icons/align-left.png"), "Align left", self)
		alignLeft.triggered.connect(self.alignLeft)

		alignCenter = QtGui.QAction(QtGui.QIcon("icons/align-center.png"), "Align center", self)
		alignCenter.triggered.connect(self.alignCenter)

		alignRight = QtGui.QAction(QtGui.QIcon("icons/align-right.png"), "Align right", self)
		alignRight.triggered.connect(self.alignRight)

		alignJustify = QtGui.QAction(QtGui.QIcon("icons/align-justify.png"), "Align justify", self)
		alignJustify.triggered.connect(self.alignJustify)

		indentAction = QtGui.QAction(QtGui.QIcon("icons/indent.png"), "Indent Area", self)
		indentAction.setShortcut("Ctrl+Tab")
		indentAction.triggered.connect(self.indent)

		dedentAction = QtGui.QAction(QtGui.QIcon("icons/dedent.png"), "Dedent Area", self)
		dedentAction.setShortcut("Shift+Tab")
		dedentAction.triggered.connect(self.dedent)
		

		self.formatbar = self.addToolBar("Format")

		self.formatbar.addWidget(fontBox)
		self.formatbar.addWidget(fontSize)

		self.formatbar.addSeparator()

		self.formatbar.addAction(fontColor)
		self.formatbar.addAction(backColor)

		self.formatbar.addSeparator()

		self.formatbar.addAction(boldAction)
		self.formatbar.addAction(italicAction)
		self.formatbar.addAction(underlAction)
		self.formatbar.addAction(strikeAction)
		self.formatbar.addAction(superAction)
		self.formatbar.addAction(subAction)
		
		self.formatbar.addSeparator()

		self.formatbar.addAction(alignLeft)
		self.formatbar.addAction(alignCenter)
		self.formatbar.addAction(alignRight)
		self.formatbar.addAction(alignJustify)

		self.formatbar.addSeparator()

		self.formatbar.addAction(indentAction)
		self.formatbar.addAction(dedentAction)


	def initMenubar(self):

		menubar =self.menuBar()

		file = menubar.addMenu("File")
		edit = menubar.addMenu("Edit")
		view = menubar.addMenu("View")

		file.addAction(self.newAction)
		file.addAction(self.openAction)
		file.addAction(self.saveAction)
		file.addAction(self.printAction)
		file.addAction(self.previewAction)

		edit.addAction(self.undoAction)
		edit.addAction(self.redoAction)
		edit.addAction(self.cutAction)
		edit.addAction(self.copyAction)
		edit.addAction(self.pasteAction)

		toolbarAction.QtGui.QAction("Toggle Toolbar", self)
		toolbarAction.triggered.connect(self.toggleToolbar)

		formatbarAction.QtGui.QAction("Toggle Formatbar", self)
		formatbarAction.triggered.connect(self.toggleFormatbar)

		statusbarAction.QtGui.QAction("Toggle Statusbar", self)
		statusbarAction.triggered.connect(self.toggleStatusbar

		view.addAction(toolbarAction)
		view.addAction(formatbarAction)
		view.addAction(statusbarAction)

	def initUI(self):

		self.text = QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)

		self.initToolbar()
		self.initMenubar()
		self.initFormatbar()

		# Initialize a statusbar for the window
		self.statusbar = self.statusBar()

		# x and y coordinates on the screen, width, height
		self.setGeometry(100, 100, 1030, 800)

		self.text.setTabStopWidth(32)
		self.text.cursorPositionChanged.connect(self.cursorPosition)

		self.setWindowTitle("Writer")
		self.setWindowIcon(QtGui.QIcon("icons/icon.png"))

	def new(self):

		spawn = Main(self)
		spawn.show()

	def open(self):

		# Get filename and show only .writer files
		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', ".(*.writer)")

		if self.filename:
			with open(self.filename, "rt") as file:
				self.text.setText(file.read())

	def save(self):

		# Only open dialog if there is no name yet
		if not self.filename:
			self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

		# Append extension if not there yet
		if not self.filename.endswith(".writer"):
			self.filename += ".writer"

		# We just store the contents of the
		with open(self.filename, "wt") as file:
			file.write(self.text.toHtml())

	def preview(self):

		# Open preview dialog
		preview = QtGui.QPrintPreviewDialog()

		# If a print is requested, open print dialog
		preview.paintRequested.connect(lambda p: self.text.print_(p))

		preview.exec_()

	def print(self):

		# Open printing dialog
		dialog = QtGui.QPrintDialog()

		if dialog.exec_() == QtGui.QDialog.Accepted:
			self.text.document().print_(dialog.printer())

	def bulletList(self):

		cursor = self.text.textCursor()

		# Insert bulleted list
		cursor.insertList(QtGui.QTextListFormat.ListDisc)

	def numberList(self):

		cursor = self.text.textCursor()

		# Insert list with numbers
		cursor.insertList(QtGui.QTextListFormat.ListDecimal)

	def cursorPosition(self):

		cursor = self.text.textCursor()

		# Mortals :D
		line = cursor.blockNumber() + 1
		col = cursor.columnNumber()

		self.statusbar.showMessage("Line: {} | Column: {}".format(line, col))

	def fontFamily(self, font):
		self.text.setCurrentFont(font)

	def fontSize(self, fontsize):
		self.text.setFontPointSize(int(fontsize))

	def fontColor(self):

		# Get a color from the text dialog
		color = QtGui.QColorDialog.getColor()

		# Set it as the new text color
		self.text.setTextColor(color)

	def highlight(self):

		color = QtGui.QColorDialog.getColor()

		self.text.setTextBackgroundColor(color)

	def bold(self):

		if self.text.fontWeight() == QtGui.QFont.Bold:
			self.text.setFontWeight(QtGui.QFont.Normal)
		else:
			self.text.setFontWeight(QtGui.QFont.Bold)

	def italic(self):

		self.text.setFontItalic(not self.text.fontItalic())

	def underline(self):

		self.text.setFontUnderline(not self.text.fontUnderline())

	def strike(self):
		
		# Grab the text's format
		fmt = self.text.currentCharFormat()

		# Set the fontStrikeOut property to its oposite
		fmt.setFontStrikeOut(not fmt.fontStrikeOut())

		# Set the next char format
		self.text.setCurrentCharFormat(fmt)

	def superScript(self):

		# Grab the text's format
		fmt = self.text.currentCharFormat()

		# And get the vertical alignment property
		align = fmt.verticalAlignment()

		# Toggle the state
		if align == QtGui.QTextCharFormat.AlignNormal:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

		else:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

		# Set the new format
		self.text.setCurrentCharFormat(fmt)

	def subScript(self):

		# Grab the text's format
		fmt = self.text.currentCharFormat()

		# And get the vertical alignment property
		align = fmt.verticalAlignment()

		# Toggle the state
		if align == QtGui.QTextCharFormat.AlignNormal:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

		else:

			fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

		# Set the new format
		self.text.setCurrentCharFormat(fmt)

	def alignLeft(self):
		self.text.setAlignment(Qt.AlignLeft)

	def alignCenter(self):
		self.text.setAlignment(Qt.AlignCenter)

	def alignRight(self):
		self.text.setAlignment(Qt.AlignRight)

	def alignJustify(self):
		self.text.setAlignment(Qt.AlignJustify)

	def indent(self):

		# Grab the cursor
		cursor = self.text.textCursor()

		if cursor.hasSelection():
			# Store the current line/block number
			temp = cursor.blockNumber()

			# Move to the selections last line
			cursor.setPosition(cursor.selectionEnd())
			# Calculate range of selection
			diff = cursor.blockNumber() - temp

			# Iterate over lines
			for n in range(diff + 1):

				# Move to start of each line
				cursor.movePosition(QtGui.QTextCursor.StartOfLine)

				# Insert tabbing
				cursor.insertText("\t")

				# And move back up
				cursor.movePosition(QtGui.QTextCursor.Up)

		# If there is no selection, just insert a tab
		else:

			cursor.insertText("\t")

	def dedent(self):

		cursor = self.text.textCursor()

		if cursor.hasSelection():

			temp = cursor.blockNumber()

			cursor.setPosition(cursor.selectionEnd())

			diff = cursor.blockNumber() - temp

			for n in range(diff + 1):
				self.handleDedent(cursor)
				cursor.movePosition(QtGui.QTextCursor.Up)
		else:
			self.handleDedent(cursor)

	def handleDedent(self, cursor):
		cursor.movePosition(QtGui.QTextCursor.StartOfLine)

		line = cursor.block().text()

		if line.startswith("\t"):
			cursor.deleteChar()
		else:
			for char in line[:8]:

				if char != " ":
					break

				cursor.deleteChar()

	def toggleToolbar(self):

		state =  self.toolbar.isVisible()

		self.toolbar.setVisible(not state)

	def toggleFormatbar(self):
		state = self.formatbar.isVisible()
		self.formatbar.setVisible(not state)

	def toggleStatusbar(self):
		state = self.statusbar.isVisible()
		self.statusbar.setVisible(not state)


def main():

	app = QtGui.QApplication(sys.argv)

	main = Main()
	main.show()

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()