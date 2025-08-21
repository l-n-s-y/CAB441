#!/bin/python3

import os

from backup_VM_configs import routing_table

# todo: currently can't handle sudo level stuff, or anything involving a login prompt
def main():
    
    comm = input("$>")

    for hostname in routing_table:
        ip = routing_table[hostname]
        
        # todo: remove sshpass in favour of silent PKI handshakes. unfortunately
        # a tool is needed to deposit the public keys in the first place, so you 
        # can't make one without the other :)
        print("Sending to: ", hostname, ".student441...")
        final_comm = f"sshpass -p {os.environ['SUPER_SECRET_SSH_PASSWORD']} ssh -oStrictHostKeyChecking=no student@{ip} {comm}"
        print(final_comm)
        res = os.popen(final_comm)
        if res is None:
            print("[!] ERROR: command send failed.")
        print(f"[ {hostname}.student441 ]=====================")
        print(res.read())
        print(f"==============================================")


    print("[+] All command sends finished.")
        


if __name__ == "__main__":
    main()
