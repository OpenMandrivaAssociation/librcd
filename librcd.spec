%define major 0
%define libname %mklibname rcd %major
%define develname %mklibname rcd -d

Name:		librcd
Summary:	Russian charset detection library
Version:	0.1.13
Release:	1
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://http://rusxmms.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2

%description
Russian charset detection library.

%package -n %{libname}
Summary:        Russian charset detection library
Group:          System/Libraries

%description -n %{libname}
Russian charset detection library.

%package -n %{develname}
Summary:        Russian charset detection library development files
Group:          Development/C
Requires:	%{libname} = %{version}

%description -n %{develname}
Russian charset detection library. This package contains files required
for development purposes only.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/librcd.so.%{major}
%{_libdir}/librcd.so.%{version}

%files -n %{develname}
%doc AUTHORS ChangeLog README
%{_libdir}/librcd.so
%{_includedir}/librcd.h
