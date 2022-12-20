import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('version_dir_pattern', [
    '5.6.0$'
])
def test_cm_installed(host, version_dir_pattern):

    cm_home = host.check_output('find %s | grep --color=never -E %s',
                                '/opt/camunda-modeler/',
                                version_dir_pattern)

    cm_sh = host.file(cm_home + '/camunda-modeler')

    assert cm_sh.exists
    assert cm_sh.is_file
    assert cm_sh.user == 'root'
    assert cm_sh.group == 'root'
    assert oct(cm_sh.mode) == '0o755'


def test_cm_exists(host):
    assert host.run('which camunda-modeler').rc == 0


def test_cm_desktop_file(host):
    desk_file = host.file('/usr/share/applications/camunda-modeler.desktop')

    assert desk_file.exists
    assert desk_file.is_file
    assert desk_file.user == 'root'
    assert desk_file.group == 'root'
    assert oct(desk_file.mode) == '0o644'


@pytest.mark.parametrize('fact_group_name', [
    'camundamodeler'
])
def test_facts_installed(host, fact_group_name):
    fact_file = host.file('/etc/ansible/facts.d/' + fact_group_name + '.fact')

    assert fact_file.exists
    assert fact_file.is_file
    assert fact_file.user == 'root'
    assert fact_file.group == 'root'
    assert oct(fact_file.mode) == '0o644'
