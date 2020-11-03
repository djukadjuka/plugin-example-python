import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from epp import util
from epp.view.dialogs.PluginManagerDialog import PluginManagerDialog


class AbsAction(QAction):
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


class NewFileAction(AbsAction):
    def __init__(self, parent):
        super().__init__(parent,
                         icon=util.get_icon_path(util.ICON_FLAG_NEW_FILE),
                         name="New File")


class OpenFileAction(AbsAction):
    def __init__(self, parent):
        super().__init__(parent,
                         icon=util.get_icon_path(util.ICON_FLAG_OPEN_FILE),
                         name="Open File")


class SaveFileAction(AbsAction):
    def __init__(self, parent):
        super().__init__(parent,
                         icon=util.get_icon_path(util.ICON_FLAG_SAVE_FILE),
                         name="Save")


class SaveAsFileAction(AbsAction):
    def __init__(self, parent):
        super().__init__(parent,
                         icon=util.get_icon_path(util.ICON_FLAG_SAVE_FILE_AS),
                         name="Save As...")


class CloseFileAction(AbsAction):
    def __init__(self, parent):
        super().__init__(parent,
                         icon=util.get_icon_path(util.ICON_FLAG_CLOSE_FILE),
                         name="Close File")


class ExitAction(AbsAction):
    def __init__(self, parent):
        super().__init__(parent,
                         icon=util.get_icon_path(util.ICON_FLAG_QUIT),
                         name="&Exit")
        self.setShortcut("Ctrl+Q")

    def action_performed(self):
        sys.exit(0)


class PluginManagerAction(AbsAction):
    def __init__(self, parent):
        super().__init__(parent,
                         icon=util.get_icon_path(util.ICON_FLAG_PLUGIN),
                         name="Plugin Manager")
        self.setShortcut("Ctrl+A")

    def action_performed(self):

        PluginManagerDialog(self.parent)
