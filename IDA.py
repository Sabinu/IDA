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
        self.project_info = self.window.extract_variables()
        self.platform = self.project_info.get('platform', None)
        self.project_path = self.project_info.get('project_path', None)
        self.project_name = self.project_info.get('project_base_name', None)
        self.current_object = self.project_info.get('file_path', None)

    def get_lp_xml(self):
        self.lp_xml_converter = self.window.project_data()["LP_XML_Converter"]
        if self.lp_xml_converter is None:
            self.window.show_input_panel('Archicad Version:', '19', self.done_lp_xml, self.change_lp_xml, self.cancel_lp_xml)
        return self.lp_xml_converter

    def done_lp_xml(self, ac_version):
        print('Got: {}'.format(ac_version))

    def change_lp_xml(self, ac_version):
        print('Changed: {}'.format(ac_version))

    def cancel_lp_xml(self):
        print('LP_XML_Converter was not given.')

    def list_lp_xml(self):
        print(self.window.project_data())
        print('LP_XML_Converter: {}'.format(self.get_lp_xml()))

    def list_project_info(self):
        for k, v in self.project_info.items():
            print('{:<25}: {}'.format(k, v))

    def list_gsm_objects(self):
        path_library_gsm = self.project_path + '/library_gsm'
        # self.gsm_objects = os.listdir(path_library_gsm)
        self.gsm_objects = os.walk(path_library_gsm)
        for i, v in enumerate(self.gsm_objects):
            print('{:>3}: {}'.format(i, v))

    def get_object(self):
        pass


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
        self.list_lp_xml()
        # self.list_project_info()
        self.list_gsm_objects()
        print(60 * '=')
        print(self.platform)
        print(self.project_name)
        print(self.project_path)
        print(self.current_object)
        print(60 * '=')
        # call(['mkdir', '/Users/sabinu/blipy'])
        # call(["pwd"])
        # call(["ls", "-l"])
        # call('dir', 'c:\\')
        # print(60 * '=')


class IdaLibraryMakeCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')


class IdaLibraryUnpackCommand(IDACommand):
    def run(self):
        sublime.error_message('Function not yet implemented.')
