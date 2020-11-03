from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QMenu, QVBoxLayout, QToolBar, \
    QSizePolicy

import epp
from epp import util
from epp.controller.actions import *
from epp.model.PluginContext import PluginContext
from epp.model.PluginManager import PluginManager


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        size = (800, 600)

        # -- INITIALIZE MODEL ITEMS
        self.plugin_manager = PluginManager()

        # -- INITIALIZE ACTIONS
        self.new_file_action = NewFileAction(self)
        self.open_file_action = OpenFileAction(self)
        self.save_file_action = SaveFileAction(self)
        self.save_as_file_action = SaveAsFileAction(self)
        self.close_file_action = CloseFileAction(self)
        self.exit_action = ExitAction(self)
        self.plugin_manager_action = PluginManagerAction(self)

        # -- INITIALIZE MENU BAR
        menu_bar = self.menuBar()

        # - file menu
        self.file_menu = menu_bar.addMenu("&File")
        self.file_menu.addAction(self.new_file_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.open_file_action)
        self.file_menu.addAction(self.save_file_action)
        self.file_menu.addAction(self.save_as_file_action)
        self.file_menu.addAction(self.close_file_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)

        # - options menu
        self.options_menu = menu_bar.addMenu("&Options")
        self.options_menu.addAction(self.plugin_manager_action)

        # -- INITIALIZE LEFT TOOLBAR
        self.toolbar_left = QToolBar()
        self.toolbar_left.addAction(self.new_file_action)
        self.toolbar_left.addAction(self.new_file_action)
        self.toolbar_left.addSeparator()
        self.toolbar_left.addAction(self.open_file_action)
        self.toolbar_left.addAction(self.save_file_action)
        self.toolbar_left.addAction(self.save_as_file_action)
        self.toolbar_left.addAction(self.close_file_action)
        self.toolbar_left.addSeparator()
        self.toolbar_left.addAction(self.exit_action)

        # -- INITIALIZE RIGHT TOOLBAR
        self.toolbar_right = QToolBar()
        spacer = QWidget()
        spacer.setSizePolicy(
            util.SIZE_POLICY_EXPANDING,
            util.SIZE_POLICY_EXPANDING)
        self.toolbar_right.addWidget(spacer)
        self.toolbar_right.addAction(self.plugin_manager_action)

        self.addToolBar(self.toolbar_left)
        self.addToolBar(self.toolbar_right)

        # -- INITIALIZE CENTRAL WIDGET
        central_widget = QWidget()
        central_widget.setLayout(QVBoxLayout())
        central_widget.setMaximumSize(*size)

        self.setCentralWidget(central_widget)

        self.setMinimumSize(*size)

        self.plugin_manager.run_checked_plugins(self)

        self.setVisible(True)
