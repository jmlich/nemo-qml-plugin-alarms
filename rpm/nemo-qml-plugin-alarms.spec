# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       nemo-qml-plugin-alarms

# >> macros
# << macros

Summary:    Alarms plugin for Nemo Mobile
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-alarms
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-alarms.yaml
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(timed) >= 2.67
Provides:   nemo-qml-plugins-alarms > 0.3.15
Obsoletes:   nemo-qml-plugins-alarms <= 0.3.15

%description
%{summary}.

%package tests
Summary:    QML alarms plugin tests
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/alarms/libnemoalarms.so
%{_libdir}/qt4/imports/org/nemomobile/alarms/qmldir
# >> files
# << files

%files tests
%defattr(-,root,root,-)
/opt/tests/nemo-qml-plugins/alarms/*
# >> files tests
# << files tests
