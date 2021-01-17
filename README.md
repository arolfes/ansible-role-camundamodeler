Ansible Role: camunda-modeler
======================================

[![Build Status](https://github.com/arolfes/ansible-role-camunda-modeler/workflows/molecule%20tests/badge.svg?branch=master)](https://github.com/arolfes/ansible-role-camunda-modeler/actions?query=branch%3Amaster+workflow%3A%22molecule+tests%22)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-arolfes.camunda-modeler-blue.svg)](https://galaxy.ansible.com/arolfes/camunda-modeler)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/arolfes/ansible-role-camunda-modeler/master/LICENSE)

Role to install [https://camunda.com/de/products/camunda-bpm/modeler/](Camunda-Modeler) .

You can start it from shell via `camunda-modeler` or via shortcut from your desktop. (`cp /usr/share/applications/camunda-modeler.desktop ~/Desktop/`)

```bash
$ which camunda-modeler


cp /usr/share/applications/camunda-modeler.desktop ~/Desktop/
```

Requirements
------------

* Ansible >= 2.8.0

* Linux Distribution

    * Debian Family

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

        * Debian

            * Stretch (9)
            * Buster (10)

    * RedHat Family

        * CentOS

            * 7
            * 8

        * Fedora

            * 31

    * SUSE Family

        * openSUSE

            * 15.1

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Camunda Modeler Version to download and unpack
cm_version: '4.5.0'

# Download url for Camunda Modeler tarball
cm_download_url: 'https://github.com/camunda/camunda-modeler/releases/download/v{{ cm_version }}'

# Filename of camunda-modeler redistributable package
cm_redis_filename: 'camunda-modeler-{{ cm_version }}-linux-x64.tar.gz'

# Base installation directory
cm_install_dir: '/opt/camunda-modeler/{{ cm_version }}'

# Directory to store files downloaded for Camunda Modeler installation
cm_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

### Supported camunda-modeler Versions

The following versions of camunda-modeler are supported without any additional configuration

* 4.5.0
* 4.0.0
* 3.0.0

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: arolfes.camunda-modeler
```
You can install a specific version of Camunda-Modeler by specifying the cm_version.
```yaml
- hosts: servers
  roles:
     - role: arolfes.camunda-modeler
       cm_version: '4.0.0'
```
You can provide your own download mirror.
In this case the latest version (4.5.0) will be downloaded from google and not from github.
See testcase [molecule/ubuntu-max-cm-max/playbook.yml](ubuntu-max-cm-max)
```yaml
- hosts: servers
  roles:
     - role: arolfes.camunda-modeler
       cm_download_url: https://downloads.camunda.cloud/release/camunda-modeler/4.5.0
```
You can provide your own patched version.
```yaml
- hosts: servers
  roles:
     - role: arolfes.camunda-modeler
       cm_download_url: https://localhost/camunda-modeler
       cm_redis_filename: camunda-modeler-patched.tar.gz
       cm_redis_sha256sum: '862b48542cd916f7d06ce1f5a3e821eada1ca8b595c34a564671eb8a660fc519'

```


Role Facts
----------

This role exports the following Ansible facts for use by other roles:

* `ansible_local.camundamodeler.general.version`

    * e.g. `4.5.0`

* `ansible_local.camundamodeler.general.home`

    * e.g. `/opt/camunda/modeler/4.5.0`

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test --all
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

Alexander Rolfes




