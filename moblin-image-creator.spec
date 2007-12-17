%define name moblin-image-creator
%define version 0.1
%define git 20070723
%define release %mkrel 0.%{git}.2
%define distname %{name}-%{git}

Summary: Mobile & Internet Linux Development Kit
Name: %{name}
Version: %{version}
Release: %{release}
# git clone http://www.moblin.org/repos/tools/moblin-image-creator.git
# git archive --format=tar --prefix=moblin-image-creator-$(date +%Y%m%d)/ master | bzip2 > moblin-image-creator-$(date +%Y%m%d).tar.bz2
Source0: %{distname}.tar.bz2
License: GPL
Group: Development/Other
Url: http://www.moblin.org/
BuildArch: noarch
Requires: debootstrap dosfstools

%description
Moblin Image Creator is a tool aimed at making life easier for the
mobile and embedded developer. The tool is designed to be extremely
flexible with platform-specific knowledge isolated to a platform
definition. Initial focus is on a new class of devices known as Mobile
Internet Devices (MIDs), but the design of Moblin Image Creator is not
MID-specific and talk is already underway to add new platform
definitions to build consumer electronics stacks, such as TV set-top
boxes.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf %{buildroot}
# do not run tests here, they require write access to _datadir
%make basicinstall DESTDIR=%{buildroot}
rm -f %{buildroot}%{_datadir}/pdk/COPYING

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/image-creator
%{_datadir}/pdk
%{_datadir}/applications/image-creator.desktop
%{_sysconfdir}/bash_completion.d/image-creator-completion.bash
