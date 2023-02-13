Ansible Role: camundamodeler
======================================

[![Build Status](https://github.com/arolfes/ansible-role-camundamodeler/workflows/molecule%20tests/badge.svg?branch=master)](https://github.com/arolfes/ansible-role-camundamodeler/actions?query=branch%3Amaster+workflow%3A%22molecule+tests%22)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-arolfes.camundamodeler-blue.svg)](https://galaxy.ansible.com/arolfes/camundamodeler)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/arolfes/ansible-role-camundamodeler/master/LICENSE)

Role to install [https://camunda.com/de/products/camunda-bpm/modeler/](Camunda-Modeler) .

You can start it from shell via `camunda-modeler` or via shortcut from your desktop. (`cp /usr/share/applications/camunda-modeler.desktop ~/Desktop/`)

```bash
$ which camunda-modeler 
/usr/local/bin/camunda-modeler


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

        * Fedora

            * 37

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
cm_version: '4.12.0'

# Download url for Camunda Modeler tarball
cm_download_url: 'https://github.com/camunda/camunda-modeler/releases/download/v{{ cm_version }}'

# Filename of camunda-modeler redistributable package
cm_redis_filename: 'camunda-modeler-{{ cm_version }}-linux-x64.tar.gz'

# Base installation directory
cm_install_dir: '/opt/camunda-modeler/{{ cm_version }}'

# Directory to store files downloaded for Camunda Modeler installation
cm_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"

# downloads and extract camunda modeler plugins to correct place
# by default it is disabled
# to enable just add plugins list and for each item define name and the url with zip or tar
#plugins:
#  - name: tooltip
#    url: https://github.com/viadee/camunda-modeler-tooltip-plugin/archive/refs/tags/v0.0.8.tar.gz
#  - name: property-info 
#    url: https://github.com/umb/camunda-modeler-property-info-plugin/archive/refs/tags/0.0.2.tar.gz
#  - name: token-simulation
#    url: https://github.com/bpmn-io/bpmn-js-token-simulation-plugin/archive/refs/heads/master.zip
#  - name: autosave
#    url: https://github.com/pinussilvestrus/camunda-modeler-autosave-plugin/archive/refs/tags/v0.2.0.tar.gz
#  - name: camunda-modeler-plugin-resize-tasks 
#    url: https://github.com/philippfromme/camunda-modeler-plugin-resize-tasks/archive/refs/heads/master.zip
#  - name: camunda-transaction-boundaries
#    url: https://github.com/bpmn-io/camunda-transaction-boundaries/archive/refs/tags/v1.1.2.tar.gz
#  - name: bpmn-js-embedded-comments
#    url: https://github.com/bpmn-io/bpmn-js-embedded-comments/archive/refs/tags/v0.6.1.tar.gz
```

### Supported camunda-modeler Versions

The following versions of camunda-modeler are supported without any additional configuration

* 5.8.0
* 5.7.0
* 5.6.0
* 5.5.1
* 5.5.0
* 5.4.1
* 5.4.0
* 5.3.0
* 5.2.0
* 5.1.0
* 5.0.0
* 4.12.0
* 4.11.1
* 4.11.0
* 4.10.0
* 4.9.0
* 4.8.1
* 4.8.0
* 4.7.0
* 4.6.0
* 4.5.0
* 4.4.0
* 4.3.0
* 4.2.0
* 4.1.1
* 4.1.0
* 4.0.0
* 3.7.3
* 3.7.2
* 3.7.1
* 3.7.0
* 3.6.0
* 3.5.0
* 3.4.1
* 3.4.0
* 3.3.5
* 3.3.4
* 3.3.3
* 3.3.2
* 3.3.1
* 3.3.0
* 3.2.3
* 3.2.2
* 3.2.1
* 3.2.0
* 3.1.2
* 3.1.1
* 3.1.0
* 3.0.1
* 3.0.0

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: arolfes.camundamodeler
```
You can install a specific version of Camunda-Modeler by specifying the cm_version.
```yaml
- hosts: servers
  roles:
     - role: arolfes.camundamodeler
       cm_version: '5.8.0'
```
add additional modeler plugins to be automatically installed
```yaml
- hosts: servers
  roles:
     - role: arolfes.camundamodeler
       plugins:
          - name: tooltip
            url: https://github.com/viadee/camunda-modeler-tooltip-plugin/archive/refs/tags/v0.0.8.tar.gz
          - name: property-info 
            url: https://github.com/umb/camunda-modeler-property-info-plugin/archive/refs/tags/0.0.2.tar.gz
          - name: token-simulation
            url: https://github.com/bpmn-io/bpmn-js-token-simulation-plugin/archive/refs/heads/master.zip
          - name: autosave
            url: https://github.com/pinussilvestrus/camunda-modeler-autosave-plugin/archive/refs/tags/v0.2.0.tar.gz
          - name: camunda-modeler-plugin-resize-tasks 
            url: https://github.com/philippfromme/camunda-modeler-plugin-resize-tasks/archive/refs/heads/master.zip
          - name: camunda-transaction-boundaries
            url: https://github.com/bpmn-io/camunda-transaction-boundaries/archive/refs/tags/v1.1.2.tar.gz
          - name: bpmn-js-embedded-comments
            url: https://github.com/bpmn-io/bpmn-js-embedded-comments/archive/refs/tags/v0.6.1.tar.gz
```
You can provide your own download mirror.
In this case the latest version (4.12.0) will be downloaded from google and not from github.
See testcase [molecule/ubuntu-max-cm-max/playbook.yml](ubuntu-max-cm-max)
```yaml
- hosts: servers
  roles:
     - role: arolfes.camundamodeler
       cm_download_url: https://downloads.camunda.cloud/release/camunda-modeler/5.8.0
```
You can provide your own patched version.
```yaml
- hosts: servers
  roles:
     - role: arolfes.camundamodeler
       cm_download_url: https://localhost/camunda-modeler
       cm_redis_filename: camunda-modeler-patched.tar.gz
       cm_redis_sha256sum: '862b48542cd916f7d06ce1f5a3e821eada1ca8b595c34a564671eb8a660fc519'

```


Role Facts
----------

This role exports the following Ansible facts for use by other roles:

* `ansible_local.camundamodeler.general.version`

    * e.g. `5.8.0`

* `ansible_local.camundamodeler.general.home`

    * e.g. `/opt/camunda/modeler/5.8.0`

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




