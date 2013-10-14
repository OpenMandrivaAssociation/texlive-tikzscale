# revision 30637
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzscale
# catalog-date 2013-05-22 10:58:45 +0200
# catalog-license lppl1.3
# catalog-version 0.2.6
Name:		texlive-tikzscale
Version:	0.2.6
Release:	2
Summary:	Resize pictures while respecting text size
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzscale
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzscale.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzscale.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzscale.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the \includegraphics command to support
tikzpictures. It allows scaling of TikZ images and PGFPlots to
a given width or height without changing the text size.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzscale/tikzscale.sty
%doc %{_texmfdistdir}/doc/latex/tikzscale/3Dplot.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/README
%doc %{_texmfdistdir}/doc/latex/tikzscale/alt.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/histogramNormal.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/invisible.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/linewidth.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/only.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/onslide.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/pause.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/pgfplots-test.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/pgfplots.randn.dat
%doc %{_texmfdistdir}/doc/latex/tikzscale/temporal.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/test-tikzscale.pdf
%doc %{_texmfdistdir}/doc/latex/tikzscale/test-tikzscale.tex
%doc %{_texmfdistdir}/doc/latex/tikzscale/testNode.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/testRectangle.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/testgraphic2D.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/tikzscale-beamer.tex
%doc %{_texmfdistdir}/doc/latex/tikzscale/tikzscale.pdf
%doc %{_texmfdistdir}/doc/latex/tikzscale/uncover.tikz
%doc %{_texmfdistdir}/doc/latex/tikzscale/visible.tikz
#- source
%doc %{_texmfdistdir}/source/latex/tikzscale/tikzscale.dtx
%doc %{_texmfdistdir}/source/latex/tikzscale/tikzscale.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
