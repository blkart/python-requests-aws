Name:           python-requests-aws
Version:        0.1.8
Release:        1.eayun%{?dist}
Summary:        AWS authentication for Amazon S3 for the python requests module

License:        GPL
Group:          Development/Languages/Python
Url:            https://github.com/tax/python-requests-aws
Source:         python-requests-aws-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-requests
BuildRequires:  python-setuptools
Requires:       python-requests >= 2.4.1

%description
AWS authentication for Amazon S3 for the wonderful [pyhon requests library](http://python-requests.org)

%prep
%setup -q -n python-requests-aws-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{python_sitelib}/*

%changelog
* Fri Jul 15 2016 blkart <blkart.org@gmail.com>
- build rpm package
