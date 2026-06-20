Name:           dde-image-editor
Version:        1.0.0
Release:        1%{?dist}
Summary:        DDE Image Editor for Lingmo OS
License:        GPL-3.0-or-later
URL:            https://github.com/LingmoOS/dde-image-editor
Source0:        dde-image-editor-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.10
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(dtk6core)
BuildRequires:  pkgconfig(dtk6gui)
BuildRequires:  pkgconfig(dtk6widget)

%description
DDE Image Editor is an image editing application for the
Lingmo desktop environment with basic editing features.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE*
%{_bindir}/dde-image-editor
%{_libdir}/dde-image-editor/
%{_datadir}/applications/dde-image-editor.desktop

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
