#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	TNEF
Summary:	Convert::TNEF - Perl module to read TNEF files
Summary(pl):	Convert::TNEF - modu³ Perla do odczytu plików TNEF
Name:		perl-Convert-TNEF
Version:	0.17
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31cddf42fae9495b4a686b17ec68d7e0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-tools
BuildRequires:	perl(MIME::Body) >= 4.109
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TNEF stands for Transport Neutral Encapsulation Format, and if you've
ever been unfortunate enough to receive one of these files as an email
attachment, you may want to use the Convert::TNEF Perl module.

%description -l pl
TNEF oznacza niezale¿ny od transportu format enkapsulacji (Transport
Neutral Encapsulation Format) i je¶li otrzyma siê jeden z takich
plików jako za³±cznik w e-mailu, mo¿e zaistnieæ potrzeba pos³u¿enia
siê modu³em Perla Convert::TNEF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Convert/TNEF.pm
