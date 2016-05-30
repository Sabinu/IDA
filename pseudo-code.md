
    Make option for working from LCF or .library
    Make option for how many back-ups are allowed
    make JSON with tree
    make option for VERBOSE output

Import All:
    - backup .xml and CODE folder
    - if LCF is True >> backup .library & unpack
    - retain object_tree from .library folder in variable
    - run LP_XML
    - check if .xml tree is same with TEMP.tree
        - if not than revert from backup and through error
    - unpack from .xml to CODE
    - check if .xml tree is same with .xml
        - if not than revert from backup and through error