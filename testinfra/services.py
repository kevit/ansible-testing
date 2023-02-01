def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

 host.ansible("apt", "name=nginx state=present", become=True)["changed"]



 py.test --hosts='ssh://server'
 py.test --hosts='ansible://all'

  py.test --hosts='kubectl://mypod-a1b2c3'
  py.test --hosts='podman://container_id_or_name'


  -qq --nagios --tb line test_ok.py; echo $?

## JUnit output
  py.test --junit-xml junit.xml tests.py


## Check dependencies
import pytest

@pytest.mark.parametrize("name,version", [
    ("nginx", "1.6"),
    ("python", "2.7"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

## the same via ansible
def check_ansible_play(host):
    assert not host.ansible("package", "name=nginx state=present")["changed"]


import testinfra
def test_os_release(host):
    assert host.file("/etc/os-release").contains("Fedora")



location / {
    add_header location root always;
}

location ~ /(\w+\-)\.html {
    add_header location html always;    
}
}

location ~ /(\w+\-)\.html {
    add_header location 2;    
}