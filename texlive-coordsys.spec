Name:		texlive-coordsys
Version:	15878
Release:	2
Summary:	Draw cartesian coordinate systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coordsys
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coordsys.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coordsys.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coordsys.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for typesetting number lines
(coordinate axes), coordinate systems and grids in the picture
environment. The package may be integrated with other drawing
mechanisms: the documentation shows examples of drawing graphs
(coordinate tables created by Maple), using the eepic package's
drawing capabilities.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/coordsys/coordsys.sty
%{_texmfdistdir}/tex/latex/coordsys/logsys.sty
%doc %{_texmfdistdir}/doc/latex/coordsys/README
%doc %{_texmfdistdir}/doc/latex/coordsys/coordsys.pdf
%doc %{_texmfdistdir}/doc/latex/coordsys/putfile.maple
#- source
%doc %{_texmfdistdir}/source/latex/coordsys/coordsys.dtx
%doc %{_texmfdistdir}/source/latex/coordsys/coordsys.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
