waal70.pihole
=========

Determines whether samba-ad-dc is active on this device.
If it is, it will update smb.conf to take out dns forwarders, and have samba listen on a different dns port.
This also requires you set the authoritative domain for which samba is authoritative, pihole_localdns_authoritativedomain
It will then put the relevant stanzas in the dnsmasq.conf

If requested, it will purge the pihole adlist database and repopulate, using mongodb commands.

Requirements
------------

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

The port where you want SAMBA to have its DNS listen
    samba_dns_port: "5353"
The FQ domain name for which the samba built-in DNS is authoritative
    samba_realm: "samba.authoritativedomain"

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

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html#license-text)

Author Information
------------------

Unless otherwise noted, this entire repository is (c) 2025 by André (waal70). [See github profile](https://github.com/waal70)

Please contact me if you need a commercial license for any of these files
