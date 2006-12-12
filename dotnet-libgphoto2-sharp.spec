%include	/usr/lib/rpm/macros.mono
Summary:	.NET binding to libgphoto2
Summary(pl):	Wi�zanie .NET dla libgphoto2
Name:		dotnet-libgphoto2-sharp
Version:	2.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gphoto/libgphoto2-sharp-%{version}.tar.bz2
# Source0-md5:	5099e2d5ee928a33546eb0c56ad024cd
Patch0:		%{name}-am.patch
Patch1:		%{name}-version.patch
URL:		http://www.gphoto.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	libgphoto2-devel >= 2.3.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	rpmbuild(monoautodeps)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET binding to libgphoto2.

%description -l pl
Wi�zanie .NET dla libgphoto2.

%package devel
Summary:	Development files for .NET binding to libgphoto2
Summary(pl):	Pliki programistyczne wi�zani .NET dla libgphoto2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for .NET binding to libgphoto2.

%description devel -l pl
Pliki programistyczne wi�zani .NET dla libgphoto2.

%prep
%setup -q -n libgphoto2-sharp-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4m
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	cslibdir=%{_prefix}/lib/mono/libgphoto2-sharp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%{_prefix}/lib/mono/gac/libgphoto2-sharp
%{_prefix}/lib/mono/libgphoto2-sharp

%files devel
%defattr(644,root,root,755)
#%{_prefix}/lib/mono/libgphoto2-sharp
%{_pkgconfigdir}/libgphoto2-sharp.pc