#!/usr/bin/python3
# Generate NET/NSAP to IS-IS Instance for linux
# Author: Tiago Eduardo Zacarias
# Project Change OSPF to IS-IS
# Date: 27/08/2023

class CalcNet:

    #Method INit
    def __init__(self, oct):

        # Attributes
        self.oct = oct

    # Method
    def gen_net(self):

        self.conv = hex(int(self.oct))[2:]
        self.cump = len(self.conv)

        if self.cump == 1:

            self.conv = "0" + self.conv
            return

        else:

            self.conv = self.conv
            return


def main():

    try:

        ip = input('Enter the loopback IP to generate the (NET/NSAP):')
        ip_parts = ip.split(".")
        oct_one = ip_parts[0]
        oct_two = ip_parts[1]
        oct_tree = ip_parts[2]
        oct_four = ip_parts[3]

        # Object 1
        calc1 = CalcNet(oct_one)
        calc1.gen_net()
        # Object 2
        calc2 = CalcNet(oct_two)
        calc2.gen_net()
        # Object 3
        calc3 = CalcNet(oct_tree)
        calc3.gen_net()
        # Object 4
        calc4 = CalcNet(oct_four)
        calc4.gen_net()

        print(
            f"\033[0;33m49.0000.0000.4116.c000.{calc1.conv}{calc2.conv}.{calc3.conv}{calc4.conv}.0000.00\033[0m")

    except (IndexError, ValueError) as error:
        print("You need to enter a valid IP."),

    except KeyboardInterrupt as error:
        print("System closed")


if __name__ == '__main__':
    main()
