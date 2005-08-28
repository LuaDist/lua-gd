Name: lua-gd
Version: 2.0.33r1
Release: 1
Summary: gd bindings for the Lua programming language
Summary(pt_BR): Bindings da bibliotea gd para Lua
Packager: Alexandre Erwin Ittner <aittner@netuno.com.br>
License: LGPL
Group: Libraries
Group(pt_BR): Bibliotecas
Source0: %{name}-%{version}.tar.gz
URL: http://lua-gd.luaforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: lua >= 5.0
Requires: libgd2 >= 2.0.33
BuildRequires: lua-devel
BuildRequires: libgd-devel >= 2.0.33
Prefix: /usr
Provides: libluagd.so libluagd

%description
Lua-GD is a library that allows you to use the gd graphic library from
programs written in the Lua programming language.


%description -l pt_BR
Lua-GD � uma biblioteca que permite que voc� use a biblioteca gr�fica
gd em programas escritos na linguagem Lua.


%prep
%setup -q

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp *.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf %{buildroot} $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING doc/* demos/*
%{_libdir}/*.so*

%changelog
* Sun Aug 28 2005 Alexandre Erwin Ittner <aittner@netuno.com.br>
- First version of this package.


