Summary:	Simple V4L program designed to view and process video streams
Summary(pl):	Narzedzie do ogladania i przetwarzania strumieni video z urzadzen v4l
Name:		SDLcam
Version:	0.7.3
Release:	1
License:	GPL
Source0:	http://raph.darktech.org/SDLcam/%{name}-%{version}.tar.gz
Patch0:		%{name}-path.patch
URL:		http://raph.darktech.org/SDLcam/
Group:		X11/Applications/Multimedia

BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	divx4linux
BuildRequires:	libfame-devel >= 0.8.10-2
BuildRequires:	avifile-devel >= 0.7.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6 

%description
SDLcam is a simple Video4Linux program, that was designed to view
video streams coming from a Philips USB Webcam. It uses SDL, and has a
simple user interface. SDLcam can save snapshots in Jpeg, PNG or BMP
formats. It also has a lot of video filters that can be combined and
applied in real time to the video stream.


%description -l pl
Program SDLcam przeznaczony jest do ogladania i przetwarzania
strumienia video pochodzacego ze zrodla kompatybilnego z v4l -
szczegolnie kamer USB firmy Philips. Posiada prosty interfejs
uzytkownika, potrafi zapisywac zrzuty w formacie JPEG, PNG i BMP.
Posiada wiele filtrow, ktore mozna laczyc i przetwarzac nimi w czasie
rzeczywistym obraz.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/SDLcam
install -d $RPM_BUILD_ROOT%{_libdir}/SDLcam
install -d $RPM_BUILD_ROOT%{_libdir}/SDLcam/filters
install -d $RPM_BUILD_ROOT%{_libdir}/SDLcam/capture
install -d $RPM_BUILD_ROOT%{_libdir}/SDLcam/sources
cp SDLcam $RPM_BUILD_ROOT%{_bindir}/
cp LucidaSansRegular.ttf LucidaTypewriterRegular.ttf $RPM_BUILD_ROOT%{_datadir}/SDLcam/
cp -f filter/*.so $RPM_BUILD_ROOT%{_libdir}/SDLcam/filters
cp -f capture/*.so $RPM_BUILD_ROOT%{_libdir}/SDLcam/capture
cp -f sources/*.so $RPM_BUILD_ROOT%{_libdir}/SDLcam/sources
cp -f SDLcam.xml $RPM_BUILD_ROOT%{_datadir}/SDLcam

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README TODO
%attr(755,root,root) %{_bindir}/SDLcam
%{_datadir}/SDLcam/LucidaSansRegular.ttf
%{_datadir}/SDLcam/LucidaTypewriterRegular.ttf
%{_datadir}/SDLcam/SDLcam.xml
%{_libdir}/SDLcam/filters/*
%{_libdir}/SDLcam/capture/*
%{_libdir}/SDLcam/sources/*
