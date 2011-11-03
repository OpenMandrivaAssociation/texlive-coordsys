# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/coordsys
# catalog-date 2007-02-20 10:49:06 +0100
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-coordsys
Version:	1.4
Release:	1
Summary:	Draw cartesian coordinate systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coordsys
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coordsys.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coordsys.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coordsys.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides commands for typesetting number lines
(coordinate axes), coordinate systems and grids in the picture
environment. The package may be integrated with other drawing
mechanisms: the documentation shows examples of drawing graphs
(coordinate tables created by Maple), using the eepic package's
drawing capabilities.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
