import sublime
import sublime_plugin


class IDACommand(sublime_plugin.WindowCommand):
    def get_project_info(self):
        project_info = self.window.extract_variables()
        self.platform = project_info.get('platform', None)
        self.project_path = project_info.get('project_path', None)
        self.project_name = project_info.get('project_base_name', None)
        self.location = project_info.get('file_path', None)
        # for k, v in project_info.items():
            # print('{:<25}: {}'.format(k, v))


class IdanewobjectCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdacurrentmakeCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdacurrentimportCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaallmakeCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaallimportCommand(IDACommand):
    def run(self):
        self.get_project_info()
        if self.project_name is None:
            sublime.error_message('\nYou are not in a Project\nPlease work inside a project.')
            return
        print(60 * '=')
        print(self.platform)
        print(self.project_name)
        print(self.project_path)
        print(self.location)
        print(60 * '=')


class IdalibrarymakeCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdalibraryunpackCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')
