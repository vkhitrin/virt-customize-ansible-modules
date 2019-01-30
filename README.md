# virt-customize Ansible Modules

**Note:** This is a POC repo

**Note:** Due to it being a POC repo, code isn't optimized.

virt-customize Ansible modules allow users to use Ansible to automate commonly used libguestfs actions in a native way.

## Prerequisites:

On host with Ansible installed:
* Ansible >= 2.4.0
* Python >= 2.7.5

On host:
* gcc
* libguestfs
* libguestfs python bindings:
    * Method A:  
    If your distribution's package manager contains 'python-libguestfs', install it (via `yum`, `apt` ...)  
    To be used in virtualenv, you could supply the parameter `--system-site-packages` when creating a virtualenv  
    * Method B:
    [guestfs python bindings in a virtualenv](http://libguestfs.org/guestfs-python.3.html#using-python-bindings-in-a-virtualenv)  
    **Requires libguestfs-devel to be installed by your package manager**  
    In order to install via pip download the relevant version from `http://download.libguestfs.org/python/`  
    Example, `http://download.libguestfs.org/python/guestfs-1.36.10.tar.gz`  

May work on earlier releases, tested on the above

## Modules:

Located under the `ansible/modules/virt_customize` directory and utilizes a helper utility script located in `ansible/module_utils/`.

### virt_customize_packages:

**Note:** Currently works only on images using `dnf`, `yum` and `apt` package managers.

Perform package manipulations on guest disk image:

* Install packages

* Remove packages

* List installed packages

### virt_customize_command:

Performs commands inside guest disk image

### virt_customize_upload:

**Note:** Currently doesn't check if file exists on guest disk image

**Note:** remote_src is not yet implemented

Uploads files/directories to guest disk image

### virt_customize_download:

**Note:** Currently doesn't check if file exists on guest disk image

**Note:** remote_src is not yet implemented

Downloads files/directories from guest disk image

### virt_customize_users

Maintaines users on guest disk image

## Documentation:

Please refer to `README.md` in `examples`.

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

This project is licensed under GPL-3.0 License. Please see the [COPYING.md](https://github.com/vkhitrin/virt-customize-ansible-modules/blob/master/COPYING.md) for more information.
