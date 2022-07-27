Name:		wfuzz
Version:	3.1.0
Release:	1
Summary:	The web bruteforcer
License:	GPL
Group:		Networking/Other
URL:		http://www.edge-security.com/wfuzz.php
Source0:    https://github.com/xmendez/wfuzz/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#Source:     http://www.edge-security.com/soft/wfuzz-%{version}.tar.bz2
#Patch0:     wfuzz-1.4-fhs.patch
Requires:   python-curl
BuildArch:	noarch


%description
Wfuzz is a tool designed for bruteforcing Web Applications, it can be used for
finding resources not linked (directories, servlets, scripts, etc), bruteforce
GET and POST parameters for checking different kind of injections (SQL, XSS,
LDAP,etc), bruteforce Forms parameters (User/Password), Fuzzing,etc.

%prep
%setup -q -n %{name}-%{version}
#patch0 -p 1
#chmod 644 COPYING LICENSES README

%build
%py_build
%install
%py_install

#install -d -m 755 %{buildroot}%{_bindir}
#install -d -m 755 %{buildroot}%{_datadir}/wfuzz/lib

#install -m 755 wfuzz.py %{buildroot}%{_bindir}
#install -m 644 *.py %{buildroot}%{_datadir}/wfuzz/lib
#rm -f %{buildroot}%{_datadir}/wfuzz/lib/wfuzz.py
#cp -pr wordlist %{buildroot}%{_datadir}/wfuzz

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING LICENSES README
%{_bindir}/wfuzz.py
%{_datadir}/wfuzz



%changelog
* Wed Jun 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.4c-1mdv2011.0
+ Revision: 682371
- import wfuzz

