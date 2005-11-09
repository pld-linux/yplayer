Summary:	yplayer - simple GUI player for Y Sound Objects using the GTK+ toolkit
Summary(pl):	yplayer - prosty graficzny odtwarzacz obiektów d¼wiêkowych Y oparty na GTK+
Name:		yplayer
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	03fa82937f084e9e9c91b469fb78e839
URL:		http://wolfpack.twu.net/YIFF/
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

%description -l pl
YPlayer to prosty odtwarzacz dla obiektów d¼wiêkowych Y z graficznym
interfejsem u¿ywaj±cym toolkitu GTK+.

%prep
%setup -q

%build
%{__make} -C yplayer \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall `gtk-config --cflags`"

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
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/yplayer
%{_pixmapsdir}/*.xpm
%{_mandir}/man1/yplayer.1*
