import sublime
import sublime_plugin

import os.path
import filecmp
import shutil
import time
from subprocess import Popen, PIPE
import xml.etree.ElementTree as ET


class IDACommand(sublime_plugin.WindowCommand):
    def __init__(self, *args):
        super().__init__(*args)
        self.project_info = self.window.extract_variables()
        self.platform = self.project_info.get('platform', None)
        self.project_path = self.project_info.get('project_path', None)
        self.project_name = self.project_info.get('project_base_name', None)
        self.current_object = self.project_info.get('file_path', None)
        self.settings = sublime.load_settings('IDA.sublime-settings')
        self.lp_xml_converter = self.settings.get('LP_XML_Converter')[self.platform]

    def get_lp_xml(self):
        if self.lp_xml_converter is None:
            self.window.show_input_panel('Archicad Version:', '19', self.done_lp_xml, self.change_lp_xml, self.cancel_lp_xml)
        return self.lp_xml_converter

    # ======================================================
    def done_lp_xml(self, ac_version):
        print('Got: {}'.format(ac_version))

    def change_lp_xml(self, ac_version):
        print('Changed: {}'.format(ac_version))

    def cancel_lp_xml(self):
        print('LP_XML_Converter was not given.')
    # ======================================================

    def list_lp_xml(self):
        print('>>> LP_XML_Converter: {}'.format(self.get_lp_xml()))

    def list_project_info(self):
        for k, v in self.project_info.items():
            print('{:<25}: {}'.format(k, v))

    def clean_walk(self, walk):
        new_walk = {}
        for e in walk:
            new_files = []
            for f in e[2]:
                if f[0] != '.':
                    new_name = '.'.join(f.split('.')[:-1])
                    new_files.append(new_name)
            new_walk[e[0].replace(self.project_path, '.').replace('/library_gsm', '')] = new_files
        return new_walk

    def list_gsm_objects(self):
        path_library_gsm = self.project_path + '/library_gsm'
        self.gsm_objects = list(os.walk(path_library_gsm))
        for i, v in self.clean_walk(self.gsm_objects).items():
            print('{:<10}: {}'.format(i, v))

    def import_all(self):
        ''' imports all objects in project
            transforms all source folders in .gsm files
        '''
        if os.path.isfile(self.lp_xml_converter):
            output = None
            p = Popen([self.lp_xml_converter,
                       'l2x',
                       '-img',
                       self.project_path + '/bitmaps',
                       self.project_path + '/library_gsm',
                       self.project_path + '/library_xml'], stdout=PIPE)
            output = p.communicate()[0]
            output = output.decode("utf-8")[:-1]
            output = output.replace('\r', '')
            print("Importing all objects from library.")
            print(output)

    def make_all(self):
        ''' makes all objects in project
            transforms all source folders in .gsm files
        '''
        if os.path.isfile(self.lp_xml_converter):
            output = None
            p = Popen([self.lp_xml_converter,
                       'x2l',
                       '-img',
                       self.project_path + '/bitmaps',
                       self.project_path + '/library_xml',
                       self.project_path + '/library_gsm'], stdout=PIPE)
            output = p.communicate()[0]
            output = output.decode("utf-8")[:-1]
            output = output.replace('\r', '')
            print("Making all objects from library.")
            print(output)

    def get_object(self):
        pass


class IdaNewObjectCommand(IDACommand):
    def run(self):
        sublime.error_message('IDA Message:\nFunction not yet implemented.')


class IdaCurrentMakeCommand(IDACommand):
    def run(self):
        sublime.error_message('IDA Message:\nFunction not yet implemented.')


class IdaCurrentImportCommand(IDACommand):
    def run(self):
        sublime.error_message('IDA Message:\nFunction not yet implemented.')


class IdaAllMakeCommand(IDACommand):
    def run(self):
        if self.project_name is None:
            sublime.error_message('IDA Message:\nYou are not in a Project\nPlease work inside a project.')
            return
        print(60 * '+')
        self.list_gsm_objects()
        print(60 * '=')
        print(60 * '+')
        self.make_all()
        print(60 * '+')


class IdaAllImportCommand(IDACommand):
    def run(self):
        # Check if user is in a project
        if self.project_name is None:
            sublime.error_message('IDA Message:\nYou are not in a Project\nPlease work inside a project.')
            return
        print(60 * '+')
        self.list_gsm_objects()
        print(60 * '=')
        filename = self.project_path + '/library_xml/Hello_Archicad.xml'
        with open(filename, 'r', encoding='utf-8') as obj_file:
            xml = obj_file.read()
        XML_Root = ET.fromstring(xml)
        # ET.parse(filename)
        print(XML_Root.findall('.//Script_2D')[0].items())
        print(XML_Root.findall('.//Script_2D')[0].text)
        print(60 * '+')
        self.import_all()
        print(60 * '+')


class IdaLibraryMakeCommand(IDACommand):
    def run(self):
        sublime.error_message('IDA Message:\nFunction not yet implemented.')


class IdaLibraryUnpackCommand(IDACommand):
    def run(self):
        sublime.error_message('IDA Message:\nFunction not yet implemented.')
