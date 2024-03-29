#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : GConf
Version  : 3.2.6
Release  : 18
URL      : https://download.gnome.org/sources/GConf/3.2/GConf-3.2.6.tar.xz
Source0  : https://download.gnome.org/sources/GConf/3.2/GConf-3.2.6.tar.xz
Summary  : GNOME Config System.
Group    : Development/Tools
License  : LGPL-2.0
Requires: GConf-bin = %{version}-%{release}
Requires: GConf-data = %{version}-%{release}
Requires: GConf-lib = %{version}-%{release}
Requires: GConf-libexec = %{version}-%{release}
Requires: GConf-license = %{version}-%{release}
Requires: GConf-locales = %{version}-%{release}
Requires: GConf-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : gtk-doc
BuildRequires : intltool
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libxml-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GConf is a configuration database system, functionally similar to the
Windows registry but lots better. :-) It's being written for the GNOME
desktop but does not require GNOME; configure should notice if GNOME
is not installed and compile the basic GConf library anyway.

%package bin
Summary: bin components for the GConf package.
Group: Binaries
Requires: GConf-data = %{version}-%{release}
Requires: GConf-libexec = %{version}-%{release}
Requires: GConf-license = %{version}-%{release}

%description bin
bin components for the GConf package.


%package data
Summary: data components for the GConf package.
Group: Data

%description data
data components for the GConf package.


%package dev
Summary: dev components for the GConf package.
Group: Development
Requires: GConf-lib = %{version}-%{release}
Requires: GConf-bin = %{version}-%{release}
Requires: GConf-data = %{version}-%{release}
Provides: GConf-devel = %{version}-%{release}
Requires: GConf = %{version}-%{release}

%description dev
dev components for the GConf package.


%package doc
Summary: doc components for the GConf package.
Group: Documentation
Requires: GConf-man = %{version}-%{release}

%description doc
doc components for the GConf package.


%package lib
Summary: lib components for the GConf package.
Group: Libraries
Requires: GConf-data = %{version}-%{release}
Requires: GConf-libexec = %{version}-%{release}
Requires: GConf-license = %{version}-%{release}

%description lib
lib components for the GConf package.


%package libexec
Summary: libexec components for the GConf package.
Group: Default
Requires: GConf-license = %{version}-%{release}

%description libexec
libexec components for the GConf package.


%package license
Summary: license components for the GConf package.
Group: Default

%description license
license components for the GConf package.


%package locales
Summary: locales components for the GConf package.
Group: Default

%description locales
locales components for the GConf package.


%package man
Summary: man components for the GConf package.
Group: Default

%description man
man components for the GConf package.


%prep
%setup -q -n GConf-3.2.6
cd %{_builddir}/GConf-3.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680023059
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --disable-orbit \
--sysconfdir=/usr/share/defaults/etc \
--disable-gtk
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1680023059
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/GConf
cp %{_builddir}/GConf-%{version}/COPYING %{buildroot}/usr/share/package-licenses/GConf/5fb362ef1680e635fe5fb212b55eef4db9ead48f || :
%make_install
%find_lang GConf2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gconf-merge-tree
/usr/bin/gconftool-2
/usr/bin/gsettings-data-convert
/usr/bin/gsettings-schema-convert

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GConf-2.0.typelib
/usr/share/dbus-1/services/org.gnome.GConf.service
/usr/share/defaults/etc/gconf/2/path
/usr/share/defaults/etc/xdg/autostart/gsettings-data-convert.desktop
/usr/share/gir-1.0/*.gir
/usr/share/sgml/gconf/gconf-1.0.dtd

%files dev
%defattr(-,root,root,-)
/usr/include/gconf/2/gconf/gconf-changeset.h
/usr/include/gconf/2/gconf/gconf-client.h
/usr/include/gconf/2/gconf/gconf-engine.h
/usr/include/gconf/2/gconf/gconf-enum-types.h
/usr/include/gconf/2/gconf/gconf-error.h
/usr/include/gconf/2/gconf/gconf-listeners.h
/usr/include/gconf/2/gconf/gconf-schema.h
/usr/include/gconf/2/gconf/gconf-value.h
/usr/include/gconf/2/gconf/gconf.h
/usr/lib64/libgconf-2.so
/usr/lib64/pkgconfig/gconf-2.0.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gconf/ch01.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-backend.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-changeset.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-client.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-engine.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-error.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-internals.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-listeners.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-locale.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-schema.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-sources.html
/usr/share/gtk-doc/html/gconf/gconf-gconf-value.html
/usr/share/gtk-doc/html/gconf/gconf-gconf.html
/usr/share/gtk-doc/html/gconf/gconf.devhelp2
/usr/share/gtk-doc/html/gconf/home.png
/usr/share/gtk-doc/html/gconf/index.html
/usr/share/gtk-doc/html/gconf/index.sgml
/usr/share/gtk-doc/html/gconf/left.png
/usr/share/gtk-doc/html/gconf/right.png
/usr/share/gtk-doc/html/gconf/style.css
/usr/share/gtk-doc/html/gconf/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/GConf/2/libgconfbackend-oldxml.so
/usr/lib64/GConf/2/libgconfbackend-xml.so
/usr/lib64/gio/modules/libgsettingsgconfbackend.so
/usr/lib64/libgconf-2.so.4
/usr/lib64/libgconf-2.so.4.1.5

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gconfd-2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/GConf/5fb362ef1680e635fe5fb212b55eef4db9ead48f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gconftool-2.1
/usr/share/man/man1/gsettings-data-convert.1
/usr/share/man/man1/gsettings-schema-convert.1

%files locales -f GConf2.lang
%defattr(-,root,root,-)

