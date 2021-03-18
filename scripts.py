import os
import zipfile
from datetime import datetime


def package():
    def add_folder(_zf, folder):
        for dirname, subdirs, files in os.walk(folder):
            [_zf.write(os.path.join(dirname, f))
             for f in files if not f.startswith('.') and f != '__pycache__']

    zf = zipfile.ZipFile('pkg.zip', 'w', zipfile.ZIP_DEFLATED)
    zf.write('python.pex')
    zf.write('app.py')
    zf.write('models.py')
    zf.write('bs_utils.py')
    add_folder(zf, 'auth')
    add_folder(zf, 'templates')
    add_folder(zf, 'static')
    zf.close()


def deploy():
    package()


if __name__ == "__main__":
    import sys
    locals()[sys.argv[1]]()
