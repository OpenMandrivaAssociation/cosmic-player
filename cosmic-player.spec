%undefine _debugsource_packages
%define         appname com.system76.CosmicPlayer
Name:           cosmic-player
Version:        1.0.0
Release:        0.alpha5.0
Summary:        COSMIC media player
Group:          Video
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-player
Source0:        https://github.com/pop-os/cosmic-screenshot/archive/epoch-%{version}-alpha.5/%{name}-epoch-%{version}-alpha.5.tar.gz
#Source:         cosmic-player-master.zip
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  clang-devel
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.5 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/%{appname}.svg
%{_datadir}/icons/hicolor/???x???/apps/%{appname}.svg
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.metainfo.xml
