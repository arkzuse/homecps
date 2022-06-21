from ipaddress import ip_address
from mininet.topo import Topo

from utils import *


class HomeTopo(Topo):

    def build(self):
        
        switch = self.addSwitch('s1')

        plc1 = self.addHost(
            'plc1',
            ip = PLC1_ADDR,
            mac = MAC['plc1']
        )
        self.addLink(plc1, switch)

        plc2 = self.addHost(
            'plc2',
            ip = PLC2_ADDR,
            mac = MAC['plc2']
        )
        self.addLink(plc2, switch)
        
        plc3 = self.addHost(
            'plc3',
            ip = PLC3_ADDR,
            mac = MAC['plc3']
        )
        self.addLink(plc3, switch)
