import zipfile
import hashlib
import base64

apkName = "WA.apk"
zipFile = zipfile.ZipFile(apkName,'r')

hash = hashlib.md5()
hash.update(zipFile.read('classes.dex'))

print("ClassedDEX: "+ base64.b64encode(hash.digest()));
