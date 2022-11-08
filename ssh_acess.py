from paramiko import SSHClient
import os

# Open a SSH Connection
client = SSHClient()
client.load_system_host_keys()
client.connect('example.com', username='user', password='secret')

#redhat/CentOs/AmazonLinux
try:
    os.system('sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm')
    os.system('sudo systemctl status amazon-ssm-agent')
except Exception as e:
    #Debian
    try:
        os.system('wget https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/debian_amd64/amazon-ssm-agent.deb')
        os.system('sudo dpkg -i amazon-ssm-agent.deb')
        os.system('sudo systemctl status amazon-ssm-agent')
    except Exception as e:
        pass

#Close the ssh connection
client.close()