%define		module		Louie
Summary:	Signal dispatching mechanism
Name:		python-%{module}
Version:	1.1
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/L/Louie/%{module}-%{version}.tar.gz
# Source0-md5:	46a61f7a88c624433c96f28ae30aa1a4
URL:		http://pylouie.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools >= 0.6-0.c1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Louie provides Python programmers with a straightforward way to
dispatch signals between objects in a wide variety of contexts. It is
based on PyDispatcher, which in turn was based on a highly-rated
recipe in the Python Cookbook.

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/louie/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/louie
%{py_sitescriptdir}/louie/*.py[co]
%{py_sitescriptdir}/Louie-%{version}-py*.egg-info
