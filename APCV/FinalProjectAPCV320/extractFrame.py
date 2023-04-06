class Frame:
    """
    A Frame is use to represent a data frame described in the given file.

    Attributes:
    id: int, frame number id such as 1 of frame 1 in the given file
    src: str, source address such as "00:14:ee:08:dd:b1" of frame 1
    dec: str, destination address such as "01:00:5e:7f:ff:fa" of frame 1
    ftype: str, frame type such as "0x800" that describes the IPv4 protocol of frame 1

    Methods:
    __init__
    __str__
    setAddress: set either src or dec
    setFrameType: set ftype value
    """

    def __init__(self, frameId, source="", dest="", frame_type=""):
        """
        n: an int set as the id of the Frame object
        src: a str set as the source address
        dst: a str set as the destination address
        ftype: a str set as the fame type
        """
        self.frame_id = frameId
        self.source = source
        self.dest = dest
        self.frame_type = frame_type

    def setAddress(self, address, is_source):
        """
        address: a string to set as src or dst address
        isSrc: a bool, if it is True, set src as address and otherwise set dst as address
        """
        if is_source:
            self.source = address
        else:
            self.dest = address

    def setFrameType(self, frame_type):
        """
        ftype: a string to set as ftype value
        """
        self.frame_type = frame_type

    def __str__(self):
        """
        Returns a string to represent the Frame object. For example, frame 1
        in the given file could be represented as:

        Frame 1, Src:00:14:ee:08:dd:b1, Dst:01:00:5e:7f:ff:fa, Type:0x0800

        """
        return f"Frame {self.frame_id}, Src:{self.source}, Dst:{self.dest}, Type:{self.frame_type}"


def extractTextFileFrames(input_filename, src_encoding="utf-8"):
    """
    input_filename: str, input file name such as "wireShark.txt"
    src_encoding: str, encoding used to open the input file

    Returns a list of Frame objects
    """
    frames = []

    with open(input_filename, "r", encoding=src_encoding) as input_file:
        for line in input_file:
            if line.startswith('Frame'):
                frameId = (line.split()[1])
            if line.startswith('Ethernet II'):
                source = line.split('Src: ')[1].split()[1]
                source_str = source.replace("(", "").replace(")", "").replace(",", "")
                dest = line.split('Dst: ')[1].split()[1]
                dest_str = dest.replace("(", "").replace(")", "")

            if 'Type: ' in line:
                frame_type = line.split()[2].split()[0]
                frame_type_str = frame_type.replace("(", "").replace(")", "")
                frame = Frame(frameId, source_str, dest_str, frame_type_str)
                frames.append(frame)

    return frames


# Printing
f = Frame(int("1"), '00:14:ee:08:dd:b1', '01:00:5e:7f:ff:fa', '0x0800')
print('Example frame creation: ', f)

frames = extractTextFileFrames("wireshark.txt")
for f in frames:
    print(f)
