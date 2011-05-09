Summary:	A new style menu
Name:		launchy
Version:	2.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.launchy.net/downloads/src/%{name}-%{version}.tar.gz
# Source0-md5:	ca9de9e165d6c327f48aa81dd0ee1a6f
URL:		http://www.launchy.net/
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Launchy is a free cross-platform utility designed to help you forget
about your start menu, the icons on your desktop, and even your file
manager.

Launchy indexes the programs in your start menu and can launch your
documents, project files, folders, and bookmarks with just a few
keystrokes!

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme*
%attr(755,root,root) %{_bindir}/launchy
%{_pixmapsdir}/launchy_icon.png
%{_desktopdir}/launchy.desktop
%dir %{_datadir}/launchy
%dir %{_datadir}/launchy/skins
%{_datadir}/launchy/skins/*
%dir %{_libdir}/launchy
%dir %{_libdir}/launchy/plugins
%dir %{_libdir}/launchy/plugins/icons
%{_libdir}/launchy/plugins/*.so
%{_libdir}/launchy/plugins/icons/*
