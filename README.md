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
* libguestfs (and in some scenarios libguestfs-tools)
* [guestfs python bindings](http://libguestfs.org/guestfs-python.3.html#using-python-bindings-in-a-virtualenv) >= 1.36.10

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
