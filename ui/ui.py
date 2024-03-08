import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QTextEdit, QScrollArea, QStackedWidget, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class SyllabusGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SyllaBot')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setStyleSheet("background-color: #E9ECEF;")

        # Create stacked widget to hold different widgets
        self.stacked_widget = QStackedWidget()

        # Create welcome label widget
        welcome_text = QLabel('Welcome to the SyllaBot!')
        welcome_text.setAlignment(Qt.AlignCenter)
        welcome_text.setStyleSheet("font-size: 36pt; color: #868E96; font-weight: bold;")

        welcome_layout = QHBoxLayout()
        welcome_layout.setAlignment(Qt.AlignCenter)

        # Add image to the left of the text
        logo_label = QLabel(self)
        pixmap = QPixmap("logo.png")
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        welcome_layout.addWidget(logo_label)
        welcome_layout.addWidget(welcome_text)

        welcome_widget = QWidget()
        welcome_widget.setLayout(welcome_layout)

        # Create load PDF button only for the welcome widget
        self.btn_load_pdf = QPushButton('Load PDF', self)
        self.btn_load_pdf.setStyleSheet(
        # initial background-color: #343A40;
        # hover initial background-color: #495057;
            """
            QPushButton {
                background-color: #E9ECEF;
                color: #ADB5BD;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #ADB5BD;
                color: white;
            }
            """
        )
        self.btn_load_pdf.setCursor(Qt.PointingHandCursor)
        self.btn_load_pdf.clicked.connect(self.loadPDF)

        welcome_layout.addWidget(self.btn_load_pdf)

        # Scroll area for messages
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none;")

        # Widget to contain messages
        self.message_container = QWidget()
        self.message_layout = QVBoxLayout(self.message_container)

        self.scroll_area.setWidget(self.message_container)

        # Add widgets to stacked widget
        self.stacked_widget.addWidget(welcome_widget)
        self.stacked_widget.addWidget(self.scroll_area)

        # Text input area
        self.input_box = QTextEdit()
        self.input_box.setMaximumHeight(80)
        self.input_box.setStyleSheet("border-radius: 8px; background-color: #FFFFFF; border: 2px solid #ADB5BD;")

        # Create generate button
        btn_generate = QPushButton('Generate', self)
        btn_generate.setStyleSheet(
            """
            QPushButton {
                background-color: #087F5B;
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #027955;
            }
            """
        )
        btn_generate.setCursor(Qt.PointingHandCursor)
        btn_generate.clicked.connect(self.change_widget)
        btn_generate.clicked.connect(self.sendMessage)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.input_box)
        layout.addWidget(btn_generate)

        self.setLayout(layout)

    def sendMessage(self):
        message_text = self.input_box.toHtml()

        if message_text:
            self.addMessage("You", message_text)
            self.addMessage("Model", message_text)
            self.input_box.clear()

    def addMessage(self, sender, message):
        message_label = QLabel(f"<b>{sender}:</b> {message}")
        message_label.setWordWrap(True)

        if sender == "You":
            message_label.setStyleSheet("background-color: #c3e6cb; padding: 8px; border-radius: 8px;")
        else:
            message_label.setStyleSheet("background-color: #d4edda; padding: 8px; border-radius: 8px;")

        self.message_layout.addWidget(message_label)
        self.message_layout.setAlignment(Qt.AlignTop)

    def change_widget(self):
        # Change the displayed widget when the button is clicked
        current_index = self.stacked_widget.currentIndex()
        new_index = (current_index + 1) % self.stacked_widget.count()
        if new_index == 0:
            new_index = 1
        else :
            pass
        self.stacked_widget.setCurrentIndex(new_index)

    def loadPDF(self):
        # Implement PDF loading functionality here
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load PDF", "", "PDF Files (*.pdf);;All Files (*)",
                                                  options=options)
        if fileName:
            # Change button color and disable
            self.btn_load_pdf.setStyleSheet(
                """
                QPushButton {
                    background-color: #087F5B;
                    color: white;
                    padding: 12px 24px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                }
                """
            )
            self.btn_load_pdf.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SyllabusGenerator()
    window.show()
    sys.exit(app.exec_())
