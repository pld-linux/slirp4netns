Summary:	User-mode networking for unprivileged network namespaces
Name:		slirp4netns
Version:	1.1.9
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/rootless-containers/slirp4netns/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fe9d1020205c41faa195e821730d8462
URL:		https://github.com/rootless-containers/slirp4netns
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.2
BuildRequires:	glib2-devel
BuildRequires:	go-md2man
BuildRequires:	libcap-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libslirp-devel >= 4.1.0
BuildRequires:	pkgconfig
Requires:	libslirp >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
slirp4netns provides user-mode networking ("slirp") for unprivileged
network namespaces.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/slirp4netns
%{_mandir}/man1/slirp4netns.1*
