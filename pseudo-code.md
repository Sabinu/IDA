Preferences:

    Make option for working from LCF or .library
    Make option for how many back-ups are allowed
    make JSON with tree
    make option for VERBOSE output

Import All:
''' all operation is made in .TEMP folder '''
  - backup    - make .TEMP folder
  - check     - if LCF
              - True  >> unpack LCF to .TEMP/.library
              - False >> continue
  - internal  - retain object_tree from .library folder in variable
  - operation - run LP_XML
  - check     - if .xml tree is same with TEMP.tree
              - True  >> continue
              - False >> revert from .TEMP and through error
  - operation - unpack from .xml to CODE
  - check     - if .xml tree is same with .xml
    - if not than revert from backup and through error
  - delete .TEMP folder

Export All:

  - make .TEMP folder
  - retain object_tree from CODE folder in variable
  - delete .TEMP folder
