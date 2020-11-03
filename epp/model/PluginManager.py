import importlib
import pkgutil
import epp.plugins
import inspect

from epp import util
from epp.model.AbstractPluginModels import AbstractPluginHandler
from epp.model.PluginContext import PluginContext


class PluginManager:
    def __init__(self):
        self.plugin_file_path = r"D:\WORK\DOWNLOADS\ExamplePluginProje" \
                                r"ct\assets\plugins\plugin_resource.txt"

        self.plugin_handlers = {}

        self.load_plugin_handler_classes()
        self.load_and_update_plugins_in_file()

    def run_checked_plugins(self, main_window):
        plugin_context = PluginContext(main_window)
        for plugin in self.plugin_handlers.values():
            if plugin.is_plugin_enabled():
                plugin.setup_plugin(plugin_context)
            else:
                plugin.tear_down_plugin(plugin_context)

    def load_and_update_plugins_in_file(self):
        scanned_file = self.load_plugin_file_contents()
        self.merge_plugins_and_file_plugins(scanned_file)
        self.save_plugins_to_file()

    def load_plugin_file_contents(self):
        with open(self.plugin_file_path, mode="r") as f:
            file_contents = f.readlines()

            # -- Contains package:bool
            scanned_file_contents = {}

            for line in file_contents:
                # -- Split by the splitter character
                name, checked = line.split(util.PLUGIN_RESOURCE_FILE_SPLIT_CHAR)
                # -- First strip the '\n' and check if it's true
                scanned_file_contents[name] = checked.strip() == 'True'

        return scanned_file_contents

    def merge_plugins_and_file_plugins(self, scanned_file: dict):
        # -- plugin handlers contain package:object
        for dict_item in self.plugin_handlers.items():
            if dict_item[0] not in scanned_file:
                # -- If key from plugin module is not in file,
                #    uncheck it by default
                scanned_file[dict_item[0]] = False
            else:
                # -- Else add the correct flag from the file
                dict_item[1].set_plugin_enabled(
                    scanned_file[dict_item[0]]
                )

    def save_plugins_to_file(self):
        s = ""
        for item in self.plugin_handlers.items():
            s += item[0] + \
                 util.PLUGIN_RESOURCE_FILE_SPLIT_CHAR + \
                 str(item[1].is_plugin_enabled()) + \
                 "\n"

        # -- Write scanned plugins to file
        with open(self.plugin_file_path, mode="w") as f:
            f.write(s)

    @staticmethod
    def _is_valid_class(cls):
        return inspect.isclass(cls) \
               and issubclass(cls, AbstractPluginHandler) \
               and cls is not AbstractPluginHandler

    def _find_handler_class(self, name):
        # -- Import using the name
        imported_module = importlib.import_module(name)
        # -- Get members from the imported module
        imported_module_members = inspect.getmembers(imported_module)
        for tup in imported_module_members:
            imported_class = tup[1]
            # -- Needs to be class, needs to be subclass of
            # AbstractPluginHandler
            # and musn't be AbstractPluginHandler
            if self._is_valid_class(imported_class):
                return imported_class()

        # -- If all above passes with no return, use the name as a path for
        # recursive search
        found_handler_classes = []
        if imported_module_members[7][0] != "__path__":
            return None
        path = imported_module_members[7][1]
        for file_finder, name, is_package in \
                pkgutil.iter_modules(path, name + "."):
            result = self._find_handler_class(name)
            if result is not None:
                found_handler_classes.append(result)

        if not len(found_handler_classes):
            return None
        return found_handler_classes

    def load_plugin_handler_classes(self):
        # -- Find all plugin packages
        found_plugins = []
        for file_finder, name, is_package in pkgutil.iter_modules(
                epp.plugins.__path__,
                epp.plugins.__name__ + "."):
            handlers = self._find_handler_class(name)
            if len(handlers):
                found_plugins.extend(handlers)

        for plugin in found_plugins:
            self.plugin_handlers[plugin.__module__] = plugin
