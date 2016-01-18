import sublime
import sublime_plugin


class IDACommand(sublime_plugin.WindowCommand):
    def get_project_info(self):
        project_info = self.window.extract_variables()
        self.platform = project_info['platform']
        self.project_name = project_info['project_name']
        self.project_path = project_info['project_path']


class IdanewobjectCommand(IDACommand):
    def run(self):
        print('Not implemented')


class IdacurrentmakeCommand(IDACommand):
    def run(self):
        print('Not implemented')


class IdacurrentimportCommand(IDACommand):
    def run(self):
        print('Not implemented')


class IdaallmakeCommand(IDACommand):
    def run(self):
        print('Not implemented')


class IdaallimportCommand(IDACommand):
    def run(self):
        self.get_project_info()
        print(60 * '=')
        print(self.platform)
        print(60 * '=')


class IdalibrarymakeCommand(IDACommand):
    def run(self):
        print('Not implemented')


class IdalibraryunpackCommand(IDACommand):
    def run(self):
        print('Not implemented')
