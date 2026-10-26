%global debug_package %{nil}
%global upstream_version 0.1.0-alpha.7

Name:           flectar-mail
Version:        0.1.0
Release:        0.alpha.7%{?dist}
Summary:        Native, offline-first email client
License:        AGPL-3.0-only
URL:            https://github.com/flectar/mail
ExclusiveArch:  x86_64

Source0:        https://github.com/flectar/mail/releases/download/v%{upstream_version}/flectar-mail-%{upstream_version}-linux-x64.rpm

BuildRequires:  appstream
BuildRequires:  cpio
BuildRequires:  desktop-file-utils
BuildRequires:  rpm

Requires:       fontconfig
Requires:       hicolor-icon-theme
Requires:       libX11
Requires:       libX11-xcb
Requires:       libXcursor
Requires:       libXi
Requires:       libwayland-client
Requires:       libxkbcommon
Requires:       libxkbcommon-x11
Requires:       xdg-utils
Recommends:     gnome-keyring
Recommends:     gnupg2
Recommends:     pinentry
Recommends:     xdg-desktop-portal

%description
Flectar Mail is a native Rust and Slint mail client with offline-first storage, Gmail and Microsoft account support, contacts, and calendars.

%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idm

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.flectar.mail.desktop
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/com.flectar.mail.metainfo.xml

%files
%{_bindir}/flectar-mail
%{_libdir}/flectar-mail/
%{_datadir}/applications/com.flectar.mail.desktop
%{_datadir}/metainfo/com.flectar.mail.metainfo.xml
%{_datadir}/icons/hicolor/512x512/apps/com.flectar.mail.png
%{_datadir}/icons/hicolor/scalable/apps/com.flectar.mail.svg
%license %{_licensedir}/%{name}
%doc %{_docdir}/%{name}

%changelog
* Mon Oct 26 2026 Lezetho <hello@lezetho.xyz> - 0.1.0-0.alpha.7
- Initial copr for 0.1.0-alpha.7
