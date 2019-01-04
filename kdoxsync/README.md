# KDocsync tool

Tool for getting source code of products whose documentation needs to be generated.

YAML file with product definition needs to be created.
If product contains subgroups it should have this format:

```
---
  groups:
    - name: 'Frameworks'
      subgroups:
        - name: 'Tier 1'
          items:
            - name: 'kconfig'
              repoUrl: 'git://anongit.kde.org/kconfig.git'
              target: 'master'
            - name: 'kcoreaddons'
              repoUrl: 'git://anongit.kde.org/kcoreaddons.git'
              target: 'master'

```

If product doesn't contain subgroups, but it contains items it should have this format:

```
---
  groups:
    - name: 'PIM'
      items:
        - name: 'akonadi'
          repoUrl: 'git://anongit.kde.org/akonadi.git'
          target: 'master'

```

If product doesn't contain subgroups or items, it should have this format:

```
---
  item:
    name: 'phonon'
    repoUrl: 'git://anongit.kde.org/phonon.git'
    target: 'master'

```

Running the tool:

```
doxsync.py --projects-definition {path_to_the_yaml_file} --sourcesdir {path_to_the_directory_for_source_code}"
```

If git repo is already checked in _path_to_the_directory_for_source_code_ then doxsync tool will just pull latest code.
