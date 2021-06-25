from machine import UART

def processPkt(pkt: bytes):
        """
        packet = [0x59, 0x59, distL, distH, strL, strH, reserved, integration time, checksum]
        return True if there is a problem
        Note: the integration time always seems to be 0
        """
        # turn string data into array of bytes
        # pkt = list(map(ord, pkt))
        problem = bool()
        if len(pkt) != 9:
            problem = True
            print("< 9 bytes")

        # check header
        if pkt[0] != 0x59 or pkt[1] != 0x59:
            print("bad headers")
            problem = True

        # calculate checksum
        cs = sum(pkt[:8])
        cs &= 0xff
        # print('cs', cs, pkt[8])

        if pkt[8] != cs:
            problem = True
            print("bad checksum")

        # print('L {} H {}'.format(pkt[2], pkt[3]))

        #strength = pkt[4] + (pkt[5] << 8)
        # q    = pkt[7]

        # print('ans',dist, st, q)

        return problem


def getdistance(uart: UART):
    '''
    Input: uart port from pi pico
    ***********
    Output: return the distance read from uart sensor (for tfmini only)
    '''
    # flush serial
    while uart.any() > 0:
        uart.read(uart.any())
    data = uart.read(9)

    while processPkt(data):
        # re_read data
        while uart.any() > 0:
            uart.read(uart.any())
        data = uart.read(9)
        print(data)

    dist = (data[2] + (data[3] << 8))/100

    return dist


