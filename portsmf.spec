Summary:	Port Standard MIDI File - portable library for reading/writing Standard MIDI Files
Summary(pl.UTF-8):	Port Standard MIDI File - przenośna biblioteka do odczytu/zapisu plików SMF
Name:		portsmf
Version:	0.1
%define	snap	20101010
Release:	0.%{snap}.1
License:	MIT-like
Group:		Libraries
# svn co https://portmedia.svn.sourceforge.net/svnroot/portmedia/portsmf/trunk portsmf
Source0:	%{name}.tar.xz
# Source0-md5:	654893b608c70230e0838725c563b86f
Patch0:		%{name}-shared.patch
URL:		http://sourceforge.net/p/portmedia/wiki/portsmf/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PortSMF is "Port Standard MIDI File", a cross-platform, C++ library
for reading and writing Standard MIDI Files.

%description -l pl.UTF-8
PortSMF (Port Standard MIDI File) to wieloplatformowa biblioteka C++
do odczytu i zapisu plików SMF (Standard MIDI File).

%package devel
Summary:	Header files for portSMF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki portSMF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for portSMF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki portSMF.

%package static
Summary:	Static portSMF library
Summary(pl.UTF-8):	Statyczna biblioteka portSMF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static portSMF library.

%description static -l pl.UTF-8
Statyczna biblioteka portSMF.

%prep
%setup -q -n %{name}
%patch0 -p1

%{__rm} configure

%build
%{__libtoolize}
%{__aclocal} -I autotools/m4
%{__autoconf}
%{__automake}
%configure \
	--includedir=%{_includedir}/portSMF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt changelog.txt license.txt
%attr(755,root,root) %{_libdir}/libportSMF.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libportSMF.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libportSMF.so
%{_libdir}/libportSMF.la
%{_includedir}/portSMF

%files static
%defattr(644,root,root,755)
%{_libdir}/libportSMF.a
