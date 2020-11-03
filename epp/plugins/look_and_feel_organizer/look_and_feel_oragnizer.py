from epp.model import PluginContext
from epp.model.AbstractPluginModels import AbstractPluginHandler


class LookAndFeelOrganizerHandler(AbstractPluginHandler):
    def __init__(self):
        super().__init__("Look and Feel Organizer")

    def tear_down_plugin(self, plugin_context: PluginContext):
        pass

    def setup_plugin(self, plugin_context: PluginContext):
        print("Plugin [{}], Context: [{}]".format(self.name, plugin_context))


class LookAndFeelOrganizer:
    def __init__(self):
        print("Look and feel organizer started")
