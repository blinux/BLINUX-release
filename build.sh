#!/bin/sh

rpmbuild -bb BLINUX-release.spec | tee build.log
rpmlint --info `grep "Wrote: " build.log | awk '{print $2}'`
