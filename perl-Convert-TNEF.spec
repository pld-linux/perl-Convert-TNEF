%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	TNEF
Summary:	Convert::TNEF perl module
Summary(pl):	Modu³ perla Convert::TNEF
Name:		perl-Convert-TNEF
Version:	0.16
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::TNEF - Perl module to read TNEF files.

%description -l pl
Convert::TNEF - modu³ Perla do czytania plików TNEF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Convert/TNEF.pm
