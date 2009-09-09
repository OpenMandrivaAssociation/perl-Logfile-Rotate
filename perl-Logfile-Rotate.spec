%define	module	Logfile-Rotate
%define	name	perl-%{module}
%define	version	1.04
%define	release	%mkrel 1

Summary:	Logfile::Rotate to rotate logfiles
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.gz
Url:		http://www.cpan.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot/
Buildrequires:	perl-devel
Requires:	perl 
Buildarch:	noarch

%description


%prep
%setup -q -n %{module}-%{version}

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

