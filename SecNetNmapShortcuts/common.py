import nmap
import os
from lxml import etree
from datetime import date

nm=nmap.PortScanner()

def sweep(subnet):
    nm.scan(hosts=subnet,arguments='-sn -oG -')
    hosts_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]
    output = ""
    for host,status in hosts_list:
        output = output + ('{0}: {1}\n'.format(host,status))
    return output

def intenseScan(ip):
    nm.scan(ip,arguments='-A')
    filename = ip+'_nmap_output_'+date.today().isoformat()+'.xml'
    f = open(filename,'w')
    f.write(nm.get_nmap_last_output())
    f.close()
    return(filename)

def XMLToHTML(xml):
    dom = etree.parse(xml)
    xslt = etree.parse('/usr/local/Cellar/nmap/7.60/share/nmap/nmap.xsl')
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    filename = xml.strip('.xml')+'.html'
    f = open(filename,'w')
    #etree.tostring outputs as binary, so converting to string is necessary; plus, it also adds some extra garbage to
    #the final HTML output, so the extra strip and replace commands are necessary too
    f.write(str(etree.tostring(newdom, pretty_print=True)).strip("'").strip("b\'").replace("\\n",'\n'))
    f.close()
    os.remove(xml)
    return(filename)