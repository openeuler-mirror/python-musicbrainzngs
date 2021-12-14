Name:           python-musicbrainzngs
Version:        0.7.1
Release:        1 
Summary:        Python bindings for MusicBrainz NGS webservice

License:        BSD and ISC
URL:            https://github.com/alastair/python-musicbrainzngs
Source0:        https://github.com/alastair/python-musicbrainzngs/archive/refs/tags/v0.7.1.tar.gz

BuildArch:      noarch

%description
This library implements webservice bindings for the MusicBrainz NGS site, also
known as /ws/2.

For more information on the MusicBrainz webservice see:
  http://wiki.musicbrainz.org/XML_Web_Service

%package     -n python3-musicbrainzngs
Summary:        Python 3 bindings for MusicBrainz NGS webservice
%{?python_provide:%python_provide python3-musicbrainzngs}
BuildRequires:  python3-devel
BuildRequires:  python3-nose

%description -n python3-musicbrainzngs
This library implements Python 3 webservice bindings for the
MusicBrainz NGS site, also known as /ws/2.

For more information on the MusicBrainz webservice see:
  http://wiki.musicbrainz.org/XML_Web_Service

%prep

%autosetup -n python-musicbrainzngs-0.7.1
chmod a-x examples/*.py
sed -i '1{\@^#!/usr/bin/env python@d}' examples/*.py

%build
%py3_build

%install
%py3_install

%check
rm -rf musicbrainzngs
PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version}
 
%files -n python3-musicbrainzngs
%license COPYING
%doc README.rst docs examples
%{python3_sitelib}/*

%changelog
* Wed Jul 07 2021 xuyonghui <xuyonghui@kylinos.cn> - 0.7.1-1
- Package init
