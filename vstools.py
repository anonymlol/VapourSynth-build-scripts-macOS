#!/usr/bin/env python3
import os
import tarfile

# Define versions
autoconf_version    = '2.71'
automake_version    = '1.16.5'
libtool_version     = '2.4.7'
pkg_config_version  = '0.29.2'
cmake_version       = '3.27.9'
ragel_version       = '6.10'
nasm_version        = '2.16.01'
yasm_version        = '1.3.0'

# Define working directory
home = os.path.expanduser('~' + '/')
installs = ('.installs')
full_path = home + installs

# Creating a working directory
if os.path.exists(full_path) == True:
    print(f'Directory found: {full_path}')
else:
    print(f'Creating directory: {full_path}')
    os.chdir(home)
    os.mkdir(installs)

# Everything that will be downloaded, compiled and installed. Comment out the parts you want to skip
def main():
    xcode_cmd_line_tools()
    autoconf(autoconf_version)
    automake(automake_version)
    libtool(libtool_version)
    pkg_config(pkg_config_version)
    cmake(cmake_version)
    ragel(ragel_version)
    nasm(nasm_version)
    yasm(yasm_version)

# Install Xcode Command Line Tools
def xcode_cmd_line_tools():
    os.system('xcode-select --install')

# Setup Autoconf
def autoconf(version):
    print('Setting up Autoconf...')
    os.chdir(full_path)
    if os.path.exists(f'autoconf-{version}.tar.gz') == False:
        os.system(f'curl https://ftp.gnu.org/gnu/autoconf/autoconf-{version}.tar.gz -o autoconf-{version}.tar.gz')
    with tarfile.open(f'autoconf-{version}.tar.gz', 'r') as tf:
        tf.extractall('./')
    os.chdir(full_path + f'/autoconf-{version}')
    print('.configure')
    os.system('./configure')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

# Setup Automake
def automake(version):
    print('Setting up Automake...')
    os.chdir(full_path)
    if os.path.exists(f'automake-{version}.tar.gz') == False:
        os.system(f'curl https://ftp.gnu.org/gnu/automake/automake-{version}.tar.gz -o automake-{version}.tar.gz')
    with tarfile.open(f'automake-{version}.tar.gz', 'r') as tf:
        tf.extractall('./')
    os.chdir(full_path + f'/automake-{version}')
    print('./configure')
    os.system('./configure')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

# Setup Libtool
def libtool(version):
    print('Setting up Libtool...')
    os.chdir(full_path)
    if os.path.exists(f'libtool-{version}.tar.gz') == False:
        os.system(f'curl https://ftp.wayne.edu/gnu/libtool/libtool-{version}.tar.gz -o libtool-{version}.tar.gz')
    with tarfile.open(f'libtool-{version}.tar.gz', 'r') as tf:
        tf.extractall('./')
    os.chdir(full_path + f'/libtool-{version}')
    print('./configure')
    os.system('./configure')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

# Setup pkg-config
def pkg_config(version):
    print('Setting up pkg-config...')
    os.chdir(full_path)
    if os.path.exists(f'pkg-config-{version}.tar.gz') == False:
        os.system(f'curl https://pkg-config.freedesktop.org/releases/pkg-config-{version}.tar.gz -o pkg-config-{version}.tar.gz')
    with tarfile.open(f'pkg-config-{version}.tar.gz', 'r') as tf:
        tf.extractall('./')
    os.chdir(full_path + f'/pkg-config-{version}')
    print('./configure --with-internal-glib')
    os.system('./configure --with-internal-glib')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

# Setup CMake
def cmake(version):
    print('Setting up cmake...')
    os.chdir(full_path)
    if os.path.exists('cmake') == False:
        os.system('git clone https://gitlab.kitware.com/cmake/cmake.git')
    os.chdir(full_path + '/cmake')
    os.system(f'git checkout v{version}')
    print('./configure')
    os.system('./configure')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

# Setup ragel
def ragel(version):
    print('Setting up ragel...')
    os.chdir(full_path)
    if os.path.exists(f'ragel-{version}.tar.gz') == False:
        os.system(f'curl http://www.colm.net/files/ragel/ragel-{version}.tar.gz -o ragel-{version}.tar.gz')
    with tarfile.open(f'ragel-{version}.tar.gz', 'r') as tf:
        tf.extractall('./')
    os.chdir(full_path + f'/ragel-{version}')
    print('./configure')
    os.system('./configure')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

# Setup NASM
def nasm(version):
    print('Setting up nasm...')
    os.chdir(full_path)
    if os.path.exists('nasm') == False:
        os.system('git clone https://github.com/netwide-assembler/nasm')
    os.chdir(full_path + '/nasm')
    os.system(f'git checkout nasm-{version}')
    print('./autogen.sh')
    os.system('./autogen.sh')
    print('./configure')
    os.system('./configure')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

# Setup YASM
def yasm(version):
    print('Setting up yasm...')
    os.chdir(full_path)
    if os.path.exists(f'yasm-{version}.tar.gz') == False:
        os.system(f'curl http://www.tortall.net/projects/yasm/releases/yasm-{version}.tar.gz -o yasm-{version}.tar.gz')
    with tarfile.open(f'yasm-{version}.tar.gz', 'r') as tf:
        tf.extractall('./')
    os.chdir(full_path + f'/yasm-{version}')
    print('./configure')
    os.system('./configure')
    print('make')
    os.system('make')
    print('sudo make install')
    os.system('sudo make install')

main()