import sys
import zipfile
import hashlib
import base64
from xml.dom import minidom
from axmlparser import AXML

try:
        apkName = sys.argv[1]
        zipFile = zipfile.ZipFile(apkName,'r')
        hash = hashlib.md5()
        hash.update(zipFile.read('classes.dex'))
        axml = AXML(zipFile.read('AndroidManifest.xml'))
        xml = minidom.parseString(axml.get_buff())
        package = xml.documentElement.getAttribute("package")
        print("--> WhatsApp Version : "+xml.documentElement.getAttributeNS('http://schemas.android.com/apk/res/android', "versionName"))
        print("--> WhatsApp ClassesDEX MD5 : "+ str(base64.b64encode(hash.digest())));

except:
        print("Please enter directory of WhatsApp.apk")
