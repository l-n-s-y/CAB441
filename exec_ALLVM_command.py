#!/bin/python3

import os

from backup_VM_configs import routing_table


def exec_remote():
    while True:
        comm = input("$>")
        if comm.lower() == "exit":
            break
        if comm.lower() == "help":
            print("enter bash command or 'exit'")
            continue

        for hostname in routing_table:
            ip = routing_table[hostname]
            
            # todo: remove sshpass in favour of silent PKI handshakes. unfortunately
            # a tool is needed to deposit the public keys in the first place, so you 
            # can't make one without the other :)
            print("Sending to: " + hostname + ".student441...")
            final_comm = f"sshpass -p {os.environ['SUPER_SECRET_SSH_PASSWORD']} ssh -oStrictHostKeyChecking=no student@{ip} {comm}"
            print(final_comm)
            res = os.popen(final_comm)
            if res is None:
                print("[!] ERROR: command send failed.")
            print(f"[ {hostname}.student441 ]=====================")
            print(res.read())
            print(f"==============================================")


        print("[+] All command sends finished.")

def exec_local():
    print("[?] include '-_-' where the hostname should go.")
    while True:
        comm = input("$>")
        if comm.lower() == "exit":
            break
        if comm.lower() == "help":
            print("enter bash command or 'exit'")
            continue

        for hostname in routing_table:
            ip = routing_table[hostname]

            print("Pointing at: " + hostname + ".student441...")
            final_comm = f"sshpass -p {os.environ['SUPER_SECRET_SSH_PASSWORD']} " + comm.replace("-_-", ip)
            print(final_comm)
            res = os.popen(final_comm)
            if res is None:
                print("[!] ERROR: command exec failed.")
            print(f"[ {hostname}.student441 ]=====================")
            print(res.read())
            print(f"==============================================")

        print("[+] All commands execs finished.")


# todo: currently can't handle sudo level stuff, or anything involving a login prompt
def main():
    print("1) local command")
    print("2) remote command")
    choice = input("#>")
    try:
        c = int(choice)
    except:
        print("[!] INVALID")
        exit()

    if c > 2 or c < 1:
        print("[!] INVALID")
        exit()

    if c == 1:
        exec_local()
    else:
        exec_remote()

if __name__ == "__main__":
    main()
