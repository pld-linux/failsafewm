Summary:	Window manager for REAL minimalists
Summary(pl):	Menad¿er okien dla prawdziwych minimalistów
Name:		failsafewm
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.small-window-manager.de/%{name}-%{version}.tgz
URL:		http://www.small-window-manager.de/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
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
failsafewm jest na pocz±tkowym etapie rozwoju. Co¶ dla prawdziwych
minimalistów.

U¿ycie:

Alt-Tab: zmienia cyklicznie okna.
Alt-F2 : przesuwa okno znajduj±ce siê pod kursorem myszy do momentu
         naci¶niêcia przycisku myszy.
Alt-F3 : zmienia rozmiary okna do momentu naci¶niêcia przycisku myszy.
Alt-F4 : na razie nie robi nic.
Alt-F5 : uaktywnia okno pod kursorem.

failsafewm mo¿e nie dzia³aæ najlepiej.

%prep
%setup -q -n failsafewm

%build
%{__make} CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install failsafewm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
