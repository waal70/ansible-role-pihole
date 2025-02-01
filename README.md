waal70.pihole
=========

Installs pihole on a dummy network interface (it assumes you have some other DNS running).  
If requested, it will purge the pihole adlist database and repopulate, using mongodb commands.

Requirements
------------

Assumes you have some form of DNS running on the proper network interface (e.g. samba DNS)  
In pihole.yml, a reference is made to a client list with custom DNS entries. For now it defaults to
    ~/ansible/home/inventory/client.list
An example file is provided in this role's files folder (custom.list)  
Change the location in the task or make sure you provide the file  
It also presumes a passwordless web GUI. If you do not want this, please change
    setupVars.conf.j2
in the templates folder of this role

Role Variables
--------------

    install_pihole: false # switch to (re-)install pihole  

The name of the dummy interface  
    iface_dummy: "eth53"  
    iface_dummy_private_ipv4_prefix: "10.1.1."  
    iface_dummy_private_ipv6_prefix: "2a10:3781:3623:d0::"  

My provider documents these on [https://freedom.nl/page/servers], use your own if needed  
Forwarder 1 and 2 are required  
    forward_dns_1: "185.93.175.43" # Google would be 8.8.8.8  
    forward_dns_2: "185.232.98.76" # Google would be 8.8.4.4  
Use 3 and 4 for IPv6. You can also leave them empty  
    forward_dns_3: "2a10:3780:2:52:185:93:175:43"  
    forward_dns_4: "2a10:3780:2:53:185:232:98:76"  

The json (in pihole export format) for the adlists. If you wish to add adlists, do that here so that this script may install  
    adlists: "{{ lookup('file', 'myadlist.json') | from_json }}"  

Various whitelists and blacklists, in both exact and regex forms. Again, these adhere to the pihole-export format, for your convenience  
    wl_exact: "{{ lookup('file', 'whitelist-exact.json') | from_json }}"  
    wl_regex: "{{ lookup('file', 'whitelist-regex.json') | from_json }}"  
    bl_exact: "{{ lookup('file', 'blacklist-exact.json') | from_json }}"  
    bl_regex: "{{ lookup('file', 'blacklist-regex.json') | from_json }}"  

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - waal70.pihole

License
-------

MIT

Author Information
------------------

[https://github.com/waal70]
