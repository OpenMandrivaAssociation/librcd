%define major 0
%define libname %mklibname rcd %major
%define develname %mklibname rcd -d

Name:		librcd
Summary:	Russian charset detection library
Version:	0.1.13
Release:	2
License:	LGPLv2.1+
Group:		System/Libraries
URL:		http://http://rusxmms.sourceforge.net
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

%package -n %{develname}
Summary:        Russian charset detection library development files
Group:          Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

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


%changelog
* Tue Feb 21 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.1.13-2
+ Revision: 778548
- add provides for devel package
- fix description

* Mon Feb 20 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.1.13-1
+ Revision: 778194
- imported package librcd

