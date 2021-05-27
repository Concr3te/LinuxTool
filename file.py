 
def GetSSHPort():
     config_file = "/etc/ssh/sshd_config"
     search_string = "Port"
     with open(config_file, 'r') as read_obj:
         for line in read_obj:
             if search_string in line:
                 words = line.split(' ')
                 port = int(words[-1])
                 return port

def GetFTPPort():
    config_file = "/etc/vsftpd.conf"
    search_string = "listen_port"
    with open(config_file, 'r') as read_obj:
        for line in read_obj:
            if search_string in line:
                words = line.split('=')
                return int(words[-1])
            return 21

if __name__ == "__main__":
    print(GetSSHPort())
    print(GetFTPPort())
