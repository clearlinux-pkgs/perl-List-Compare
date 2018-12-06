#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-Compare
Version  : 0.53
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/List-Compare-0.53.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/List-Compare-0.53.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblist-compare-perl/liblist-compare-perl_0.53-1.debian.tar.xz
Summary  : 'Compare elements of two or more lists'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-List-Compare-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::CaptureOutput)

%description
List::Compare - Compare elements of two or more lists
This document refers to version 0.53 of List::Compare.  This version was
released June 07 2015.

%package dev
Summary: dev components for the perl-List-Compare package.
Group: Development
Provides: perl-List-Compare-devel = %{version}-%{release}

%description dev
dev components for the perl-List-Compare package.


%package license
Summary: license components for the perl-List-Compare package.
Group: Default

%description license
license components for the perl-List-Compare package.


%prep
%setup -q -n List-Compare-0.53
cd ..
%setup -q -T -D -n List-Compare-0.53 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/List-Compare-0.53/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-List-Compare
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-List-Compare/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1List/Compare.pm
/usr/lib/perl5/vendor_perl/5.28.1List/Compare/Base/_Auxiliary.pm
/usr/lib/perl5/vendor_perl/5.28.1List/Compare/Base/_Engine.pm
/usr/lib/perl5/vendor_perl/5.28.1List/Compare/Functional.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::Compare.3
/usr/share/man/man3/List::Compare::Base::_Auxiliary.3
/usr/share/man/man3/List::Compare::Base::_Engine.3
/usr/share/man/man3/List::Compare::Functional.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-List-Compare/deblicense_copyright
