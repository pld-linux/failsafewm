Summary:	Window manager for REAL minimalists
Summary(pl):	Zarz�dca okien dla prawdziwych minimalist�w
Name:		failsafewm
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.small-window-manager.de/%{name}-%{version}.tgz
# Source0-md5:	8ec6487cdf585775d9351f626d0de11f
Source1:	%{name}-xsession.desktop
URL:		http://www.small-window-manager.de/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/%{name}

%description
failsafewm is at a very early development stage... It is just
something for REAL minimalists.

Usage:

Alt-Tab: cycles windows
Alt-F2 : window under mouse can be moved until a mouse button is pressed.
Alt-F3 : window under mouse can be resized until a mouse button is pressed.
Alt-F4 : does currently nothing.
Alt-F5 : raise window under mouse cursor

failsafewm may be still instable.

%description -l pl
failsafewm jest na pocz�tkowym etapie rozwoju. Co� dla prawdziwych
minimalist�w.

U�ycie:

Alt-Tab: zmienia cyklicznie okna.
Alt-F2 : przesuwa okno znajduj�ce si� pod kursorem myszy do momentu
         naci�ni�cia przycisku myszy.
Alt-F3 : zmienia rozmiary okna do momentu naci�ni�cia przycisku myszy.
Alt-F4 : na razie nie robi nic.
Alt-F5 : uaktywnia okno pod kursorem.

failsafewm mo�e nie dzia�a� najlepiej.

%prep
%setup -q -n failsafewm

%build
%{__make} CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xsessions}

install failsafewm $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xsessions/%{name}.desktop
