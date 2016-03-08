import sublime
import sublime_plugin

import os.path
import filecmp
import shutil
import time
from subprocess import Popen, PIPE
import xml.etree.ElementTree as ET

scripts = {"Script_1D": "0 Master Script",
           "Script_2D": "1 2D Script",
           "Script_3D": "2 3D Script",
           "Script_VL": "3 Parameter Script",
           "Script_UI": "4 Interface Script",
           "Script_PR": "5 Properties Script",
           "Script_FWM": "6 Forward Migration",
           "Script_BWM": "7 Backward Migration"}


def clip_path(path, folder):
    ''' clips path sequence at folder
        returns path from folder(except) to the end, except file
    '''
    path = path.split(os.sep)
    clip = path.index(folder)
    output = os.sep.join(path[clip+1:])
    return output


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
        self.objects = None  # TODO try to ingest objects at __init__
        self.initiate_folders()

    def initiate_folders(self):
        ''' initiates paths of needed folders. '''
        if self.project_name is None:
            return
        self.folder_backup = self.project_path + os.sep + self.project_name + '.backup'
        self.folder_images = self.project_path + os.sep + 'images'
        self.folder_code = self.project_path + os.sep + 'CODE'
        self.folder_library = self.project_path + os.sep + self.project_name + '.library'
        self.folder_xml = self.project_path + os.sep + self.project_name + '.xml'

    def check_project(self, output=True):
        ''' Check if user is in a project.
            returns: True or False.
        '''
        if self.project_name is None:
            if output:
                sublime.error_message('IDA Message:\nYou are not in a Project\nPlease work inside a project.')
            return False
        else:
            return True

    def get_lp_xml(self):
        ''' TODO
            returns the path/adress of the LP_XML Converter.
        '''
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
        ''' INSPECTION method
            prints the path of the LP_XML Converter to the console.
        '''
        print('>>> LP_XML_Converter: {}'.format(self.get_lp_xml()))

    def list_project_info(self):
        ''' INSPECTION Method
            prints the project info to the console.
        '''
        print(60 * '=')
        print('PROJECT INFO')
        print(60 * '=')
        for k, v in self.project_info.items():
            print('{:<25}: {}'.format(k, v))

# ========= BLEND WITH LIST_OBJECTS ==================================
    def get_tree(self, walk=None, folder=None):
        ''' TODO
            must return a clean list of objects(name & path)
            regardless of the source of the walk.
            which could only be from: `backup`, `library`, `code` or `xml` folders
        '''
        folder = folder.split(os.sep)[-1]
        tree = []
        for i in walk:
            for f in i[2]:
                if f[0] != '.':
                    tree.append((clip_path(i[0], folder), f))
        # if self.tree is None:  # TODO make tree available in JSON file, as reference
        #     self.tree = tree
        return tree

    def list_objects(self, folder=None, output=False):
        ''' TODO
            must output all objects in specified folder
            returns a list with objects(name & path)
        '''
        print(60 * '=')
        print('GSM OBJECTS in {}'.format(folder.split(os.sep)[-1]))
        print(60 * '=')
        walk = list(os.walk(folder))
        tree = self.get_tree(walk, folder)
        for i in tree:
            print('{:<30}: {}'.format(i[0], i[1]))
        return tree
# ========= BLEND WITH LIST_OBJECTS ==================================

    def make_all(self):
        ''' makes all objects in project
            transforms all source folders in .gsm files
        '''
        if os.path.isfile(self.lp_xml_converter):
            output = None
            p = Popen([self.lp_xml_converter,
                       'x2l',
                       '-img',
                       self.folder_images,
                       self.folder_xml,
                       self.project_library], stdout=PIPE)
            # TODO add password option
            output = p.communicate()[0]
            output = output.decode("utf-8")[:-1]
            output = output.replace('\r', '')
            print("Making all objects from library.")
            print(output)

    def import_all(self):
        ''' gets all objects from library folder
            puts them in the xml folder
        '''
        if os.path.isfile(self.lp_xml_converter):
            output = None
            p = Popen([self.lp_xml_converter,
                       'l2x',
                       '-img',
                       self.folder_images,
                       self.folder_library,
                       self.folder_xml], stdout=PIPE)
            # TODO add password option
            output = p.communicate()[0]
            output = output.decode("utf-8")[:-1]
            output = output.replace('\r', '')
            print("Importing all objects from library.")
            print(output)


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
        if not self.check_project():
            return
        print(60 * '+')
        self.list_gsm_objects()
        print(60 * '=')
        print(60 * '+')
        self.make_all()
        print(60 * '+')


class IdaAllImportCommand(IDACommand):
    def run(self):
        self.import_all()
        if not self.check_project():
            return
        print(60 * '+')
        print('IDA Import All')
        print(60 * '+')
        # self.list_project_info()
        objects = self.list_objects(self.folder_xml)
        print(60 * '=')
        for lp in objects:
            filename = '{}/{}/{}'.format(self.folder_xml, lp[0], lp[1])
            # TODO try to put this in method, make structure at given folder
            lp_name = lp[1].split('.')[0]
            try:
                os.makedirs('{}/{}/{}.CODE'.format(self.folder_code, lp[0], lp_name))
            except:
                pass
            with open(filename, 'r', encoding='utf-8') as obj_file:
                xml = obj_file.read()
            lp_root = ET.fromstring(xml)
            # self.unpack_object(lp, lp_root)
            s_num = 0
            for k in scripts:
                t = lp_root.find('.//' + k).text
                if t.strip() != '':
                    s_num += 1
            print('Found {} Scripts in {}'.format(s_num, lp[1]))
            # for i in list(lp_root.iter()):
            #     print(i)
            # print(lp_root.findall('.//Script_2D')[0].items())
            # print(lp_root.findall('.//Script_2D')[0].text)
        print(60 * '+')


class IdaLibraryMakeCommand(IDACommand):
    def run(self):
        sublime.error_message('IDA Message:\nFunction not yet implemented.')


class IdaLibraryUnpackCommand(IDACommand):
    def run(self):
        sublime.error_message('IDA Message:\nFunction not yet implemented.')
