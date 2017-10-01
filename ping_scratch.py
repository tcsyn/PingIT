#Host check
#ping return codes, 1 = up, 2 = resolvable but unreachable, 68 = unresolvable & unreachable

import subprocess
import time
import cPickle as pickle

#global vars

tgts = "newss.bbc.co.uk"
timenow = time.strftime('%d/%m/%y %H:%M:%S')

def main():


    def hostcheck(target):

        output = subprocess.Popen(['ping', '-c', '1', '{}'.format(target)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = output.communicate()

        status = output.returncode

        def hoststatus(x):
            # Store the current value as object and load value and set as lastv
            f = file('/Users/chris/status', 'wb')
            pickle.dump(timenow, f)
            pickle.dump(x, f)
            f.close()
            print x

        hoststatus(status)

    hostcheck(tgts)

main()

