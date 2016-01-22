import sublime
import sublime_plugin

import os.path
import filecmp
import shutil
import time

from subprocess import call


class IDACommand(sublime_plugin.WindowCommand):
    def __init__(self, *args):
        super().__init__(*args)
        project_info = self.window.extract_variables()
        self.platform = project_info.get('platform', None)
        self.project_path = project_info.get('project_path', None)
        self.project_name = project_info.get('project_base_name', None)
        self.location = project_info.get('file_path', None)
        # for k, v in project_info.items():
            # print('{:<25}: {}'.format(k, v))
        

class IdaNewObjectCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaCurrentMakeCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaCurrentImportCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaAllMakeCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaAllImportCommand(IDACommand):
    def run(self):
        if self.project_name is None:
            sublime.error_message('You are not in a Project\nPlease work inside a project.')
            return
        print(60 * '=')
        print(self.platform)
        print(self.project_name)
        print(self.project_path)
        print(self.location)
        print(60 * '=')
        # call(['mkdir', '/Users/sabinu/blipy'])
        # call(["pwd"])
        # call(["ls", "-l"])
        # call('dir', 'c:\\')
        print(60 * '=')


class IdaLibraryMakeCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaLibraryUnpackCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')
