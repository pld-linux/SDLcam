Summary:	Simple V4L program designed to view and process video streams
Summary(pl):	Narzêdzie do ogl±dania i przetwarzania strumieni video z urz±dzeñ v4l
Name:		SDLcam
Version:	0.7.3
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://raph.darktech.org/SDLcam/%{name}-%{version}.tar.gz
# Source0-md5:	82b7d7e7e6f4d6fe1cd2c4ab97232fd8
Patch0:		%{name}-path.patch
Patch1:		%{name}-include.patch
URL:		http://raph.darktech.org/SDLcam/
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRequires:	avifile-devel >= 0.7.15
BuildRequires:	divx4linux
BuildRequires:	libfame-devel >= 0.8.10-2
BuildRequires:	libxml2-devel >= 2.4.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
SDLcam is a simple Video4Linux program, that was designed to view
video streams coming from a Philips USB Webcam. It uses SDL, and has a
simple user interface. SDLcam can save snapshots in Jpeg, PNG or BMP
formats. It also has a lot of video filters that can be combined and
applied in real time to the video stream.

%description -l pl
Program SDLcam przeznaczony jest do ogl±dania i przetwarzania
strumienia video pochodz±cego ze ¼ród³a kompatybilnego z v4l - w
szczególno¶ci kamer USB firmy Philips. Posiada prosty interfejs
u¿ytkownika, potrafi zapisywaæ zrzuty w formacie JPEG, PNG i BMP.
Posiada wiele filtrów, które mo¿na ³±czyæ i przetwarzaæ nimi w czasie
rzeczywistym obraz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

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
%doc CHANGELOG LICENSE README TODO
%attr(755,root,root) %{_bindir}/SDLcam
%{_datadir}/SDLcam
%attr(755,root,root) %{_libdir}/SDLcam
