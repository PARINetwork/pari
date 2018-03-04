# -*- mode: ruby -*-
# vi: set ft=ruby :

IP = '192.168.5.100'
HOST = 'development.ruralindiaonline.org'
HOSTS_FILE = '/etc/hosts'
HOST_ENTRY = "#{IP} #{HOST}"

def add_host_entry
  script = <<-MARKER
    if ! grep -Fxq "#{HOST_ENTRY}" #{HOSTS_FILE} ; then
      echo Adding new host entry. Requires SUDO password of host machine.
      echo "#{HOST_ENTRY}" | sudo tee -a #{HOSTS_FILE} > /dev/null
    fi
  MARKER

  if ARGV[0] == 'up' || ARGV[0] == 'provision'
    system(script)
  end
end

Vagrant.configure("2") do |config|

  config.vm.synced_folder ".", "/vagrant", type: "nfs",  mount_options: ['rw', 'vers=3', 'tcp', 'fsc' ,'actimeo=2']

  config.vm.define 'pari.machine' do |machine|
    machine.vm.box = 'pari/devbox'
    machine.vm.network "private_network", ip: "#{IP}"
  end

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
  end

  add_host_entry

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = '../pari-ansible/site.yml'
    ansible.inventory_path = '../pari-ansible/hosts.yml'
    ansible.limit = 'vagrant'
    #ansible.tags = 'install'
    ansible.verbose = '-v'
    ansible.raw_ssh_args = ['-o ControlPath=/tmp/%r@%h:%p']
  end
end