import subprocess
import time

tgts = "www.google.co.uk"

while True:

    def hostcheck(target):
        output = subprocess.Popen(['ping', '-c', '1', '{}'.format(target)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = output.communicate()

        status = int(output.returncode)

        time.sleep(1)

        out = hostcheck(tgts)

    out = 0

    while out == 0:
        out += 1
        print out
