%define ver   1.4
%define alpha  a24

Summary:	A very fast, POSIX compliant tape archiver
Name:		star
Version:	%{ver}%{alpha}
Release:	1
Source0:	ftp://ftp.fokus.gmd.de/pub/unix/star/alpha/%{name}-%{version}.tar.gz
License:	GPL
Group:		System Environment/Base
URL:		http://www.fokus.gmd.de/research/cc/glone/employees/joerg.schilling/private/star.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Star is a very fast, POSIX-compliant tar archiver. It reads and writes
POSIX compliant tar archives as well as non-POSIX GNU tar archives.
Star is the first free POSIX.1-200x compliant tar implementation. It
saves many files together into a single tape or disk archive, and can
restore individual files from the archive.

It includes a FIFO for speed, a pattern matcher, multivolume support,
the ability to archive sparse files, automatic archive format
detection, automatic byte order recognition, automatic archive
compression / decompression, remote archives, and special features
that allow star to be used for full backups. This package contains the
getfacl and setfacl utilities needed for manipulating access control
lists.

It includes the only known platform independant "rmt" server program
that hides Linux incompatibilities. The "rmt" server from the star
package implements all Sun/GNU/Schily/BSD enhancements and allows any
"rmt" client from any OS to contact any OS as server.


%prep
%setup -q -n %{name}-%{ver}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install INS_BASE=$RPM_BUILD_ROOT/usr MANDIR=%{_mandir}

%files
%defattr(644,root,root,755)
%{_bindir}/star
%{_bindir}/smt
%{_sbindir}/rmt
%{_mandir}/man1/star.1
%{_mandir}/man1/rmt.1

%clean
rm -rf $RPM_BUILD_ROOT
