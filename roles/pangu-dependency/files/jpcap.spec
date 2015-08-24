%define __jar_repack 0
%define debug_package %{nil}
%define name         jpcap
%define _prefix      /opt/local/lib
%define _conf_dir    %{_sysconfdir}/jpcap
%define _log_dir     %{_var}/log/jpcap

Summary: jpcap
Name: jpcap
Version: %{version}
Release: %{build_number}
License: Apache License, Version 2.0
Group: Applications/Databases
URL: http://netresearch.ics.uci.edu
Source: http://netresearch.ics.uci.edu/kfujii/jpcap/jpcap-%{version}.tar.gz

%description
jpcap

%prep

%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/jpcap
cp -r $RPM_BUILD_DIR $RPM_BUILD_ROOT%{_prefix}
rm -rf $RPM_BUILD_ROOT%{_prefix}/jpcap

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_prefix}

%changelog
* Sat Aug 8 2015 zard <we_zard@163.com> - 0.7
- initial release
