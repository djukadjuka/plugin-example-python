from epp.model import PluginContext
from epp.model.AbstractPluginModels import AbstractPluginHandler


class EnglishToPolishTranslatorPluginHandler(AbstractPluginHandler):
    def tear_down_plugin(self, plugin_context: PluginContext):
        pass

    def __init__(self):
        super().__init__("English To Polish Translator")

    def setup_plugin(self, plugin_context: PluginContext):
        print("Plugin [{}], Context: [{}]".format(self.name, plugin_context))


class EnglishToPolishTranslatorPlugin:
    def __init__(self):
        print("English to Polish translator plugin started")

