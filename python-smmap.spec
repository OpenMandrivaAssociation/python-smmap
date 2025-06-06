%define upstream_name smmap

Name: 		python-%{upstream_name}
Version:	5.0.2
Release:	1
Summary: 	A pure git implementation of a sliding window memory map manager
License:	BSD
Group: 		Development/Python
Url: 		https://pypi.python.org/pypi/smmap
Source0:	https://files.pythonhosted.org/packages/source/s/smmap/%{upstream_name}-%{version}.tar.gz
BuildRequires:  python-distribute
BuildArch:      noarch

%description
When reading from many possibly large files in a fashion similar to random
access, it is usually the fastest and most efficient to use memory maps.

%prep
%autosetup -p1 -n %upstream_name-%version

%build
%py_build

%install
%py_install

%files
%defattr(-,root,root)
%doc PKG-INFO
%{python_sitelib}/smmap
%{python_sitelib}/smmap-%{version}-py%{py_ver}.egg-info


%changelog
* Thu Jul 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.1-1mdv2011
+ Revision: 689059
- update to new version 0.8.1

* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.0-1
+ Revision: 688466
- import python-smmap

