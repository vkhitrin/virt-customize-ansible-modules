# Documentation

## Modules

Full documentation(ansible-doc) is present inside the module.

| Module                   | Description                | Documentation                                                             |
|--------------------------|----------------------------|---------------------------------------------------------------------------|
| virt_customize_command   | Execute commands           | [doc](/ansible/modules/virt_customize/virt_customize_command.py#L14-L47)  |
| virt_customize_pakacges  | Manage packages            | [doc](/ansible/modules/virt_customize/virt_customize_packages.py#L14-L51) |
| virt_customize_users     | Manage users               | [doc](/ansible/modules/virt_customize/virt_customize_users.py#L14-L46)    |
| virt_customize_download  | Fetch files                | [doc](/ansible/modules/virt_customize/virt_customize_download.py#L14-L46) |
| virt_customize_upload    | Upload files               | [doc](/ansible/modules/virt_customize/virt_customize_upload.py#L14-L47)   |

## Sample Play

Assumes you have everything installed (mentioned in [repo's README](/README.md)).

### Install package on image located on localhost:

Download a CentOS cloud image to /tmp:

`curl https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud-1809.qcow2 -o /tmp/CentOS-7-x86_64-GenericCloud-1809.qcow2`

Run playbook on localhost:

`ansible-playbook docs/samples/main.yml -i hosts`
