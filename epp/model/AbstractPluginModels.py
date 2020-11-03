from epp.model import PluginContext


class AbstractPluginHandler:
    def __init__(self, name):
        if not name:
            name = "Abstract Plugin"

        self.name = name
        self._checked = False
        self.plugin = None

    def setup_plugin(self, plugin_context: PluginContext):
        raise NotImplementedError("Abstract plugin needs to implement "
                                  "run_plugin method.")

    def tear_down_plugin(self, plugin_context: PluginContext):
        raise NotImplementedError("Abstract plugin needs to implement "
                                  "tear_down_plugin method.")

    def set_plugin_enabled(self, enabled):
        self._checked = enabled

    def is_plugin_enabled(self):
        return self._checked

    def __str__(self):
        return "{} - {}".format(self.name, self._checked)
