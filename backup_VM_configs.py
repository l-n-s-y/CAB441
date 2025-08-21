#!/bin/python3

import os, shutil

routing_table = {
    "host VM": "172.0.99.1",
    "extrouter": "172.0.99.2",
    "introuter1": "172.0.99.3",
    "introuter2": "172.0.99.4",
    "introuter3": "172.0.99.5",
    "introuter4": "172.0.99.6",
    "dns": "172.0.99.7",
    "vpn": "172.0.99.8",
    "git": "172.0.99.9",
    "www": "172.0.99.10",
    "db": "172.0.99.11",
    "wiki": "172.0.99.12",
    "dev1": "172.0.99.13",
    "bastion": "172.0.99.14",
    "staff1": "172.0.99.15"
}

def main():
    if os.path.exists("VM_BACKUPS"):
        print("[!] WARNING: VM_BACKUPS directory already detected. Continuing will overwrite previous backups.")
        while True:
            res = input("Do you want to continue? (Y/n): ").lower()
            if res != "y" and res != "n" and len(res)>0:
                print("!!! INVALID SELECTION !!!")
            elif res == "n":
                print("[*] Goodbye")
                exit()
            else:
                break
        shutil.rmtree("VM_BACKUPS",ignore_errors=True)

    #os.rmdir("VM_BACKUPS")
    os.mkdir("VM_BACKUPS")
    os.chdir("VM_BACKUPS")

    nft_dir_command = "scp -r student@{}:/etc/nftables.d/* nftables.d/."
    nft_conf_command = "scp student@{}:/etc/nftables.conf nftables.conf"

    for hostname in routing_table:
        print(f"[?] Backing up student@{hostname}...")
        os.mkdir((dirname := hostname+"_backup"))
        os.chdir(dirname)

        os.mkdir("nftables.d")

        ip = routing_table[hostname]
        print(f"\t[?] IP parsed as: {ip}")

        dir_comm = nft_dir_command.format(ip)
        conf_comm = nft_conf_command.format(ip)
        print(f"\t[?] executing: [ {dir_comm} ]")
        # os.system(dir_comm)
        print(f"\t[?] executing: [ {conf_comm} ]")
        # os.system(conf_comm)

        os.chdir("../")

    print("[*] All done.")


if __name__ == "__main__":
    main()
