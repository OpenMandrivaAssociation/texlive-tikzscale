%global tl_name tikzscale
%global tl_revision 78251

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.6
Release:	%{tl_revision}.1
Summary:	Resize pictures while respecting text size
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzscale
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzscale.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzscale.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzscale.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(xstring)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the \includegraphics command to support
tikzpictures. It allows scaling of TikZ images and PGFPlots to a given
width or height without changing the text size.

