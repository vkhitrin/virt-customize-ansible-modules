# virt-customize Ansible Modules

Example on how runnig this module, assumes you have everything installed (mentioned in root dir).

Download a CentOS cloud image to /tmp:

`curl https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud-1809.qcow2 -o /tmp/CentOS-7-x86_64-GenericCloud-1809.qcow2`

Run playbook on localhost:

`ansible-playbook main.yml -i hosts`
