%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	TNEF
Summary:	Convert::TNEF perl module
Summary(pl):	Modu³ perla Convert::TNEF
Name:		perl-Convert-TNEF
Version:	0.17
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31cddf42fae9495b4a686b17ec68d7e0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-MIME-tools
BuildRequires:	perl(MIME::Body) >= 4.109
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::TNEF - Perl module to read TNEF files.

%description -l pl
Convert::TNEF - modu³ Perla do czytania plików TNEF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Convert/TNEF.pm
