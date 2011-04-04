Summary: node.js
Name: node
Version: 0.3.4n4
Release: 1
License: XYZ
Group: n4
URL: unknown
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

%prep
%setup -q

%build
./configure --prefix="$RPM_BUILD_ROOT/usr"
make

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
/usr/lib/node/wafadmin/*
/usr/lib/pkgconfig/nodejs.pc
%{_includedir}/*
%{_mandir}/man1/*
%doc

%changelog
* Mon Apr  4 2011  <builder@rpmbuilder32.infra.corp.numberfour.eu> - 
- Initial build.

