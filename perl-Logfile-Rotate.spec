%define upstream_name       Logfile-Rotate
%define upstream_version    1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	Perl module to rotate logfiles
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Logfile/%{upstream_name}-%{upstream_version}.tar.gz

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

%changelog
* Thu Sep 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 437371
- use new %%perl_version macro

* Wed Sep 09 2009 Anne Nicolas <anne.nicolas@mandriva.com> 1.04-1mdv2010.0
+ Revision: 435147
- fix description
- first release (Vigilo deps)
- import perl-Logfile-Rotate

