from epp import util


class PluginContext:
    def __init__(self, main_window):
        self._mw = main_window
        # -- Get main toolbars
        self.main_toolbar_left = main_window.toolbar_left
        self.main_toolbar_right = main_window.toolbar_right

        # -- Get main menu bar and main menus
        self.main_menu_bar = main_window.menuBar()
        self.file_menu = main_window.file_menu
        self.options_menu = main_window.options_menu

        self.plugins_directory_path = util.PLUGINS_DIRECTORY

    def add_toolbar(self, toolbar):
        self._mw.insertToolBar(
            self.main_toolbar_right,
            toolbar)

    def remove_toolbar(self, toolbar):
        self._mw.removeToolBar(toolbar)
