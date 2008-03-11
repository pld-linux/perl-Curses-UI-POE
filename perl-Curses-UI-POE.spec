#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Curses
%define	pnam	UI-POE
Summary:	Curses::UI::POE - A subclass makes Curses::UI POE Friendly.
#Summary(pl.UTF-8):	
Name:		perl-Curses-UI-POE
Version:	0.02801
Release:	1
# same as perl (REMOVE THIS LINE IF NOT TRUE)
#License:	GPL v1+ or Artistic
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Curses/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5a97d0f9a13c6b04f60427d8bd173d9
Patch0:		%{name}-tests.patch
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/Curses-UI-POE/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(Curses::UI) >= 0.93
BuildRequires:	perl-POE >= 0.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A module that makes Curses::UI POE friendly.

%description -l pl.UTF-8
Moduł perlowy ktory zmienia Curses::UI w bardziej przyjazne dla POE.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Curses/UI/*.pm
#%%{perl_vendorlib}/Curses/UI/POE
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
