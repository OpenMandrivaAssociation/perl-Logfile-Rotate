%define upstream_name       Logfile-Rotate
%define upstream_version    1.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1
Summary:	Perl module to rotate logfiles
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Logfile-Rotate
Source:		https://cpan.metacpan.org/authors/id/P/PA/PAULG/Logfile-Rotate-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl module to rotate logfiles.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files 
%doc MANIFEST 
%{perl_vendorlib}/Logfile/Rotate.pm
%{_mandir}/*/*

