%define upstream_name smmap

Name: 		python-%{upstream_name}
Version: 	0.8.2
Release: 	2
Summary: 	A pure git implementation of a sliding window memory map manager
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/smmap
Source0: 	http://pypi.python.org/packages/source/s/smmap/smmap-%{version}.tar.gz
BuildRequires:  python-distribute
BuildArch:      noarch

%description
When reading from many possibly large files in a fashion similar to random
access, it is usually the fastest and most efficient to use memory maps.

%prep
%setup -q -n %upstream_name-%version

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

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

