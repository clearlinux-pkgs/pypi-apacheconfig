#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-apacheconfig
Version  : 0.3.2
Release  : 18
URL      : https://files.pythonhosted.org/packages/cd/b5/b810fede6b3d74f0f9a6357b8e38f124be06030143c0ca5239ed08e277ac/apacheconfig-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/cd/b5/b810fede6b3d74f0f9a6357b8e38f124be06030143c0ca5239ed08e277ac/apacheconfig-0.3.2.tar.gz
Summary  : Apache config file parser
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-apacheconfig-bin = %{version}-%{release}
Requires: pypi-apacheconfig-license = %{version}-%{release}
Requires: pypi-apacheconfig-python = %{version}-%{release}
Requires: pypi-apacheconfig-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ply)
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Apache-style config parser
[![PyPI](https://img.shields.io/pypi/v/apacheconfig.svg?maxAge=1800)](https://pypi.org/project/apacheconfig)
[![Python Versions](https://img.shields.io/pypi/pyversions/apacheconfig.svg)](https://pypi.org/project/apacheconfig/)
[![Build status](https://travis-ci.org/etingof/apacheconfig.svg?branch=master)](https://secure.travis-ci.org/etingof/apacheconfig)
[![Coverage Status](https://img.shields.io/codecov/c/github/etingof/apacheconfig.svg)](https://codecov.io/github/etingof/apacheconfig)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/apacheconfig/master/LICENSE.rst)

%package bin
Summary: bin components for the pypi-apacheconfig package.
Group: Binaries
Requires: pypi-apacheconfig-license = %{version}-%{release}

%description bin
bin components for the pypi-apacheconfig package.


%package license
Summary: license components for the pypi-apacheconfig package.
Group: Default

%description license
license components for the pypi-apacheconfig package.


%package python
Summary: python components for the pypi-apacheconfig package.
Group: Default
Requires: pypi-apacheconfig-python3 = %{version}-%{release}

%description python
python components for the pypi-apacheconfig package.


%package python3
Summary: python3 components for the pypi-apacheconfig package.
Group: Default
Requires: python3-core
Provides: pypi(apacheconfig)
Requires: pypi(ply)
Requires: pypi(six)

%description python3
python3 components for the pypi-apacheconfig package.


%prep
%setup -q -n apacheconfig-0.3.2
cd %{_builddir}/apacheconfig-0.3.2
pushd ..
cp -a apacheconfig-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672254803
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-apacheconfig
cp %{_builddir}/apacheconfig-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-apacheconfig/03df29eb9eda80d9d9701a9626b8acb2d33e90d0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/apacheconfigtool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-apacheconfig/03df29eb9eda80d9d9701a9626b8acb2d33e90d0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
