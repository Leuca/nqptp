Name:           {{{ git_dir_name }}}-unstable
Version:        {{{ get_source_ver }}}
Release:        {{{ get_release }}}%{?dist}
Summary:        Not Quite PTP (unstable)

License:        GPLv2+
URL:            https://github.com/mikebrady/nqptp
VCS:            {{{ git_dir_vcs }}}

Source:         {{{ git_dir_pack }}}

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  systemd-rpm-macros


%description
nqptp is a daemon that monitors timing data from any PTP clocks – up to 64 – it sees on ports 319 and 320. It maintains records for each clock, identified by Clock ID and IP.

It is a companion application to Shairport Sync and provides timing information for AirPlay 2 operation.

This version of nqptp has been built from the development branch

%prep
{{{ git_dir_setup_macro }}}

%build
# Avoid creating user and groups during package build
sed -i '/getent/d' Makefile.am

autoreconf -fi
%configure --with-systemd-startup
%make_build

%install
%make_install

%pre
getent group %{name} &>/dev/null || groupadd -r %{name} &>/dev/null
getent passwd %{name} &> /dev/null || useradd -r -M -g %{name} -s /sbin/nologin nqptp &>/dev/null

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/nqptp
%{_unitdir}/nqptp.service

%changelog
{{{ git_dir_changelog }}}
