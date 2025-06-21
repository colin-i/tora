# Torrent client

## Install
On Ubuntu from PPA.
```sh
sudo add-apt-repository ppa:colin-i/ppa
```
Or the *manual installation step* from this link *https://gist.github.com/colin-i/e324e85e0438ed71219673fbcc661da6* \
Install:
```sh
sudo apt-get install torra
```
Will also install libgtk-4-1 if is not already installed.\
\
\
On openSUSE, run the following as __root__:\
For openSUSE Tumbleweed:
```sh
zypper addrepo https://download.opensuse.org/repositories/home:costin/openSUSE_Tumbleweed/home:costin.repo
```
For openSUSE Leap:
```sh
zypper addrepo https://download.opensuse.org/repositories/home:costin/openSUSE_Leap_15.6/home:costin.repo
```
And:
```sh
zypper refresh
zypper install python313-torra
```
Replace *python313* with *python312* or *python311* if needed.\
Will also install libgtk-4-1 if is not already installed.\
\
\
On Fedora, run the following as __root__:
```sh
dnf copr enable colin/project
dnf install python3-torra
```
And having gtk4.\
\
\
On Arch Linux, <i>.zst</i> file from [releases](https://github.com/colin-i/irc-ssl/releases). Or:
```sh
yay -Sy python-torra
```
Will also install gtk4 if is not already installed.\
\
\
From [PyPI](https://pypi.org/project/torra):
```sh
pip3 install torra
```
And having gtk4.\
\
\
On other linux distributions with gtk4, <i>.AppImage</i> file from [releases](https://github.com/colin-i/tora/releases).

## From source
Using libtorrent (arvidn) with python bindings.\
More info at setup.pre.py.

## [Info](https://github.com/colin-i/tora/blob/master/info.md)

## Donations
The *donations* section is here
*https://gist.github.com/colin-i/e324e85e0438ed71219673fbcc661da6*
