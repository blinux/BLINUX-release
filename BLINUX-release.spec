#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

%define product BLINUX

Name:           BLINUX-release
License:        BSD-2-Clause
Group:          System/Fhs
Version:        3.0
Release:        0
Provides:       aaa_version distribution-release
Provides:       suse-release-oss = %{version}-%{release}
Provides:       suse-release = %{version}-%{release}
Conflicts:      openSUSE-release

Provides:       %name-%version
Provides:       product()
Provides:       product(BLINUX) = %version-%release
Requires:       product_flavor(BLINUX)
Requires:	branding-BLINUX
Requires:	patterns-BLINUX

BuildArch:	noarch
AutoReqProv:    on
Summary:        BLINUX
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr
Vendor:		Blinux

%define codename Daiquiri Doritos

%description
BLINUX is a branding of the openSUSE distribution.

%prep

%build

%install
mkdir -p %{buildroot}/etc
echo -e 'Welcome to %{product} %{version} "%{codename}" - Kernel \\r (\\l).\n\n' > %{buildroot}/etc/issue
echo 'Welcome to %{product} %{version} "%{codename}" - Kernel %%r (%%t).' > %{buildroot}/etc/issue.net

if [ `hostname` = 'exam' ]; then
    echo "%{product} %{version} EXAM" > %{buildroot}/etc/SuSE-release
else
    echo "%{product} %{version} STD" > %{buildroot}/etc/SuSE-release
fi
echo VERSION = %{version} >> %{buildroot}/etc/SuSE-release
echo CODENAME = %{codename} >> %{buildroot}/etc/SuSE-release
echo "# /etc/SuSE-release is deprecated and will be removed in the future, use /etc/os-release instead" >> %{buildroot}/etc/SuSE-release

if [ `hostname` = 'exam' ]; then
    echo NAME=\"BLINUX EXAM\" > %{buildroot}/etc/os-release
else
    echo NAME=\"BLINUX STD\" > %{buildroot}/etc/os-release
fi
echo VERSION=\""%{version} (%{codename})"\" >> %{buildroot}/etc/os-release
echo VERSION_ID=\"`echo %{version}|tr '[:upper:]' '[:lower:]'`\"|sed -e 's/ //g;' >> %{buildroot}/etc/os-release
echo PRETTY_NAME=\"BLINUX %{version} "(%{codename})\""  >> %{buildroot}/etc/os-release
echo ID=blinux >> %{buildroot}/etc/os-release
echo ANSI_COLOR=\"0\;32\" >> %{buildroot}/etc/os-release
echo CPE_NAME=\"cpe:/o:blinux:blinux:%{version}\" >> %{buildroot}/etc/os-release
echo 'BUG_REPORT_URL="http://intra.bocal.org"' >> %{buildroot}/etc/os-release
echo 'HOME_URL="http://www.blinux.fr/"' >> %{buildroot}/etc/os-release
echo 'ID_LIKE="suse"' >> %{buildroot}/etc/os-release

echo "Have a lot of fun..." > %{buildroot}/etc/motd

%post
echo -e 'Welcome to %{product} %{version} "%{codename}" - Kernel \\r (\\l).\n\n' > /etc/issue
echo 'Welcome to %{product} %{version} "%{codename}" - Kernel %%r (%%t).' > /etc/issue.net

if [ `hostname` = 'exam' ]; then
    echo "%{product} %{version} EXAM" > /etc/SuSE-release
else
    echo "%{product} %{version} STD" > /etc/SuSE-release
fi
echo VERSION = %{version} >> /etc/SuSE-release
echo CODENAME = %{codename} >> /etc/SuSE-release
echo "# /etc/SuSE-release is deprecated and will be removed in the future, use /etc/os-release instead" >> /etc/SuSE-release

if [ `hostname` = 'exam' ]; then
    echo NAME=\"BLINUX EXAM\" > /etc/os-release
else
    echo NAME=\"BLINUX STD\" > /etc/os-release
fi
echo VERSION=\""%{version} (%{codename})"\" >> /etc/os-release
echo VERSION_ID=\"`echo %{version}|tr '[:upper:]' '[:lower:]'`\"|sed -e 's/ //g;' >> /etc/os-release
echo PRETTY_NAME=\"BLINUX %{version} "(%{codename})\""  >> /etc/os-release
echo ID=blinux >> /etc/os-release
echo ANSI_COLOR=\"0\;32\" >> /etc/os-release
echo CPE_NAME=\"cpe:/o:blinux:blinux:%{version}\" >> /etc/os-release
echo 'BUG_REPORT_URL="http://intra.bocal.org"' >> /etc/os-release
echo 'HOME_URL="http://www.blinux.fr/"' >> /etc/os-release
echo 'ID_LIKE="suse"' >> /etc/os-release

echo "Have a lot of fun..." > /etc/motd

%files
%defattr(644,root,root,755)
%config /etc/SuSE-release
%config /etc/os-release
%config(noreplace) /etc/motd
%config(noreplace) /etc/issue
%config(noreplace) /etc/issue.net

%changelog
* Mon Aug 03 2015 Emmanuel Vadot <elbarto@bocal.org> - 3.0
- Update to 3.0

* Thu Aug 07 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0
- Package creation
