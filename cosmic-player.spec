%undefine _debugsource_packages
%define         appname com.system76.CosmicPlayer
Name:           cosmic-player
Version:        0.1.0+git20240702
Release:        0
Summary:        COSMIC media player
Group:          Video
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-player
# Source0:        https://github.com/pop-os/cosmic-screenshot/archive/epoch-%{version}-alpha.2/%{name}-epoch-%{version}-alpha.2.tar.gz
Source:         cosmic-player-master.zip
Source1:        vendor.tar.xz
Source2:        cargo_config

Patch0:         ffmpeg-next.patch
Patch1:         ffmpeg-7.patch

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

%description
%{summary}.

%prep
%autosetup -n cosmic-player-master -a1 -p1
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
%{_datadir}/applications/%{appname}.desktop
