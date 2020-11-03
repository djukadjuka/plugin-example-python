from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMessageBox


class AbstractGreetingAction(QAction):
    def __init__(self, parent, icon=None, name="Action"):
        if not icon:
            icon = QIcon()
        elif isinstance(icon, str):
            icon = QIcon(icon)

        super().__init__(icon, name, parent)
        self.name = name
        self.parent = parent

        self.triggered.connect(self.action_performed)

    # Re-implement this
    # Left print so that it is ont necessary to re-implement
    def action_performed(self):
        print(self.name)


def run_dialog(parent, text):
    QMessageBox.information(parent,
                            "Message Box",
                            text)


class FrenchGreeting(AbstractGreetingAction):
    def __init__(self, parent, icon_path):
        super().__init__(parent,
                         icon=icon_path,
                         name="French Greeting")

    def action_performed(self):
        run_dialog(self.parent, "Bonjour!")


class EnglishGreeting(AbstractGreetingAction):
    def __init__(self, parent, icon_path):
        super().__init__(parent,
                         icon=icon_path,
                         name="English Greeting")

    def action_performed(self):
        run_dialog(self.parent, "Hello!")


class GermanGreeting(AbstractGreetingAction):
    def __init__(self, parent, icon_path):
        super().__init__(parent,
                         icon=icon_path,
                         name="German Greeting")

    def action_performed(self):
        run_dialog(self.parent, "Hallo!")


class PolishGreeting(AbstractGreetingAction):
    def __init__(self, parent, icon_path):
        super().__init__(parent,
                         icon=icon_path,
                         name="Polish Greeting")

    def action_performed(self):
        run_dialog(self.parent, "Cześć!")

