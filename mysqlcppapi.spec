Summary:	C++ interface to MySQL Database
Summary(pl):	Interfejs C++ do bazy MySQL
Name:		mysqlcppapi
Version:	1.9.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	2479e6ab1f0f490119ead67e254fed3b
Patch0:		%{name}-mysql-4.1.patch
URL:		http://www.advogato.org/proj/mysqlcppapi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mysqlcppapi is a C++ interface to MySQL API.

%description -l pl
Mysqlcppapi jest interfejsem C++ do API MySQL.

%package devel
Summary:	C++ interface to MySQL Database (headers)
Summary(pl):	Interfejs C++ do bazy MySQL (pliki nag³ówkowe)
Group:		Development/Libraries
Requires:	libstdc++-devel
Requires:	mysql-devel
Requires:	%{name} = %{version}-%{release}

%description devel
Mysqlcppapi is a C++ interface to MySQL API. Package contains the
development header files necessary to develop MySQL client
applications using Mysql++.

%description devel -l pl
Mysqlcppapi jest interfejsem C++ do API MySQL. Paczka zawiera nag³ówki
potrzebne do rozwoju aplikacji klienckich u¿ywaj±cych Mysql++.

%package static
Summary:	C++ interface to MySQL Database (static libraries)
Summary(pl):	Interfejs C++ do bazy MySQL (biblioteki statyczne)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Mysqlcppapi is a C++ interface to MySQL API. Package contains the static
libraries.

%description static -l pl
Mysqlcppapi jest interfejsem C++ do API MySQL. Paczka zawiera biblioteki
statyczne.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--with-mysql=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.cc $RPM_BUILD_ROOT%{_examplesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README TODO ChangeLog AUTHORS NEWS 
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_examplesdir}/*.cc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
