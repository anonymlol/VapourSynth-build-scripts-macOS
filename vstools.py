#!/usr/bin/env python3
# Setting up tools to build VapourSynth & Plugins

import os
import tarfile

autoconf    = ('autoconf',      '2.71',         'https://ftp.gnu.org/gnu/autoconf/autoconf-',               '.tar.gz',  '',             './configure',                      'make', 'sudo make install')
automake    = ('automake',      '1.16.5',       'https://ftp.gnu.org/gnu/automake/automake-',               '.tar.gz',  '',             './configure',                      'make', 'sudo make install')
libtool     = ('libtool',       '2.4.7',        'https://ftp.wayne.edu/gnu/libtool/libtool-',               '.tar.gz',  '',             './configure',                      'make', 'sudo make install')
pkg_config  = ('pkg-config',    '0.29.2',       'https://pkg-config.freedesktop.org/releases/pkg-config-',  '.tar.gz',  '',             './configure --with-internal-glib', 'make', 'sudo make install')
cmake       = ('cmake',         'v3.27.9',      'https://gitlab.kitware.com/cmake/cmake.git',               'git',      '',             './configure',                      'make', 'sudo make install')
ragel       = ('ragel',         '6.10',         'http://www.colm.net/files/ragel/ragel-',                   '.tar.gz',  '',             './configure',                      'make', 'sudo make install')
nasm        = ('nasm',          'nasm-2.16.01', 'https://github.com/netwide-assembler/nasm',                'git',      './autogen.sh', './configure',                      'make', 'sudo make install')
yasm        = ('yasm',          '1.3.0',        'http://www.tortall.net/projects/yasm/releases/yasm-',      '.tar.gz',  '',             './configure',                      'make', 'sudo make install')

# Define working directory
home = os.path.expanduser('~' + '/')
installs = ('.installs')
full_path = home + installs

# Everything that will be downloaded, compiled and installed. Comment out the parts you want to skip
def main():
    xcode_cmdln()
    build(autoconf)
    build(automake)
    build(libtool)
    build(pkg_config)
    build(cmake)
    build(ragel)
    build(nasm)
    build(yasm)

# Creating a working directory
if os.path.exists(full_path) == True:
    print(f'Directory found: {full_path}')
else:
    print(f'Creating directory: {full_path}')
    os.chdir(home)
    os.mkdir(installs)

# Install Xcode Command Line Tools
def xcode_cmdln():
    os.system('xcode-select --install')

def build(app):
    print(f'Settings up {app[0]}')
    os.chdir(full_path)
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
    os.system(f'{app[4]}') # autogen (if defined)
    os.system(f'{app[5]}') # configure
    os.system(f'{app[6]}') # make
    os.system(f'{app[7]}') # sudo make install

main()