%define upstream_name       Logfile-Rotate
%define upstream_version    1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Perl module to rotate logfiles
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Logfile/%{upstream_name}-%{upstream_version}.tar.gz
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl module to rotate logfiles.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc MANIFEST 
%{perl_vendorlib}/Logfile/Rotate.pm
%{_mandir}/*/*

