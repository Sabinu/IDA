## Preferences:

    make option for working from LCF or .library
    make option for how many back-ups are allowed
    make JSON with tree
    make option for VERBOSE output

---

## Import All:

`all operations are made in .TEMP folder`
  - `backup`    - copy LCF, .library, .xml, images and CODE to `.TEMP folder`
  - `setting`   - if LCF
    - True  - unpack LCF
    - False - continue
  - `operation` - un-pack tree from .TEMP/.library to .TEMP/objects.json
  - `verbose`   - diff between .TEMP/.library with .library
  - `operation` - run LP_XML
  - `check`     - if .TEMP/.xml tree is same with .TEMP/objects.json
    - True  - continue
    - False - delete .TEMP and through error
  - `operation` - unpack from .xml to CODE
  - `check`     - if .xml tree is same with .xml
    - if not than revert from backup and through error
  - delete `.TEMP folder`

---

## Export All:

  - make .TEMP folder
  - retain object_tree from CODE folder in variable
  - delete .TEMP folder
