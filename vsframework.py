#!/usr/bin/env python3
# Setting up Vapoursynth.framework

import os
import tarfile

# Software index. Change version number/tag to get newer versions.
openssl     = ('openssl',       'openssl-3.2.0',    'git://git.openssl.org/openssl.git',                                'git',      '',             'make', 'sudo make install', './config --prefix=/Library/Frameworks/VapourSynth.framework -no-shared')
xzutils     = ('xz',            'v5.4.5',           'https://github.com/tukaani-project/xz.git',                        'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --disable-shared')
zlib        = ('zlib',          'v1.3',             'https://github.com/madler/zlib.git',                               'git',      '',             'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --static')
python      = ('cpython',       'v3.11.7',          'https://github.com/python/cpython.git',                            'git',      '',             'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework  --enable-shared LDFLAGS="-L/Library/Frameworks/VapourSynth.framework/lib" CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include" PKG_CONFIG_PATH=/Library/Frameworks/VapourSynth.framework/lib/pkgconfig')
libjpg      = ('libjpeg-turbo', '3.0.1',            'https://github.com/libjpeg-turbo/libjpeg-turbo',                   'git',      '',             'make', 'sudo make install', 'cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/Library/Frameworks/VapourSynth.framework/ -DENABLE_STATIC=ON -DENABLE_SHARED=OFF .')
libpng      = ('libpng',        'v1.6.40',          'https://github.com/glennrp/libpng.git',                            'git',      '',             'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --enable-shared=no')
libtiff     = ('libtiff',       'v4.6.0',           'https://gitlab.com/libtiff/libtiff',                               'git',      '',             'make', 'sudo make install', 'cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/Library/Frameworks/VapourSynth.framework/ -DBUILD_SHARED_LIBS=OFF -Dzstd=OFF -Dlzma=OFF .')
imagemagick = ('ImageMagick',   '7.1.1-26',         'https://github.com/ImageMagick/ImageMagick',                       'git',      '',             'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --without-xml --disable-shared --enable-delegate-build CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include"')
freetype    = ('freetype',      '2.13.2',           '-L http://download.savannah.gnu.org/releases/freetype/freetype-',  '.tar.gz',  '',             'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --disable-shared CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include"')
harfbuzz    = ('harfbuzz',      '8.3.0',            'https://github.com/harfbuzz/harfbuzz',                             'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --disable-shared CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include"')
fribidi     = ('fribidi',       'v1.0.13',          'https://github.com/fribidi/fribidi',                               'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --disable-shared CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include"')
libass      = ('libass',        '0.17.1',           'https://github.com/libass/libass',                                 'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --disable-shared CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include/freetype2 -I/Library/Frameworks/VapourSynth.framework/include/harfbuzz" PKG_CONFIG_PATH=/Library/Frameworks/VapourSynth.framework/lib/pkgconfig')
leptonica   = ('leptonica',     '1.84.1',           'https://github.com/danbloomberg/leptonica',                        'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --disable-shared CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include" LDFLAGS="-L/Library/Frameworks/VapourSynth.framework/lib"')
tesseract   = ('tesseract',     '5.3.3',            'https://github.com/tesseract-ocr/tesseract',                       'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework CPPFLAGS="-I/Library/Frameworks/VapourSynth.framework/include/leptonica" PKG_CONFIG_PATH=/Library/Frameworks/VapourSynth.framework/lib/pkgconfig')
lsmash      = ('l-smash',       'v2.14.5',          'https://github.com/l-smash/l-smash',                               'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --disable-shared')
ffmpeg      = ('ffmpeg',        'n6.1.1',           'https://github.com/ffmpeg/ffmpeg',                                 'git',      '',             'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework --enable-gpl --enable-version3 --enable-shared --disable-static --disable-encoders --disable-programs --disable-filters --disable-doc --disable-avdevice --disable-avfilter --disable-network --disable-postproc')
zimg        = ('zimg',          'release-3.0.5',    'https://github.com/sekrit-twc/zimg',                               'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework')
vapoursynth = ('vapoursynth',   'R65',              'https://github.com/vapoursynth/vapoursynth',                       'git',      './autogen.sh', 'make', 'sudo make install', './configure --prefix=/Library/Frameworks/VapourSynth.framework PYTHON=/Library/Frameworks/VapourSynth.framework/bin/python3 PKG_CONFIG_PATH=/Library/Frameworks/VapourSynth.framework/lib/pkgconfig')

# Define working directory
home = os.path.expanduser('~' + '/')
installs = ('.installs')
full_path = home + installs
python_fw_ver = '3.11' # used to define path to site-packages

# Everything that will be downloaded, compiled and installed. Comment out the parts you want to skip.
def main():
    build(openssl)
    build(xzutils)
    build(zlib)
    build(python)
    build(libjpg)
    build(libpng)
    build(libtiff)
    build(imagemagick)
    build(freetype)
    build(harfbuzz)
    build(fribidi)
    build(libass)
    build(leptonica)
    build(tesseract)
    build(lsmash)
    build(ffmpeg)
    build(zimg)
    build(vapoursynth)

# Creating a working directory
if os.path.exists(full_path) == True:
    print(f'Directory found: {full_path}')
else:
    print(f'Creating directory: {full_path}')
    os.chdir(home)
    os.mkdir(installs)

# Download and extract
def get(app):
    if app[3] == 'git':
        if os.path.exists(app[0]) == False:
            os.system(f'git clone {app[2]}')
        os.chdir(full_path + '/' + app[0])
        os.system(f'git checkout {app[1]}')
        os.chdir(full_path + '/' + app[0])
    else:
        if os.path.exists(f'{app[0]}-{app[1]}{app[3]}') == False:
            os.system(f'curl {app[2]}{app[1]}{app[3]} -o {app[0]}-{app[1]}{app[3]}')
        with tarfile.open(f'{app[0]}-{app[1]}{app[3]}', 'r') as tf:
            tf.extractall('./')
        os.chdir(full_path + '/' + app[0] + '-' + app[1])

# Map functions to index at the top
def autogen(app):
    os.system(app[4])

def configure(app):
    os.system(app[7])

def make(app):
    os.system(app[5])

def install(app):
    os.system(app[6])

# Things to do after install
def check(app):
    if app[0] == 'cpython':
        # Make Python Links
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/bin/pip3 /usr/local/bin/vspip')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/bin/python3 /usr/local/bin/vspython')
        # Install dependencies
        os.system('sudo vspip install cython numpy setuptools wheel sphinx sphinx-intl sphinx-rtd-theme')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/bin/cython /usr/local/bin/cython')
    if app[0] == 'vapoursynth':
        # Create folder
        os.system('sudo mkdir /Library/Frameworks/VapourSynth.framework/lib/vapoursynth')
        # Make links
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/libvapoursynth.dylib /usr/local/lib/libvapoursynth.dylib')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/libvapoursynth-script.dylib /usr/local/lib/libvapoursynth-script.dylib')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/libvapoursynth-script.0.dylib /Library/Frameworks/VapourSynth.framework/lib/libvapoursynth-script.0.dylib')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/vapoursynth /usr/local/lib/vapoursynth')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/pkgconfig/vapoursynth.pc /usr/local/lib/pkgconfig/vapoursynth.pc')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/pkgconfig/vapoursynth-script.pc /usr/local/lib/pkgconfig/vapoursynth-script.pc')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/bin/vspipe /usr/local/bin/vspipe')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/include/vapoursynth /usr/local/include/vapoursynth')
        # Create desktop folders
        os.system('sudo mkdir $HOME/Desktop/VapourSynth')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/bin "$HOME/Desktop/VapourSynth/Add Executables"')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib "$HOME/Desktop/VapourSynth/Add Libraries"')
        os.system('sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/vapoursynth "$HOME/Desktop/VapourSynth/Add Plugins"')
        os.system(f'sudo ln -s /Library/Frameworks/VapourSynth.framework/lib/python{python_fw_ver}/site-packages "$HOME/Desktop/VapourSynth/Add Scripts"')

# Build instructions
def build(app):
    print(f'Setting up {app[0]}')
    os.chdir(full_path)
    get(app)
    autogen(app)
    configure(app)
    make(app)
    install(app)
    check(app)

main()