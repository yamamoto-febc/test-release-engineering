# sudo yum -y install rpmdevtools go && rpmdev-setuptree
# rpmbuild -ba ~/rpmbuild/SPECS/usacloud.spec

%define _binaries_in_noarch_packages_terminate_build 0

Summary: CLI client of the SakuraCloud
Name:    usacloud
Version: %{_version}
Release: 1
BuildArch: %{buildarch}
License: Apache-2.0
Group:   SakuraCloud
URL:     https://github.com/sacloud/usacloud

Source0:   %{_sourcedir}/usacloud_bash_completion
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
CLI client of the SakuraCloud

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 %{_builddir}/%{name}  %{buildroot}%{_bindir}/%{name}
%{__mkdir} -p %{buildroot}%{_sysconfdir}/bash_completion.d
%{__install} -m 644 -T %{SOURCE0} %{buildroot}%{_sysconfdir}/bash_completion.d/usacloud


%clean
%{__rm} -rf %{buildroot}

%post

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_sysconfdir}/bash_completion.d/usacloud

%changelog
* Wed Mar 08 2017 <yamamoto.febc@gmail.com> - 0.0.5-1
- type1:merge (by yamamoto-febc)

* Wed Mar 08 2017 <yamamoto.febc@gmail.com> - 0.0.4-1
- Add test2 (by yamamoto-febc)

* Wed Mar 08 2017 <yamamoto.febc@gmail.com> - 0.0.3-1
- Add binaries for test (by yamamoto-febc)
- Rename .spec (by yamamoto-febc)


* Fri Mar 3 2017 <yamamoto.febc@gmail.com> - 0.0.1-alpha.10
- Initial commit
