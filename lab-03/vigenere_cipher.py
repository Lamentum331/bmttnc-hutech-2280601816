# import sys

# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from ui.viginere import Ui_MainWindow  # Đảm bảo bạn có tệp giao diện tương ứng
# import requests


# class MyApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
#         self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

#     def call_api_encrypt(self):
#         url = "http://127.0.0.1:5000/api/vigenere/encrypt"
#         payload = {
#             "plain_text": self.ui.plain_txt.toPlainText(),
#             "key": self.ui.key_txt.toPlainText()
#         }

#         try:
#             response = requests.post(url, json=payload)
#             if response.status_code == 200:
#                 data = response.json()
#                 self.ui.cipher_txt.setPlainText(data["encrypted_message"])

#                 msg = QMessageBox()
#                 msg.setIcon(QMessageBox.Information)
#                 msg.setText("Encrypted Successfully")
#                 msg.exec_()
#             else:
#                 print("Error while calling API")
#         except requests.exceptions.RequestException as e:
#             print("Error: %s" % e.message)

#     def call_api_decrypt(self):
#         url = "http://127.0.0.1:5000/api/vigenere/decrypt"
#         payload = {
#             "cipher_text": self.ui.cipher_txt.toPlainText(),
#             "key": self.ui.key_txt.toPlainText()
#         }

#         try:
#             response = requests.post(url, json=payload)
#             if response.status_code == 200:
#                 data = response.json()
#                 self.ui.plain_txt.setPlainText(data["decrypted_message"])

#                 msg = QMessageBox()
#                 msg.setIcon(QMessageBox.Information)
#                 msg.setText("Decrypted Successfully")
#                 msg.exec_()
#             else:
#                 print("Error while calling API")
#         except requests.exceptions.RequestException as e:
#             print("Error: %s" % e.message)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow  # Đảm bảo tệp giao diện tồn tại
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": self.ui.plain_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.cipher_txt.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Failed to encrypt")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": self.ui.cipher_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plain_txt.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Failed to decrypt")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())