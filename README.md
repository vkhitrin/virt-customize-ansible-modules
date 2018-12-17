# virt-customize Ansible Modules

**Note:** This is a POC repo, if you're part of RedHat please contribute to the [desgin sheet](https://docs.google.com/document/d/1ho_iVpoyiGbAX8mtgpfByGtlwvKNQ8bcmd_0-orz45s/)

**Note:** Due to it being a POC repo, code isn't optimized.

virt-customize Ansible modules allow users to use Ansible to automate commonly used libguestfs actions in a native way.

## Prerequisites:

* Ansible >= 2.5.11
* Python >= 2.7.5
* [guestfs python bindings](http://libguestfs.org/guestfs-python.3.html#using-python-bindings-in-a-virtualenv)

## Documentation:

Can be viewed inside each module under the "DOCUMENTATION" variable.

## Examples:

Can be viewed inside each module under the "EXAMPLES" variable.

## Results:

Can be viewed inside each module under the "RETURN" variable.

## Installation

TO BE IMPLEMENTED IN A PROPER WAY

Make sure ansible and guestfs bindings are installed.

For now, copy `library` and `module_utils` directories to a directory where your playbook resides in.

## Uninstallation

TO BE IMPLEMENTED IN A PROPER WAY

Delete `library` and `module_utils` directories.

## License

This project is licensed under GPL-3.0 License. Please see the (COPYING.md)[https://github.com/vkhitrin/virt-customize-ansible-modules/blob/master/COPYING.md)] for more information
