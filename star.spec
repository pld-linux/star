Summary:	A very fast, POSIX compliant tape archiver
Summary(pl):	Szybki, zgodny z POSIX program do archiwizacji
Name:		star
Version:	1.5
%define	bver	a37
Release:	0.%{bver}.1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.berlios.de/pub/star/alpha/%{name}-%{version}%{bver}.tar.bz2
# Source0-md5:	110ecfad6e61ac5c2397b4eb2f721cd3
# based on http://www.nsa.gov/selinux/patches/star-selinux.patch.gz
Patch0:		%{name}-selinux.patch
Patch1:		%{name}-no-kernel-headers.patch
Patch2:		%{name}-strtod.patch
URL:		http://www.fokus.gmd.de/research/cc/glone/employees/joerg.schilling/private/star.html
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	libselinux-devel
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

%description -l pl
Star jest szybkim, zgodnym z POSIX archiwizerem tar. Potrafi czytaæ i
zapisywaæ archiwa tar zgodne z POSIX, a tak¿e nie-posiksowe archiwa
GNU. Star jest pierwsz± wolnodostêpn± implementacj± tara zgodn± z
norm± POSIX.1-200x. Zapisuje ³±cznie wiele plików na jednej ta¶mie lub
dysku i mo¿e odtwarzaæ z archiwum pojedyncze pliki.

Ma kolejkê FIFO (dla przyspieszenia operacji), dopasowywanie wzorców,
obs³ugê archiwów wieloczê¶ciowych, mo¿liwo¶æ archiwizacji plików
rzadkich, automatyczne wykrywanie formatu archiwów i kolejno¶ci bajtów
w s³owie, automatyczn± kompresjê i dekompresjê, obs³ugê zdalnych
archiwów oraz dodatkowe mo¿liwo¶ci umo¿liwiaj±ce wykonywanie pe³nych
kopii zapasowych. Ten pakiet zawiera narzêdzia getfacl i setfacl
potrzebne do modyfikacji list kontroli dostêpu (ACL).

Pakiet zawiera te¿ niezale¿ny od platformy serwer rmt, który ma
zaimplementowane wszystkie rozszerzenia Sun/GNU/Schily/BSD i pozwala
na dostêp klientem rmt z dowolnego systemu operacyjnego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# new ac doesn't like comments in the same line as #undef
%{__perl} -pi -e 's@/\*.*\*/@@g' conf/xconfig.h.in

%build
cd conf
%{__autoconf}
cd ..
%{__make} \
	COPTOPT="%{rpmcflags}" \
	CC="%{__cc}" \
	LDCC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INS_BASE=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=/share/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.linux Changelog TODO
%attr(755,root,root) %{_bindir}/spax
%attr(755,root,root) %{_bindir}/star
%attr(755,root,root) %{_bindir}/ustar
%attr(755,root,root) %{_bindir}/smt
%attr(755,root,root) %{_sbindir}/rmt
%{_mandir}/man1/star.1*
%{_mandir}/man1/rmt.1*
%{_mandir}/man5/star.5*
