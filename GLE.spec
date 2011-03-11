Summary:	Graphics scripting language designed for creating publication quality graphs, plots, diagrams, figures and slides
Name:		GLE
Version:	4.2.3b
Release:	0.3
License:	BSD
Group:		Applications/Science
Source0:	http://downloads.sourceforge.net/glx/gle-graphics-%{version}f-src.tar.gz
# Source0-md5:	5884a1cbf7a0fe5d3a18a235d10f64a8
URL:		http://glx.sourceforge.net/index.html
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	texlive-latex
BuildRequires:	texlive-makeindex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLE (Graphics Layout Engine) is a graphics scripting language designed
for creating publication quality graphs, plots, diagrams, figures and
slides. GLE supports various graph types (function plots, histograms,
bar graphs, scatter plots, contour lines, color maps, surface plots,
...) through a simple but flexible set of graphing commands. More
complex output can be created by relying on GLE's scripting language,
which is full featured with subroutines, variables, and logic control.
GLE relies on LaTeX for text output and supports mathematical formulea
in graphs and figures. GLE's output formats include EPS, PS, PDF,
JPEG, and PNG.

%package gui
Summary:	GUI to gle
License:	GPL v2
Group:		X11/Applications/Science

%description gui
GUI to gle.

%package devel
Summary:	Development files.
Group:		Development/Libraries

%description devel
Development files.

%prep
%setup -q -n gle-graphics-%{version}
for makefile in $(find -name "Makefile*"); do
	sed -i "/chmod/d ; s/-m [0-9]\{3\}//g" ${makefile}
done

%build
%configure INSTALL_DATA=/usr/bin/install
%{__make} -j1
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT
%{__mv} $RPM_BUILD_ROOT%{_docdir}/{gle-graphics,%{name}-%{version}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gle
%attr(755,root,root) %{_bindir}/glebtool
%doc %{_docdir}/%{name}-%{version}
%{_libdir}/libgle-graphics*
%{_mandir}/man1/gle.1*
%{_datadir}/gle-graphics

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qgle

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/gle-graphics.pc
