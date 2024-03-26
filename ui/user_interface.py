import sys

from PyQt5.QtGui import QPixmap, QFont, QFontDatabase, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QPushButton, QRadioButton, QTextEdit, QScrollArea, QStackedWidget, QFileDialog, QStackedLayout, QDialog, QLineEdit
from PyQt5.QtCore import Qt, QSize

class URLInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter URL")
        self.setGeometry(400, 400, 400, 200)
        self.layout = QVBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("height: 36px; border: none;")
        self.url_input.setPlaceholderText("Enter the URL here...")
        self.layout.addWidget(self.url_input)
        self.ok_button = QPushButton("OK")
        self.ok_button.setCursor(Qt.PointingHandCursor)
        self.ok_button.setStyleSheet("color: #FFFFFF; background-color: #087F5B; border-radius: 6px; padding: 12px;")
        self.ok_button.setStyleSheet(
            """
            QPushButton {
                background-color: #087F5B;
                color: white;
                padding: 12px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #007753;
            }
            """
        )
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

class SyllaBot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('SyllaBot')
        self.setWindowIcon(QIcon('images/icon.ico'))

        ################################################################################
        # TODO SETTING FONT

        font = QFont("Monomaniac One", 20)
        QFontDatabase.addApplicationFont("/fonts/MonomaniacOne-Regular.ttf")

        ################################################################################
        # TODO DEFINING FUNCTIONS

        def create_new_chat():
            chat_button = QRadioButton("Chat XXX")
            chat_button.setFixedHeight(48)
            chat_button.setCursor(Qt.PointingHandCursor)
            chat_button.setStyleSheet(
                """
                QRadioButton {
                    background-color: #F1F3F5;
                    color: black;
                    padding: 12px 24px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    text-align: center;
                }
                QRadioButton::indicator {
                    width: 0;
                    height: 0;
                }
                QRadioButton:hover {
                    background-color: #495057;
                    color: #FFFFFF;
                }
                QRadioButton:checked {
                    background-color: #212529;
                    color: white;
                }
                """
            )
            current_chats.addWidget(chat_button)

        def delete_selected_chat():
            for i in range(current_chats.count()):
                if current_chats.itemAt(i).widget().isChecked():
                    current_chats.itemAt(i).widget().deleteLater()
                    break

        def change_widget():
            widget_changer.setCurrentIndex(1)

        def new_message(sender, message):
            message_content = QLabel(f"<b>{sender}:</b> {message}")
            message_content.setWordWrap(True)

            if sender == "You":
                message_content.setStyleSheet("background-color: #c3e6cb; padding: 8px; border-radius: 8px;")
            else:
                message_content.setStyleSheet("background-color: #d4edda; padding: 8px; border-radius: 8px;")

            chat_layout.addWidget(message_content)
            chat_layout.setAlignment(Qt.AlignTop)

        def send_message():
            message_text = prompt_box.toHtml()
            if message_text.strip() != "":
                new_message("You", message_text)
                new_message("Model", bot_response(message_text))
                prompt_box.clear()

        def attach_file():
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getOpenFileName(self, "Attach the File", "", "PDF Files (*.pdf);;All Files (*)",
                                                      options=options)
            if fileName:
                print("The file has been attached to the SyllaBot!")
                print("The file name is " + fileName)

        def open_url_dialog():
            dialog = URLInputDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                url = dialog.url_input.text()
                # Do something with the retrieved URL
                print("URL entered:", url)

        def bot_response(user_input):
            # Chatbot logic will be implemented here
            # For demo;
            return user_input

        ################################################################################
        # TODO MAIN FLOW OF THE PROGRAM

        container = QHBoxLayout(self)

        scrollbar_container = QFrame()
        main_page_container = QFrame()

        scrollbar_container.setStyleSheet("background-color: white; border-radius: 8px;")
        main_page_container.setStyleSheet("background-color: #E9ECEF; border-radius: 8px;")

        ################################################################################
        # TODO SCROLLBAR

        scrollbar_layout = QVBoxLayout(scrollbar_container)
        current_chats = QVBoxLayout()
        scrollbar_buttons = QHBoxLayout()

        scrollbar_layout.addLayout(current_chats)
        scrollbar_layout.addLayout(scrollbar_buttons)

        new_chat_button = QPushButton("New Chat")
        new_chat_button.setCursor(Qt.PointingHandCursor)
        new_chat_button.setFixedHeight(48)
        new_chat_button.setStyleSheet(
            """
            QPushButton {
                background-color: #F1F3F5;
                color: black;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #212529;
                color: #FFFFFF;
            }
            """
        )

        delete_chat_button = QPushButton("Delete Chat")
        delete_chat_button.setCursor(Qt.PointingHandCursor)
        delete_chat_button.setFixedHeight(48)
        delete_chat_button.setStyleSheet(
            """
            QPushButton {
                background-color: #ffE3E3;
                color: #F03E3E;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #C92A2A;
                color: #FFFFFF;
            }
            """
        )

        new_chat_button.clicked.connect(create_new_chat)
        delete_chat_button.clicked.connect(delete_selected_chat)

        scrollbar_buttons.addWidget(new_chat_button)
        scrollbar_buttons.addWidget(delete_chat_button)
        scrollbar_buttons.setAlignment(Qt.AlignBottom)

        ################################################################################
        # TODO TEMPORARY AREA

        temp_area_container = QFrame()

        widget_changer = QStackedLayout(temp_area_container)

        ################################################################################
        # TODO WELCOME PAGE

        # introduction_layout = QHBoxLayout(temp_area_container)
        introduction_container = QWidget()
        introduction_layout = QHBoxLayout(introduction_container)

        logo = QLabel(self)
        pixmap = QPixmap("images/logo.png")
        logo.setPixmap(pixmap)

        introduction_text = QLabel(
            "Welcome to the<br><span style='font-weight: bold; font-size: 48pt; color: #087F5B;'>SyllaBot</span>")
        introduction_text.setFont(font)
        introduction_text.setStyleSheet("font-size: 22pt; color: #868E96; font-weight: bold;")
        introduction_text.setTextFormat(Qt.RichText)

        introduction_layout.addWidget(logo)
        introduction_layout.addWidget(introduction_text)
        introduction_layout.setAlignment(Qt.AlignCenter)

        widget_changer.addWidget(introduction_container)

        ################################################################################
        # TODO CHAT SCROLL

        chat_scroll = QScrollArea()
        chat_scroll.setWidgetResizable(True)
        chat_scroll.setStyleSheet("border: none;")

        chat_container = QWidget()
        chat_layout = QVBoxLayout(chat_container)

        chat_scroll.setWidget(chat_container)

        widget_changer.addWidget(chat_scroll)

        ################################################################################
        # TODO INPUT AREA

        input_area_container = QFrame()

        # input_area = QHBoxLayout()
        input_area = QHBoxLayout(input_area_container)

        prompt_box = QTextEdit()
        prompt_box.setMaximumHeight(48)
        prompt_box.setMaximumWidth(1200)
        prompt_box.setStyleSheet("border-radius: 8px; background-color: #FFFFFF;")

        send_button = QPushButton(self)
        send_button.setMaximumHeight(48)
        send_icon = QIcon("images/arrow.png")
        send_button.setIcon(send_icon)
        send_button.setCursor(Qt.PointingHandCursor)
        send_button.clicked.connect(change_widget)
        send_button.clicked.connect(send_message)
        send_button.setStyleSheet(
            """
            QPushButton {
                background-color: #087F5B;
                color: #000000;
                padding-top: 15px;
                padding-bottom: 15px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #007753;
                color: #FFFFFF;
            }
            """
        )

        link_button = QPushButton(self)
        link_button.setMaximumHeight(48)
        link_icon = QIcon("images/chain.png")
        link_button.setIcon(link_icon)
        link_button.setCursor(Qt.PointingHandCursor)
        link_button.clicked.connect(open_url_dialog)
        link_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FFFFFF;
                color: #000000;
                padding-top: 15px;
                padding-bottom: 15px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #E6FCF5;
                color: #FFFFFF;
            }
            """
        )

        attach_button = QPushButton(self)
        attach_button.setMaximumHeight(48)
        attach_icon = QIcon("images/attach.png")
        attach_button.setIcon(attach_icon)
        attach_button.setCursor(Qt.PointingHandCursor)
        attach_button.clicked.connect(attach_file)
        attach_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FFFFFF;
                color: #000000;
                padding-top: 15px;
                padding-bottom: 15px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #E6FCF5;
                color: #FFFFFF;
            }
            """
        )

        input_area.addWidget(prompt_box)
        input_area.addWidget(send_button)
        input_area.addWidget(link_button)
        input_area.addWidget(attach_button)
        input_area.setAlignment(Qt.AlignBottom)

        ################################################################################
        # TODO MAIN PAGE

        main_page_layout = QVBoxLayout(main_page_container)
        # main_page_layout.addLayout(introduction_layout)
        main_page_layout.addWidget(temp_area_container, 7)
        # main_page_layout.addLayout(input_area)
        main_page_layout.addWidget(input_area_container, 1)

        container.addWidget(scrollbar_container, 1)
        container.addWidget(main_page_container, 5)

        self.setLayout(container)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('SyllaBot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chatbot = SyllaBot()
    sys.exit(app.exec_())
