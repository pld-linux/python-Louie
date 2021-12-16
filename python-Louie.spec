%define		module		Louie
Summary:	Signal dispatching mechanism
Summary(pl.UTF-8):	Mechanizm rozprowadzania sygnałów
Name:		python-%{module}
Version:	1.1
Release:	7
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/L/Louie/%{module}-%{version}.tar.gz
# Source0-md5:	46a61f7a88c624433c96f28ae30aa1a4
URL:		http://pylouie.org/
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 1:0.6-0.c1
BuildRequires:	rpm-pythonprov
Requires:	python-libs
Requires:	python-nose >= 0.8.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Louie provides Python programmers with a straightforward way to
dispatch signals between objects in a wide variety of contexts. It is
based on PyDispatcher, which in turn was based on a highly-rated
recipe in the Python Cookbook.

%description -l pl.UTF-8
Louie udostępnia programistom Pythona bezpośredni sposób
rozprowadzania sygnałów między obiektami w szerokim zakresie
kontekstów. Jest oparty na module PyDispatcher, który z kolei jest
oparty na przepisie z dokumentu "Python Cookbook".

%prep
%setup -qn %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/louie/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/louie
%{py_sitescriptdir}/louie/*.py[co]
%{py_sitescriptdir}/Louie-%{version}-py*.egg-info
