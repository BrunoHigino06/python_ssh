#Pre requirements
#pip install paramiko

from paramiko import SSHClient
import os

# Open a SSH Connection
with open("servers.txt") as servers:
    for server in servers:
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(server, username='', password='')

        #Install ssm agent on Ubuntu
        client.exec_command('sudo snap switch --channel=candidate amazon-ssm-agent')
        client.exec_command('sudo snap install amazon-ssm-agent --classic')
        client.exec_command('sudo snap start amazon-ssm-agent')


        #Close the ssh connection
        client.close()