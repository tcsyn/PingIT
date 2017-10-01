import subprocess
import time

tgts = "www.google.co.uk"

while True:

    def hostcheck(target):
        output = subprocess.Popen(['ping', '-c', '1', '{}'.format(target)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = output.communicate()

        status = int(output.returncode)

        print status

        time.sleep(1)

    hostcheck = hostcheck(tgts)
