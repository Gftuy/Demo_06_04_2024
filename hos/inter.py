import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import QDate

class PatientInfoWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Информация о пациенте")
        self.setGeometry(200, 200, 400, 250)

        layout = QVBoxLayout()

        self.setStyleSheet("background-color: #333333; color: #ffffff; font-size: 12px;")

        self.fullname_label = QLabel("ФИО:")
        self.fullname_label.setStyleSheet("color: #ffffff;")
        self.fullname_input = QLineEdit()
        layout.addWidget(self.fullname_label)
        layout.addWidget(self.fullname_input)

        self.passport_label = QLabel("Паспортные данные:")
        self.passport_label.setStyleSheet("color: #ffffff;")
        self.passport_input = QLineEdit()
        layout.addWidget(self.passport_label)
        layout.addWidget(self.passport_input)

        self.workplace_label = QLabel("Место работы:")
        self.workplace_label.setStyleSheet("color: #ffffff;")
        self.workplace_input = QLineEdit()
        layout.addWidget(self.workplace_label)
        layout.addWidget(self.workplace_input)

        self.insurance_label = QLabel("Номер страхового полиса:")
        self.insurance_label.setStyleSheet("color: #ffffff;")
        self.insurance_input = QLineEdit()
        layout.addWidget(self.insurance_label)
        layout.addWidget(self.insurance_input)

        self.insurance_company_label = QLabel("Страховая компания:")
        self.insurance_company_label.setStyleSheet("color: #ffffff;")
        self.insurance_company_input = QLineEdit()
        layout.addWidget(self.insurance_company_label)
        layout.addWidget(self.insurance_company_input)

        self.appointment_date_label = QLabel("Дата записи к врачу:")
        self.appointment_date_label.setStyleSheet("color: #ffffff;")
        self.appointment_date_input = QLineEdit()
        layout.addWidget(self.appointment_date_label)
        layout.addWidget(self.appointment_date_input)

        self.appointment_time_label = QLabel("Дата приёма:")
        self.appointment_time_label.setStyleSheet("color: #ffffff;")
        self.appointment_time_input = QLineEdit()
        layout.addWidget(self.appointment_time_label)
        layout.addWidget(self.appointment_time_input)

        self.save_button = QPushButton("Сохранить")
        self.save_button.setStyleSheet("color: #ffffff; background-color: #008CBA; border: 1px solid #000000; padding: 5px 10px;")
        self.save_button.clicked.connect(self.save_patient_info)
        layout.addWidget(self.save_button)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

    def save_patient_info(self):
        fullname = self.fullname_input.text()
        passport_data = self.passport_input.text()
        workplace = self.workplace_input.text()
        insurance_number = self.insurance_input.text()
        insurance_company = self.insurance_company_input.text()
        appointment_date = self.appointment_date_input.text()
        appointment_time = self.appointment_time_input.text()

        if not fullname or not passport_data or not workplace or not insurance_number or not insurance_company or not appointment_date or not appointment_time:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        # Здесь можно добавить код для сохранения информации в базу данных или ее обработки

        QMessageBox.information(self, "Успешно", "Информация о пациенте сохранена.")
        self.close()

class AuthorizationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.setStyleSheet("background-color: #333333; color: #ffffff; font-size: 12px;")

        self.username_label = QLabel("Логин:")
        self.username_label.setStyleSheet("color: #ffffff;")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Пароль:")
        self.password_label.setStyleSheet("color: #ffffff;")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти")
        self.login_button.setStyleSheet("color: #ffffff; background-color: #008CBA; border: 1px solid #000000; padding: 5px 10px;")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите логин и пароль.")
            return

        if username == "admin" and password == "adminpass":
            self.hide()
            self.patient_info_window = PatientInfoWindow()
            self.patient_info_window.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    authorization_window = AuthorizationWindow()
    authorization_window.show()
    sys.exit(app.exec())
