# virt-customize Ansible Modules

This repository is deprecated in favor of [ansible-libguestfs-collection](https://github.com/vkhitrin/ansible-libguestfs-collection)!
---

**Note:** This is a POC repo

**Note:** Due to it being a POC repo, code isn't optimized.

virt-customize Ansible modules allow users to use Ansible to automate commonly used libguestfs actions in a native way.

## Prerequisites:

On Ansible Controller:
* Ansible >= 2.4.0 (May work on earlier releases)
* Python >= 2.7.5 || Python >= 3.4
* gcc

On Ansible Host:
* gcc
* libguestfs
* libguestfs-devel
* Python >= 2.7.5 || Python >= 3.4
* libguestfs python bindings:
    * System:
      If your distribution's package manager contains `python-libguestfs`, install it (via `yum`, `apt` ...)
    * pip:
      If a virtual environment is used or you do not have a pre packaged `python-libguestfs`, refer to [guestfs python bindings in a virtualenv](http://libguestfs.org/guestfs-python.3.html#using-python-bindings-in-a-virtualenv)
      In order to install via pip download the relevant version from `http://download.libguestfs.org/python/`
      Example, `http://download.libguestfs.org/python/guestfs-1.36.10.tar.gz`

## Compatibility Matrix
:heavy_check_mark: - Fully Supported and tested

:heavy_exclamation_mark: - Supported and not tested or partial support

:x: - Not supported

| Distro             | Supported                | Notes           |
|:------------------:|:------------------------:|:---------------:|
| Fedora/CentOS/RHEL | :heavy_check_mark:       |                 |
| Ubuntu             | :heavy_check_mark:       |                 |
| Debian             | :heavy_check_mark:       |                 |
| Windows            | :x:                      | Not Implemented |

## Documentation

Please refer to [repo's documentation](/docs) for more information

## Installation

TODO: Host on PyPI

### Install from remote:
```
pip install git+https://github.com/vkhitrin/virt-customize-ansible-modules
```

### Install from cloned repo
```
git clone https://github.com/VKhitrin/virt-customize-ansible-modules
cd virt-cusomize-ansible-modules
pip install .
```

## Uninstallation

```
pip uninstall virt-customize-ansible-modules
```

## License

This project is licensed under GPL-3.0 License. Please see the [COPYING.md](/COPYING.md) for more information.
