# cups-airprint/rootfs/usr/local/bin/airprint-generate.py
#!/usr/bin/env python3
"""
Bundled copy of tjfontaine/airprint-generate (lightly trimmed) to emit
Avahi .service files for each shared printer in local CUPS.
If you prefer, replace this file with the upstream project at build time.
"""
import cups, os, sys
import argparse


TEMPLATE = """<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
<name replace-wildcards="yes">{name}</name>
<service>
<type>_ipp._tcp</type>
<subtype>_universal._sub._ipp._tcp</subtype>
<port>631</port>
<txt-record>air=none</txt-record>
<txt-record>qtotal=1</txt-record>
<txt-record>rp=printers/{queue}</txt-record>
<txt-record>ty={ty}</txt-record>
<txt-record>note=Home Assistant</txt-record>
<txt-record>product=(GPL Ghostscript)</txt-record>
<txt-record>pdl=application/pdf,application/postscript,image/jpeg,image/urf</txt-record>
<txt-record>URF=DM3</txt-record>
</service>
</service-group>
"""


def generate(dest):
    conn = cups.Connection()
    printers = conn.getPrinters()
    os.makedirs(dest, exist_ok=True)
    for name, attrs in printers.items():
        if not attrs.get('printer-is-shared', True):
            continue
        queue = name
        ty = attrs.get('printer-info', name)
        xml = TEMPLATE.format(name=name, queue=queue, ty=ty)
        with open(os.path.join(dest, f"airprint-{name}.service"), 'w') as f:
            f.write(xml)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dest', default='/etc/avahi/services')
    args = parser.parse_args()
    generate(args.dest)