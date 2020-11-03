import os

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QSizePolicy, QWidget

_ASSETS_DIRECTORY = os.path.join(os.getcwd(), "assets")
_ICONS_DIRECTORY = os.path.join(_ASSETS_DIRECTORY, "icons")
PLUGINS_DIRECTORY = os.path.join(os.getcwd(),
                                  "epp",
                                  "plugins")


ICON_FLAG_NEW_FILE = "new_file"
ICON_FLAG_OPEN_FILE = "open_file"
ICON_FLAG_SAVE_FILE = "save_file"
ICON_FLAG_SAVE_FILE_AS = "save_file_as"
ICON_FLAG_CLOSE_FILE = "close_file"
ICON_FLAG_PLUGIN = "plugin"

ICON_FLAG_QUIT = "quit"

PLUGIN_RESOURCE_FILE_SPLIT_CHAR = "="

SIZE_POLICY_EXPANDING = QSizePolicy.Expanding
SIZE_POLICY_FIXED = QSizePolicy.Fixed
SCROLL_BAR_POLICY_ALWAYS_ON = Qt.ScrollBarAlwaysOn


def get_icon_path(icon_flag):
    name = ""

    if icon_flag == ICON_FLAG_NEW_FILE:
        name = "icons8-new-file-32"
    if icon_flag == ICON_FLAG_OPEN_FILE:
        name = "icons8-live-folder-32"
    if icon_flag == ICON_FLAG_SAVE_FILE:
        name = "icons8-save-32"
    if icon_flag == ICON_FLAG_SAVE_FILE_AS:
        name = "icons8-save-as-32"
    if icon_flag == ICON_FLAG_CLOSE_FILE:
        name = "icons8-close-window-32"
    if icon_flag == ICON_FLAG_QUIT:
        name = "icons8-shutdown-32"
    if icon_flag == ICON_FLAG_PLUGIN:
        name = "icons8-plugin-32"

    return os.path.join(_ICONS_DIRECTORY, name + ".png")


def create_spacer():
    w = QWidget()
    w.setSizePolicy(SIZE_POLICY_EXPANDING, SIZE_POLICY_EXPANDING)
    return w
