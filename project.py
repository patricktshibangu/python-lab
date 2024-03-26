import subprocess
import os
import time

def main():
    print("Download the Splunk Enterprise tar file")
    subprocess.run(["sudo", "rm", "-rf", "/opt/splunk*"])
    os.chdir("/opt")
    subprocess.run(["sudo", "wget", "-O", "splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz", "https://download.splunk.com/products/splunk/releases/9.0.4.1/linux/splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz"])
    print("Extract the tar file to /opt")
    subprocess.run(["sudo", "tar", "-zxvf", "splunk-9.0.4.1-419ad9369127-Linux-x86_64.tgz", "-C", "/opt"])
    os.chdir("/opt/splunk/bin/")
    print("Start Splunk Enterprise and set up the admin user and password")
    subprocess.run(["sudo", "./splunk", "start", "--accept-license", "--answer-yes", "--no-prompt", "--seed-passwd", "abcd1234"])
    print("Enable Splunk at startup")
    subprocess.run(["sudo", "./splunk", "enable", "boot-start"])
    print("Please go to the browser, access Splunk on port 8000, username: admin password: abcd1234")
    time.sleep(4)
    exit(0)

if __name__ == "__main__":
    main()
