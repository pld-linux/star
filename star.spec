#
# TODO: use proper CC and CFLAGS

%define ver   1.4
%define alpha  a25

Summary:	A very fast, POSIX compliant tape archiver
Summary(pl):	Szybki, zgodny z POSIX program do archiwizacji
Name:		star
Version:	%{ver}%{alpha}
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.fokus.gmd.de/pub/unix/star/alpha/%{name}-%{version}.tar.gz
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

%description -l pl
Star jest szybkim, zgodnym z POSIX archiwizerem tar. Potrafi czyta� i
zapisywa� archiwa tar zgodne z POSIX, a tak�e nie-posiksowe archiwa
GNU. Star jest pierwsz� wolnodost�pn� implementacj� tara zgodn� z
norm� POSIX.1-200x. Zapisuje ��cznie wiele plik�w na jednej ta�mie
lub dysku i mo�e odtwarza� z archiwum pojedyncze pliki.

Ma kolejk� FIFO (dla przyspieszenia operacji), dopasowywanie wzorc�w,
obs�ug� archiw�w wielocz�ciowych, mo�liwo�� archiwizacji plik�w
rzadkich, automatyczne wykrywanie formatu archiw�w i kolejno�ci bajt�w
w s�owie, automatyczn� kompresj� i dekompresj�, obs�ug� zdalnych
archiw�w oraz dodatkowe mo�liwo�ci umo�liwiaj�ce wykonywanie pe�nych
kopii zapasowych. Ten pakiet zawiera narz�dzia getfacl i setfacl
potrzebne do modyfikacji list kontroli dost�pu (ACL).

Pakiet zawiera te� niezale�ny od platformy serwer rmt, kt�ry ma
zaimplementowane wszystkie rozszerzenia Sun/GNU/Schily/BSD i pozwala
na dost�p klientem rmt z dowolnego systemu operacyjnego.

%prep
%setup -q -n %{name}-%{ver}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INS_BASE=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=/share/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/star
%attr(755,root,root) %{_bindir}/smt
%attr(755,root,root) %{_sbindir}/rmt
%{_mandir}/man1/star.1*
%{_mandir}/man1/rmt.1*
