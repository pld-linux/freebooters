Summary:	Free "Pirates!" clone
Summary(pl):	Klon gry "Pirates!"
Name:		freebooters
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://download.gna.org/freebooters/%{name}-%{version}.tar.gz
# Source0-md5:	153fdd7110c48ee93a7f7a894a32a56c
Patch0:		%{name}-paths.patch
URL:		http://home.gna.org/freebooters/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	SDL_ttf-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freebooters is a strategy game settled in the Caribbean Sea during the
golden age of piracy. It is based on the game mechanics of Sid Meier's
"Pirates!", but is not an exact clone.

%description -l pl
Freebooters jest gr± strategiczn±, której akcja rozgrywa siê na Morzu
Karaibskim w czasach z³otej ery piratów. Bazuje na grze Sida Meiera
"Pirates!", ale nie jest jej dok³adnym klonem.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="`sdl-config --cflags` %{rpmcflags}"

sed -ie 's#datadir=.*#datadir=%{_datadir}/%{name}/#' data/%{name}.conf

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	DATADIR=%{_datadir} \
	MANDIR=%{_mandir} \
	SYSCONFDIR=%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,changelog-until-0.2.txt,NEWS,README,TODO}
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}
%{_mandir}/man6/*.6*
