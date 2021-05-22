#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-Compare
Version  : 0.55
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/List-Compare-0.55.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/List-Compare-0.55.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblist-compare-perl/liblist-compare-perl_0.53-1.debian.tar.xz
Summary  : 'Compare elements of two or more lists'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-List-Compare-license = %{version}-%{release}
Requires: perl-List-Compare-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)

%description
List::Compare - Compare elements of two or more lists
This document refers to version 0.55 of List::Compare.  This version was
released August 16 2020.

%package dev
Summary: dev components for the perl-List-Compare package.
Group: Development
Provides: perl-List-Compare-devel = %{version}-%{release}
Requires: perl-List-Compare = %{version}-%{release}

%description dev
dev components for the perl-List-Compare package.


%package license
Summary: license components for the perl-List-Compare package.
Group: Default

%description license
license components for the perl-List-Compare package.


%package perl
Summary: perl components for the perl-List-Compare package.
Group: Default
Requires: perl-List-Compare = %{version}-%{release}

%description perl
perl components for the perl-List-Compare package.


%prep
%setup -q -n List-Compare-0.55
cd %{_builddir}
tar xf %{_sourcedir}/liblist-compare-perl_0.53-1.debian.tar.xz
cd %{_builddir}/List-Compare-0.55
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/List-Compare-0.55/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-Compare
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-List-Compare/53adf2d8950d2ff97187db18242e087fd51d6bef
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::Compare.3
/usr/share/man/man3/List::Compare::Base::_Auxiliary.3
/usr/share/man/man3/List::Compare::Base::_Engine.3
/usr/share/man/man3/List::Compare::Functional.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-Compare/53adf2d8950d2ff97187db18242e087fd51d6bef

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/List/Compare.pm
/usr/lib/perl5/vendor_perl/5.34.0/List/Compare/Base/_Auxiliary.pm
/usr/lib/perl5/vendor_perl/5.34.0/List/Compare/Base/_Engine.pm
/usr/lib/perl5/vendor_perl/5.34.0/List/Compare/Functional.pm
