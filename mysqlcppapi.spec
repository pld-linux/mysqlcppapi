Summary:	C++ interface to MySQL Database
Summary(pl.UTF-8):	Interfejs C++ do bazy MySQL
Name:		mysqlcppapi
Version:	2.0.0
%define	pre	rc2
Release:	0.%{pre}.3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mysqlcppapi/%{name}-%{version}_%{pre}.tar.gz
# Source0-md5:	640e05864f3f688fcb4aba0505e1ffe9
URL:		http://www.advogato.org/proj/mysqlcppapi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mysqlcppapi is a C++ interface to MySQL API.

%description -l pl.UTF-8
Mysqlcppapi jest interfejsem C++ do API MySQL.

%package devel
Summary:	C++ interface to MySQL Database (headers)
Summary(pl.UTF-8):	Interfejs C++ do bazy MySQL (pliki nagłówkowe)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	mysql-devel

%description devel
Mysqlcppapi is a C++ interface to MySQL API. This package contains the
development header files necessary to develop MySQL client
applications using Mysql++.

%description devel -l pl.UTF-8
Mysqlcppapi jest interfejsem C++ do API MySQL. Ten pakiet zawiera
pliki nagłówkowe potrzebne do rozwoju aplikacji klienckich używających
Mysql++.

%package static
Summary:	C++ interface to MySQL Database (static libraries)
Summary(pl.UTF-8):	Interfejs C++ do bazy MySQL (biblioteki statyczne)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Mysqlcppapi is a C++ interface to MySQL API. This package contains the
static libraries.

%description static -l pl.UTF-8
Mysqlcppapi jest interfejsem C++ do API MySQL. Ten pakiet zawiera
biblioteki statyczne.

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.cc $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog AUTHORS NEWS 
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
