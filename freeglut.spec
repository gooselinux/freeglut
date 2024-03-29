Summary:        A freely licensed alternative to the GLUT library
Name:           freeglut
Version:        2.6.0
Release:        1%{?dist}
URL:            http://freeglut.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# For the manpages
Source1:        http://downloads.sourceforge.net/openglut/openglut-0.6.3-doc.tar.gz
License:        MIT
Group:          System Environment/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  pkgconfig libGLU-devel libXext-devel libXxf86vm-devel
BuildRequires:  libXi-devel libICE-devel
# The virtual Provides below is present so that this freeglut package is a
# drop in binary replacement for "glut" which will satisfy rpm dependancies
# properly.  The Obsoletes tag is required in order for any pre-existing
# "glut" package to be removed and replaced with freeglut when upgrading to
# freeglut.  Note: This package will NOT co-exist with the glut package.
Provides:       glut = 3.7
Obsoletes:      glut < 3.7

%description
freeglut is a completely open source alternative to the OpenGL Utility Toolkit
(GLUT) library with an OSI approved free software license. GLUT was originally
written by Mark Kilgard to support the sample programs in the second edition
OpenGL 'RedBook'. Since then, GLUT has been used in a wide variety of practical
applications because it is simple, universally available and highly portable.

freeglut allows the user to create and manage windows containing OpenGL
contexts on a wide range of platforms and also read the mouse, keyboard and
joystick functions.


%package devel
Summary:        Freeglut developmental libraries and header files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libGL-devel libGLU-devel
Provides:       glut-devel = 3.7
Obsoletes:      glut-devel < 3.7

%description devel
Developmental libraries and header files required for developing or compiling
software which links to the freeglut library, which is an open source
alternative to the popular GLUT library, with an OSI approved free software
license.


%prep
%setup -q -a 1


%build
# --disable-warnings -> don't add -Werror to CFLAGS
%configure --disable-static --disable-warnings
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/%{_libdir}/*.la

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man3
install -p -m 644 doc/man/*.3 $RPM_BUILD_ROOT/%{_mandir}/man3


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO doc/*.png doc/*.html
# don't include contents of doc/ directory as it is mostly obsolete
%{_libdir}/libglut*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/GL/*.h
%{_libdir}/libglut.so
%{_mandir}/man3/*


%changelog
* Sat Nov 28 2009 Tomas Smetana <tsmetana@redhat.com> 2.6.0-1
- update to 2.6.0 final

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Hans de Goede <hdegoede@redhat.com> 2.6.0-0.1.rc1
- New upstream release (yes really!) 2.6.0-rc1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Tomas Smetana <tsmetana@redhat.com> - 2.4.0-15
- fix #481049 - rebuild to pick up %%{_isa} provides

* Mon Mar 17 2008 Jesse Keating <jkeating@redhat.com> - 2.4.0-14
- Prevent package from obsoleting itself with matching Provides/Obsoletes.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4.0-13
- Autorebuild for GCC 4.3

* Tue Dec 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.0-12
- Add manpages to the -devel package (from openglut, bz 409651)

* Sun Mar 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 2.4.0-11
- Minor specfile cleanups
- Add a patch from gentoo to stop flightgear from crashing

* Mon Aug 27 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.4.0-10
- Rebuild for FC6

* Wed Jul 26 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.4.0-9
- disblaed static build
- dropped unneeded requires
- dropped the glib cruff passed to make

* Wed Jul 26 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.4.0-8
- clean ups to shut rpmlint up

* Fri Jul 21 2006 Mike A. Harris <mharris@redhat.com> - 2.4.0-7.fc6
- Use {?dist} tag in release field
- Update BuildRoot to comply with Fedora packaging guidelines

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 2.4.0-6
- rebuild
- Try to build w/out glib

* Fri May 19 2006 Mike A. Harris <mharris@redhat.com> 2.4.0-5
- Added "BuildRequires: libXext-devel, libXxf86vm-devel" for (#192255)

* Tue Feb 21 2006 Karsten Hopp <karsten@redhat.de> 2.4.0-4
- BuildRequires: libGLU-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 2.4.0-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 2.4.0-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Mike A. Harris <mharris@redhat.com> 2.4.0-3
- Added "Requires: libGL-devel libGLU-devel" to fix bug (#179464)
- Change file based GL header build dep to BuildRequires: libGL-devel

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> 2.4.0-2.1
- rebuilt

* Fri Nov 18 2005 Bill Nottingham <notting@redhat.com> 2.4.0-2
- Remove references to obsolete /usr/X11R6 paths

* Fri Sep 23 2005 Mike A. Harris <mharris@redhat.com> 2.4.0-1
- Updated to freeglut-2.4.0
- Removed unneeded patches:
  - freeglut-2.2.0-gcc4-fix-invalid-lvalue-in-assignment-cvsps-392-393.patch
- Use "-p /sbin/ldconfig" in post/postun scripts instead of a separate script.

* Sat Mar 05 2005 Mike A. Harris <mharris@redhat.com> 2.2.0-16
- Added freeglut-2.2.0-gcc4-fix-invalid-lvalue-in-assignment-cvsps-392-393.patch
  to fix "invalid lvalue in assignment" bugs reported by gcc 4
- Added "-Wall" to CFLAGS in specfile.

* Thu Mar 03 2005 Mike A. Harris <mharris@redhat.com> 2.2.0-15
- Rebuild with gcc 4 for FC4 development

* Sat Aug 14 2004 Mike A. Harris <mharris@redhat.com> 2.2.0-14
- Add post and postun scripts that call ldconfig (#128413)

* Fri Jun 18 2004 Mike A. Harris <mharris@redhat.com> 2.2.0-13
- Rebuilt with gcc 3.4 for FC3 development

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 2.2.0-12
- rebuilt

* Thu Mar 18 2004 Mike A. Harris <mharris@redhat.com> 2.2.0-11
- Updated "Obsoletes: glut" to be "Obsoletes: glut <= 3.7" and
  "Obsoletes: glut-devel" to be "Obsoletes: glut-devel <= 3.7" as per
  suggestion from Matthias Saou in comment #14 of bug (#107228)

* Sun Mar 07 2004 Mike A. Harris <mharris@redhat.com>
- Made "glut-devel" virtual provides be "glut-devel = 3.7"

* Sun Mar 07 2004 Mike A. Harris <mharris@redhat.com> 2.2.0-10
- Initial Red Hat packaging created by taking the ATrpms src.rpm package from
  http://tinyurl.com/2goog as suggested in bugzilla bug (#107228)
- Bumped the Release field to "10" so our package is newer when people
  upgrade to it, as requested in bug (#107228)
- Removed redundant version/release macros from top of specfile
- Versioned buildroot directory
- Add --enable-warnings arg to ./configure script
- Add HTML documentation to main package
- Made "glut" virtual provides be "glut = 3.7"
- Do not include *.la files

* Sat Feb 21 2004 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 2.2.0
- Added glut compatibility provides.
- Moved *.so to devel package.

* Tue Jan 13 2004 Andy Piper <andy.piper@freeuk.com>
- updated to freeglut-2.2.0
- fixed library install

* Fri Nov 14 2003 Andy Piper <andy.piper@freeuk.com>
- updated for freeglut-2.0.1

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 03 2003 Mike A. Harris <mharris@www.linux.org.uk> 1.3-0.20020125.3
- Add BuildRequires on /sbin/ldconfig
- Change ldconfig call to explicit /sbin/ldconfig

* Sun Jun 01 2003 Mike A. Harris <mharris@www.linux.org.uk> 1.3-0.20020125.2
- Oddly, when I build this on my workstation, it only builds static libs, but
  when I build it in the buildsystem it builds shared and static libs.  Must
  be a twilight zone thing going on.  Add shared libs to file lists.

* Sat May 31 2003 Mike A. Harris <mharris@www.linux.org.uk> 1.3-0.20020125.1
- Added -L/usr/X11R6/%%{_lib} configure script invocation and CFLAGS so lib64
  is treated properly on x86_64/ppc64/s390x architectures
  
* Fri May 30 2003 Mike A. Harris <mharris@www.linux.org.uk> 1.3-0.20020125.0
- Initial build.
