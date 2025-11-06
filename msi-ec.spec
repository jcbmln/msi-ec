%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     msi-ec
Version:  0.12.{{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Embedded Controller for MSI laptops
License:  GPLv2
URL:      https://github.com/jcbmln/msi-ec

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Embedded Controller for MSI laptops

%prep
%setup -q -c %{name}-main

%files
%doc %{name}-main/README.md
%license %{name}-main/LICENSE

%changelog
