Summary:	GTK2 tool to define photostock IPTC tags and upload images to many photostocks
Name:		photostock-helper
Version:	0.0.1
Release:	1
License:	GPLv3
Group:		Graphics
Url:		https://launchpad.net/photostock-helper
# repack from launchpad
Source0:	%{name}-%{version}.tar.bz2
Patch0:		photostock-helper-0.0.1-datapath.patch
BuildArch:	noarch

%description
PhotoStock Helper is a small GTK2-perl application that helps to define usual
photostock IPTC tags (headline, description, keywords) and upload photographs
to many photostocks at once.

%prep
%setup -q
%patch0 -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name}.pl %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 %{name}.glade %{buildroot}%{_datadir}/%{name}/%{name}.glade

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=PhotoStock Helper
Comment=GTK2 tool to define photostock IPTC tags and upload images to many photostocks
Exec=%{_bindir}/%{name}
Icon=go-up
Terminal=false
Type=Application
Categories=Graphics;
EOF

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
