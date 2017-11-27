import os
import re

DELIM = ','
TERM = '\n'

def parsePorts(filename):
    f = open(os.path.abspath(filename),'r')
    out = open(os.path.abspath('mod'+filename),'w')
    out.write(f.readline().strip(TERM)+',SourcePort,DstPort'+TERM)
    for line in f:
        elements = line.split(DELIM)
        if elements[4]=='TCP':
            ports = list(map(int, re.findall(r'\d+',elements[6])))
            sourcePort = ports[0]
            dstPort = ports[1]
            out.write(line.strip(TERM)+DELIM+str(sourcePort)+DELIM+str(dstPort)+TERM)
        else:
            out.write(line.strip(TERM)+DELIM+DELIM+TERM)
    out.close()