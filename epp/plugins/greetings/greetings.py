import os

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolBar, QLabel

from epp.model.PluginContext import PluginContext
from epp.model.AbstractPluginModels import AbstractPluginHandler
from epp.plugins.greetings.greetings_actions import EnglishGreeting, PolishGreeting, GermanGreeting, FrenchGreeting

icon_name_english = "icons8-united-kingdom-32.png"
icon_name_german = "icons8-germany-32.png"
icon_name_polish = "icons8-poland-32.png"
icon_name_french = "icons8-france-32.png"


class GreetingsPluginHandler(AbstractPluginHandler):
    def __init__(self):
        super().__init__("Greetings Plugin")

    def setup_plugin(self, plugin_context: PluginContext):
        self.plugin = GreetingsPlugin(plugin_context.main_toolbar_left,
                                      plugin_context.plugins_directory_path)
        plugin_context.add_toolbar(self.plugin)

    def tear_down_plugin(self, plugin_context: PluginContext):
        if self.plugin:
            plugin_context.remove_toolbar(self.plugin)
            self.plugin = None


class GreetingsPlugin(QToolBar):
    def __init__(self, parent, plugins_directory):
        super(GreetingsPlugin, self).__init__(parent)

        lab = QLabel("Select a greeting: ")
        self.addWidget(lab)

        self.addAction(
            EnglishGreeting(
                self,
                os.path.join(plugins_directory,
                             "greetings",
                             icon_name_english)))
        self.addAction(
            FrenchGreeting(
                self,
                os.path.join(plugins_directory,
                             "greetings",
                             icon_name_french)))
        self.addAction(
            GermanGreeting(
                self,
                os.path.join(plugins_directory,
                             "greetings",
                             icon_name_german)))
        self.addAction(
            PolishGreeting(
                self,
                os.path.join(plugins_directory,
                             "greetings",
                             icon_name_polish)))
