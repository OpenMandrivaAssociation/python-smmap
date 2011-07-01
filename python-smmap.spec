%define upstream_name smmap
%define name    python-%{upstream_name}
%define version 0.8.0
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	A pure git implementation of a sliding window memory map manager
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/smmap
Source0: 	http://pypi.python.org/packages/source/s/smmap/smmap-%{version}.tar.gz
BuildRequires:  python-distribute
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
When reading from many possibly large files in a fashion similar to random
access, it is usually the fastest and most efficient to use memory maps.

%prep
%setup -q -n %upstream_name-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc PKG-INFO
%{python_sitelib}/smmap
%{python_sitelib}/smmap-%{version}-py%{pyver}.egg-info
