import spidev
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

def setupSPI():
    # create SPI bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D8)
    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)
    return mcp

def readChannel(channel):
    # create the mcp object
    mcp = setupSPI()
    # Get value on given analog channel
    channel = AnalogIn(mcp, channel)

    return channel