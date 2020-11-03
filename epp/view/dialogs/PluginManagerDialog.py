from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QWidget, QHBoxLayout, \
    QVBoxLayout, QScrollArea, QLabel, QCheckBox

from epp import util
from epp.model.AbstractPluginModels import AbstractPluginHandler
from epp.model.PluginManager import PluginManager


class PluginManagerDialog(QDialog):
    SIZE_WIDTH = 560
    SIZE_HEIGHT = 700
    MIN_BUTTON_WIDTH = 120

    def __init__(self, parent):
        super(PluginManagerDialog, self).__init__(parent)

        self.plugin_manager = parent.plugin_manager

        self.setMinimumSize(self.SIZE_WIDTH, self.SIZE_HEIGHT)

        # -- INIT SCROLL BAR
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setLayout(QVBoxLayout())

        # -- INIT SAVE CANCEL
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.close_dialog_save)
        self.save_button.setMinimumWidth(self.MIN_BUTTON_WIDTH)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close_dialog_cancel)
        self.cancel_button.setMinimumWidth(self.MIN_BUTTON_WIDTH)

        spacer_widget = QWidget()
        spacer_widget.setSizePolicy(util.SIZE_POLICY_EXPANDING,
                                    util.SIZE_POLICY_FIXED)
        spacer_widget1 = QWidget()
        spacer_widget1.setSizePolicy(util.SIZE_POLICY_EXPANDING,
                                    util.SIZE_POLICY_FIXED)

        buttons_container = QWidget()
        buttons_container.setLayout(QHBoxLayout())
        buttons_container.layout().addWidget(spacer_widget)
        buttons_container.layout().addWidget(self.save_button)
        buttons_container.layout().addWidget(self.cancel_button)
        buttons_container.layout().addWidget(spacer_widget1)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.scroll_area)
        self.layout().addWidget(buttons_container)

        for item in self.plugin_manager.plugin_handlers.values():
            self.scroll_area.layout().addWidget(
                PluginListItem(item, self.scroll_area)
            )
        self.scroll_area.layout().addWidget(util.create_spacer())

        self.exec_()

    def close_dialog_cancel(self):
        self.close()

    def close_dialog_save(self):
        self.plugin_manager.save_plugins_to_file()
        self.plugin_manager.run_checked_plugins(self.parent())

        self.close()


class PluginListItem(QWidget):
    def __init__(self, plugin_handler: AbstractPluginHandler, parent):
        super(PluginListItem, self).__init__(parent)
        self.plugin_handler = plugin_handler

        layout = QHBoxLayout()
        self.checkbox = QCheckBox()
        self.checkbox.setText(self.plugin_handler.name)
        self.checkbox.setChecked(self.plugin_handler.is_plugin_enabled())
        self.checkbox.clicked.connect(self.checked_checkbox)
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    def checked_checkbox(self):
        self.plugin_handler.set_plugin_enabled(self.checkbox.isChecked())

