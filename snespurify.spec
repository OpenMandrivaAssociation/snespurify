%define name	snespurify
%define version 11b1
%define release %mkrel 1

Summary:	A tool to clean up SNES ROMs for compatibility with BSNES
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
URL:		http://byuu.org/
Group:		Emulators
Source0:	%{name}_v%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	qt4-devel

%description
A tool to clean up SNES ROMs for compatibility with BSNES.

With a single tool and a handful of clicks, you can:
- decompress archives
- strip headers
- fix file extensions
- convert IPS patches to the UPS file format

%files
%defattr(-,root,root)
#{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}-qt.desktop
%{_bindir}/%{name}-qt

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}

%build
sed -i "s/g++-4.5/g++/" cc-qt.sh

#use system optflags
sed -i "s/-O3/%{optflags}/" cc-qt.sh

#don't strip the binaries prematurely
sed -i "s/-s //" cc-qt.sh

sh cc-qt.sh

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%__mkdir -p %{buildroot}%{_bindir}
%__mkdir -p %{buildroot}%{_datadir}/applications
#__mkdir -p %{buildroot}%{_datadir}/pixmaps

#install icon
#__install -m 644 data/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

#install binaries
%__install -m 755 %{name}-qt %{buildroot}%{_bindir}/%{name}-qt

#install XDG menu entries
cat > %{buildroot}%{_datadir}/applications/%{name}-qt.desktop << EOF
[Desktop Entry]
Version=1.0
Name=SnesPurify (Qt4)
Comment=SNES ROMs purification utility
Exec=%{name}-qt
Icon=configure
Terminal=false
Type=Application
Categories=Qt;Game;Emulator;
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}



%changelog
* Fri Aug 19 2011 Andrey Bondrov <abondrov@mandriva.org> 11b1-1mdv2012.0
+ Revision: 695274
- imported package snespurify


* Wed Aug 17 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 11b1-1mdv2011.0
- First release for Mandriva