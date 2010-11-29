#
# Conditional build:
%bcond_without	selinux	# disable SELinux support
#
Summary:	A very fast, POSIX compliant tape archiver
Summary(pl.UTF-8):	Szybki, zgodny z POSIX program do archiwizacji
Name:		star
Version:	1.5.1
Release:	2
License:	CDDL v1.0
Group:		Applications/File
Source0:	ftp://ftp.berlios.de/pub/star/%{name}-%{version}.tar.bz2
# Source0-md5:	f9a28f83702624c4c08ef1a343014c7a
# based on http://www.nsa.gov/selinux/patches/star-selinux.patch.gz
Patch0:		%{name}-selinux.patch
Patch1:		%{name}-ac26.patch
Patch2:		%{name}-strtod.patch
URL:		http://cdrecord.berlios.de/old/private/star.html
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	perl-base
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

%description -l pl.UTF-8
Star jest szybkim, zgodnym z POSIX archiwizerem tar. Potrafi czytać i
zapisywać archiwa tar zgodne z POSIX, a także nie-posiksowe archiwa
GNU. Star jest pierwszą wolnodostępną implementacją tara zgodną z
normą POSIX.1-200x. Zapisuje łącznie wiele plików na jednej taśmie lub
dysku i może odtwarzać z archiwum pojedyncze pliki.

Ma kolejkę FIFO (dla przyspieszenia operacji), dopasowywanie wzorców,
obsługę archiwów wieloczęściowych, możliwość archiwizacji plików
rzadkich, automatyczne wykrywanie formatu archiwów i kolejności bajtów
w słowie, automatyczną kompresję i dekompresję, obsługę zdalnych
archiwów oraz dodatkowe możliwości umożliwiające wykonywanie pełnych
kopii zapasowych. Ten pakiet zawiera narzędzia getfacl i setfacl
potrzebne do modyfikacji list kontroli dostępu (ACL).

Pakiet zawiera też niezależny od platformy serwer rmt, który ma
zaimplementowane wszystkie rozszerzenia Sun/GNU/Schily/BSD i pozwala
na dostęp klientem rmt z dowolnego systemu operacyjnego.

%prep
%setup -q
%{?with_selinux:%patch0 -p1}
%patch1 -p1
%patch2 -p1

# new ac doesn't like comments in the same line as #undef
%{__perl} -pi -e 's@/\*.*\*/@@g' autoconf/xconfig.h.in
# kill annoying beep and sleep
%{__perl} -pi -e 's/^__gmake_warn.*//' RULES/mk-gmake.id

%build
cd autoconf
./autoconf
cd ..
%{__make} \
	COPTOPT="%{rpmcflags}" \
	CC="%{__cc}" \
	LDCC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/default

%{__make} -j1 install \
	INS_BASE=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=/share/man

install rmt/rmt.dfl $RPM_BUILD_ROOT%{_sysconfdir}/default/rmt
install star/star.dfl $RPM_BUILD_ROOT%{_sysconfdir}/default/star

# unwanted here (command conflict with tar and mt-st)
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{mt,tar}

# cleanup unpackaged stuff
%{__rm} -r $RPM_BUILD_ROOT{%{_includedir},%{_prefix}/lib,%{_datadir}/doc}
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/{man3,man5/make*.5*}

echo '.so star.1' > $RPM_BUILD_ROOT%{_mandir}/man1/ustar.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AN-%{version} CDDL.* Changelog READMEs/README.linux STATUS.alpha TODO
%doc star/README* star/STARvsGNUTAR
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/rmt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/star
%attr(755,root,root) %{_bindir}/gnutar
%attr(755,root,root) %{_bindir}/scpio
%attr(755,root,root) %{_bindir}/smt
%attr(755,root,root) %{_bindir}/spax
%attr(755,root,root) %{_bindir}/star
%attr(755,root,root) %{_bindir}/star_sym
%attr(755,root,root) %{_bindir}/suntar
%attr(755,root,root) %{_bindir}/tartest
%attr(755,root,root) %{_bindir}/ustar
%attr(755,root,root) %{_sbindir}/rmt
%{_mandir}/man1/gnutar.1*
%{_mandir}/man1/match.1*
%{_mandir}/man1/scpio.1*
%{_mandir}/man1/spax.1*
%{_mandir}/man1/star.1*
%{_mandir}/man1/suntar.1*
%{_mandir}/man1/tartest.1*
%{_mandir}/man1/ustar.1*
%{_mandir}/man1/smt.1*
%{_mandir}/man1/rmt.1*
%{_mandir}/man5/star.5*
