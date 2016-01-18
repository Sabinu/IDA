import sublime
import sublime_plugin


class ImportallCommand(sublime_plugin.WindowCommand):
    def run(self):
        project_info = self.window.extract_variables()
        items = ['platform', 'project_name', 'project_path']
        print(60 * '=')
        for item in items:
            print('{:<15}: {}'.format(item, project_info[item]))
        print(60 * '=')


# ==========================================================

# Extends TextCommand so that run() receives a View to modify.
# class DuplicateCommand(sublime_plugin.TextCommand):
#     def run(self, view, *args):
#         print(sys.version)
#         # Walk through each region in the selection
        # for region in view.selection():
              # Only interested in empty regions
              # otherwise they may span multiple
#             # lines, which doesn't make sense for this command.
#             if region.empty():
                 # Expand the region to the full line it resides on, excluding the newline
#                 line = view.line(region)
#                 # Extract the string for the line, and add a newline
#                 lineContents = view.substr(line) + '\n'
#                 # Add the text at the beginning of the line
#                 view.insert(line.begin(), lineContents)
