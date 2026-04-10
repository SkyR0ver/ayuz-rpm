%global _icondir %{_iconsdir}/hicolor/1024x1024/apps
%global appid de.guido.asus-hub

Name:           asus-hub
Version:        1.0.2
Release:        %autorelease
Summary:        Unofficial Control Center for Asus Laptops

License:        GPL-3.0-or-later
URL:            https://github.com/Traciges/Asus-Hub

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  dbus-devel
BuildRequires:  libappstream-glib

Requires:       gtk4
Requires:       libadwaita
Requires:       asusctl
Requires:       supergfxctl
Requires:       easyeffects
Requires:       iio-sensor-proxy
Requires:       swayidle

%description
%{summary}.


%prep
%autosetup -n Asus-Hub-%{version}


%build
cargo build --release


%install
# Install binary file
install -Dpm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# Install icon
install -Dpm644 assets/trayicon.png %{buildroot}%{_icondir}/%{appid}.png

# Install desktop file
install -Dpm644 packaging/%{appid}.desktop %{buildroot}%{_datadir}/applications/%{appid}.desktop

# Install metainfo file
install -Dpm644 packaging/%{appid}.metainfo.xml %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml


%files
%license LICENSE
%{_bindir}/%{name}
%{_icondir}/%{appid}.png
%{_datadir}/applications/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml


%changelog
%autochangelog
