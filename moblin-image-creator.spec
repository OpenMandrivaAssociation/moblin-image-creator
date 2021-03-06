%define name moblin-image-creator
%define version 0.1
%define git 20070723
%define release %mkrel 0.%{git}.4
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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-0.20070723.4mdv2011.0
+ Revision: 620378
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-0.20070723.3mdv2010.0
+ Revision: 430083
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1-0.20070723.2mdv2009.0
+ Revision: 136602
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 02 2007 Olivier Blin <oblin@mandriva.com> 0.1-0.20070723.2mdv2008.0
+ Revision: 58235
- require dosfstools for mkfs.vfat

* Mon Jul 23 2007 Olivier Blin <oblin@mandriva.com> 0.1-0.20070723.1mdv2008.0
+ Revision: 54669
- initial moblin-image-creator package
- Create moblin-image-creator

