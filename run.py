from mininet.net import Mininet
from mininet.cli import CLI
from minicps.mcps import MiniCPS

from topo import HomeTopo
from time import sleep

import sys


class HomeCPS(MiniCPS):

    def __init__(self, name, net):

        self.name = name
        self.net = net

        net.start()

        net.pingAll()

        # start devices
        plc1, plc2, plc3 = self.net.get(
            'plc1', 'plc2', 'plc3')

        # plc1.cmd(sys.executable + ' plc1.py &')
        # plc2.cmd(sys.executable + ' plc2.py &')
        # plc3.cmd(sys.executable + ' plc3.py &')

        plc1.cmd('xterm -e "python2.7 plc1.py" &')
        sleep(1)
        plc2.cmd('xterm -e "python2.7 plc2.py" &')
        sleep(1)
        plc3.cmd('xterm -e "python2.7 plc3.py" &')
        sleep(1) 

        CLI(self.net)

        net.stop()

if __name__ == "__main__":

    topo = HomeTopo()
    net = Mininet(topo=topo)

    homecps = HomeCPS(
        name='homecps',
        net=net)
