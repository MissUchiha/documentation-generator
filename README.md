# Customized KDE kapidox tool

Customized kapidox tool for generating KDE documentation piece by piece with choosen type of index page list (products or frameworks).

Updated code is surrounded with comments containing author's name.

Files that have been modified:

- kapidox/src/kapidox_generate.py
- kapidox/src/kapidox/argparserutils.py
- kapidox/src/kapidox/generator.py
- kapidox/src/kapidox/hlfunctions.py
- kapidox/src/kapidox/utils.py
- kapidox/src/kapidox/data/templates/subgroup-sidebar.html
- kapidox/src/kapidox/data/templates/subgroup.html

Files that have been created:

- kapidox/src/index_and_search_generate.py
- kapidox/src/kapidox/data/templates/subgroup-list.html
- kapidox/src/kapidox/data/templates/subgroup-about.html
- kapidox/src/kapidox/data/templates/frontpage-sidebar-frameworks.html
- kapidox/src/kapidox/data/templates/frontpage-frameworks.html
- kapidox/src/kapidox/data/templates/api-reference.html

Tool created for getting source code:

- kdocsync/doxsync.py

Pipeline script:

- pipeline-scripts/generate-documentation.pipeline
