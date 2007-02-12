Summary:	Simple V4L program designed to view and process video streams
Summary(pl.UTF-8):	Narzędzie do oglądania i przetwarzania strumieni video z urządzeń v4l
Name:		SDLcam
Version:	0.7.3
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://sdlcam.raphnet.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	82b7d7e7e6f4d6fe1cd2c4ab97232fd8
Patch0:		%{name}-path.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-gcc33.patch
URL:		http://sdlcam.raphnet.net/
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRequires:	avifile-devel >= 3:0.7.15
BuildRequires:	divx4linux-devel
BuildRequires:	libfame-devel >= 0.8.10-2
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.4.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDLcam is a simple Video4Linux program, that was designed to view
video streams coming from a Philips USB Webcam. It uses SDL, and has a
simple user interface. SDLcam can save snapshots in Jpeg, PNG or BMP
formats. It also has a lot of video filters that can be combined and
applied in real time to the video stream.

%description -l pl.UTF-8
Program SDLcam przeznaczony jest do oglądania i przetwarzania
strumienia video pochodzącego ze źródła kompatybilnego z v4l - w
szczególności kamer USB firmy Philips. Posiada prosty interfejs
użytkownika, potrafi zapisywać zrzuty w formacie JPEG, PNG i BMP.
Posiada wiele filtrów, które można łączyć i przetwarzać nimi w czasie
rzeczywistym obraz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	FEATURES="%{rpmcflags} -DMMX -DTIMER"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/SDLcam,%{_libdir}/SDLcam/{filters,capture,sources}}

install SDLcam $RPM_BUILD_ROOT%{_bindir}
install LucidaSansRegular.ttf LucidaTypewriterRegular.ttf $RPM_BUILD_ROOT%{_datadir}/SDLcam
install filter/*.so $RPM_BUILD_ROOT%{_libdir}/SDLcam/filters
install capture/*.so $RPM_BUILD_ROOT%{_libdir}/SDLcam/capture
install sources/*.so $RPM_BUILD_ROOT%{_libdir}/SDLcam/sources
install SDLcam.xml $RPM_BUILD_ROOT%{_datadir}/SDLcam

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/SDLcam
%attr(755,root,root) %{_libdir}/SDLcam
%{_datadir}/SDLcam
