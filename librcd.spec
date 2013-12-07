%define major	0
%define libname %mklibname rcd %{major}
%define devname %mklibname rcd -d

Name:		librcd
Summary:	Russian charset detection library
Version:	0.1.13
Release:	8
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://http://rusxmms.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2

%description
Library for autodection charset of russian text

LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized 
to handle very short titles, like ID3 tags, file names and etc, and provides 
very high accuracy even for short 3-4 letter words. Current version supports 
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251, 
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection 
accuracy on short titles and is able to detect ISO8859-1 (non-cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.

%package -n %{libname}
Summary:        Russian charset detection library
Group:          System/Libraries

%description -n %{libname}
Library for autodection charset of russian text

LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized 
to handle very short titles, like ID3 tags, file names and etc, and provides 
very high accuracy even for short 3-4 letter words. Current version supports 
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251, 
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection 
accuracy on short titles and is able to detect ISO8859-1 (non-cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.

%package -n %{devname}
Summary:        Russian charset detection library development files
Group:          Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
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
%{_libdir}/librcd.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README
%{_libdir}/librcd.so
%{_includedir}/librcd.h

