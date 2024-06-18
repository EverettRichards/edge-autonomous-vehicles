import paramiko

def execute_ssh_command(hostname,username,password,command):
    ssh_client = paramiko.SSHClient()

    try:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, password=password)
        stdin,stdout,stderr = ssh_client.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(f"Output: {output}")
        if error:
            print(f"Error: {error}")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        ssh_client.close()

command = "sudo python3 ~/picar-x/example/1.move.py"
execute_ssh_command("192.168.43.193","udel","bluehens",command)