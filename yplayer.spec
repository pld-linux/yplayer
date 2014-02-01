Summary:	yplayer - simple GUI player for Y Sound Objects using the GTK+ toolkit
Summary(pl.UTF-8):	yplayer - prosty graficzny odtwarzacz obiektów dźwiękowych Y oparty na GTK+
Name:		yplayer
Version:	1.1.5
Release:	1
License:	GPL-like
Group:		Applications/Sound
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	f8b53defeb5d1c40380e969fd77cd670
URL:		http://freecode.com/projects/wpeyplayer
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	yiff-devel >= 2.14.1
Requires:	gtk+ >= 1.2.10
Requires:	yiff-lib >= 2.14.1
Conflicts:	yconsole <= 3.0.8-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer -ffast-math

%description
YPlayer is a simple GUI player for Y Sound Objects using the GTK+
toolkit.

%description -l pl.UTF-8
YPlayer to prosty odtwarzacz dla obiektów dźwiękowych Y z graficznym
interfejsem używającym toolkitu GTK+.

%prep
%setup -q

%build
%{__make} -C yplayer \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall `gtk-config --cflags` -DPREFIX=\\\"%{_prefix}\\\""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C yplayer install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man1/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/yplayer
%{_pixmapsdir}/yplayer.xpm
%{_mandir}/man1/yplayer.1*
