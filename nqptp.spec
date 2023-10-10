Name:		{{{ git_dir_name }}}
Version:	{{{ git_dir_version }}}
Release:	1%{?dist}
Summary:	Not Quite PTP

License:	GPLv2+
URL:		https://github.com/mikebrady/nqptp
VCS:		{{{ git_dir_vcs }}}

Source:		{{{ git_dir_pack }}}

BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	systemd-rpm-macros


%description
nqptp is a daemon that monitors timing data from any PTP clocks – up to 64 – it sees on ports 319 and 320. It maintains records for each clock, identified by Clock ID and IP.

It is a companion application to Shairport Sync and provides timing information for AirPlay 2 operation.

%prep
{{{ git_dir_setup_macro }}}

%build
autoreconf -fi
%configure --with-systemd-startup
%make_build

%install
%make_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
{{{ git_dir_changelog }}}
