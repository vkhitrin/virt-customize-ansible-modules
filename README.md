# virt-customize Ansible Modules

**Note:** This is a POC repo

**Note:** Due to it being a POC repo, code isn't optimized.

virt-customize Ansible modules allow users to use Ansible to automate commonly used libguestfs actions in a native way.

## Prerequisites:

On Ansible Controller:
* Ansible >= 2.4.0 (May work on earlier releases)
* Python >= 2.7.5 || Python >= 3.4
* gcc
* libguestfs python bindings:  
    * System:  
      If your distribution's package manager contains 'python-libguestfs', install it (via `yum`, `apt` ...)  
    * Running in a virtual environment:  
      If a virtual environment is used, refer to [guestfs python bindings in a virtualenv](http://libguestfs.org/guestfs-python.3.html#using-python-bindings-in-a-virtualenv)  
      In order to install via pip download the relevant version from `http://download.libguestfs.org/python/`  
      Example, `http://download.libguestfs.org/python/guestfs-1.36.10.tar.gz`

On Ansible Host:
* gcc
* libguestfs
* libguestfs-devel
* Python >= 2.7.5 || Python >= 3.4

## Compatability Matrix
:heavy_check_mark: - Fully Supported and tested  
:heavy_exclamation_mark: - Supported and not tested or Half supported  
:x: - Not supported

| Distro             | Supported                | Notes           |
|--------------------|--------------------------|-----------------|
| Fedora/CentOS/RHEL | :heavy_check_mark:       |                 |
| Ubuntu             | :heavy_check_mark:       |                 |
| Debian             | :heavy_exclamation_mark: | Not tested      |
| Windows            | :x:                      | Not Implemented |

## Documentation

Please refer to [repo's documentation](/docs/README.md) for more infromation

## Installation

**TODO:** Host on PyPI

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
