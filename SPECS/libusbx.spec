Summary:        Library for accessing USB devices
Name:           libusbx
Version:        1.0.22
Release:        1%{?dist}
# upstream libusbx has merged back with libusb and is now called libusb again
# but we already have a libusb package for the old libusb-compat-0.1, renaming
# that to libusb-compat while at the same time giving this its name is a bit
# tricky, lets stick with the libusbx name for now
Source0:        https://github.com/libusb/libusb/archive/v%{version}/libusb-%{version}.tar.gz
License:        LGPLv2+
Group:          System Environment/Libraries
URL:            http://libusb.info
BuildRequires:  systemd-devel doxygen libtool
Provides:       libusb1 = %{version}-%{release}
Obsoletes:      libusb1 <= 1.0.9

%description
This package provides a way for applications to access USB devices.

Libusbx is a fork of the original libusb, which is a fully API and ABI
compatible drop in for the libusb-1.0.9 release. The libusbx fork was
started by most of the libusb-1.0 developers, after the original libusb
project did not produce a new release for over 18 months.

Note that this library is not compatible with the original libusb-0.1 series,
if you need libusb-0.1 compatibility install the libusb package.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusb1-devel = %{version}-%{release}
Obsoletes:      libusb1-devel <= 1.0.9

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package devel-doc
Summary:        Development files for %{name}
Group:          Development/Libraries
Provides:       libusb1-devel-doc = %{version}-%{release}
Obsoletes:      libusb1-devel-doc <= 1.0.9
BuildArch:      noarch

%description devel-doc
This package contains API documentation for %{name}.


%prep
%setup -q -n libusb-%{version}
mkdir -p m4
autoreconf -ivf


%build
%configure --disable-static --enable-examples-build
make %{?_smp_mflags}
pushd doc
make docs
popd


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libusb-1.0.pc

%files devel-doc
%doc doc/html examples/*.c


%changelog
* Wed Aug 22 2018 Victor Toso <victortoso@redhat.com> - 1.0.22-1
- Update to 1.0.22
- Resolves: rhbz#1620092

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.21-5
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.21-1
- Update to the final 1.0.21 upstream release

* Wed Aug 10 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.21-0.2.rc2
- Update to 1.0.21-rc2 upstream release
- Add a bunch of locking fixes which are pending upstream

* Tue Feb 23 2016 Hans de Goede <hdegoede@redhat.com> - 1.0.21-0.1.git448584a
- Update to a pre 1.0.21 git snapshot to bring in libusb_interrupt_event_handler
  which chromium needs (rhbz#1270324)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Hans de Goede <hdegoede@redhat.com> - 1.0.20-1
- Update to 1.0.20 (rhbz#1262817)

* Tue Jun 16 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.19-3
- Use %%license

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.19-1
- Update to 1.0.19 final

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.19-0.2.rc2
- Update to 1.0.19-rc2

* Mon May 19 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.19-0.1.rc1
- Update to 1.0.19-rc1

* Sat Mar  8 2014 Hans de Goede <hdegoede@redhat.com> - 1.0.18-1
- Update to 1.0.18 release (rhbz#1058000)

* Fri Sep  6 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.17-1
- Update to 1.0.17 final release

* Wed Aug 28 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.17-0.1.rc1
- New upstream 1.0.17-rc1 release

* Tue Jul 30 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.16-3
- Fix another libusb_exit deadlock (rhbz#985484)

* Fri Jul 19 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.16-2
- Fix libusb_exit sometimes (race) deadlocking on exit (rhbz#985484)

* Thu Jul 11 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.16-1
- New upstream 1.0.16 final release

* Sat Jul  6 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.16-0.2.rc3
- New upstream 1.0.16-rc3 release

* Mon Jul  1 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.16-0.1.rc2
- New upstream 1.0.16-rc2 release

* Fri Apr 19 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.15-2
- Replace tarbal with upstream re-spun tarbal which fixes line-ending and
  permission issues

* Wed Apr 17 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.15-1
- Upgrade to 1.0.15 (rhbz#952575)

* Tue Apr  2 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.14-3
- Drop devel-doc Requires from the devel package (rhbz#947297)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.14-1
- Upgrade to 1.0.14

* Mon Sep 24 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.13-1
- Upgrade to 1.0.13

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.11-2
- Fix URL to actually point to libusbx
- Improve description to explain the relation between libusbx and libusb
- Build the examples (to test linking, they are not packaged)

* Tue May 22 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.11-1
- New libusbx package, replacing libusb1
- Switching to libusbx upstream as that actually does releases (hurray)
- Drop all patches (all upstream)
- Drop -static subpackage (there are no packages using it)
