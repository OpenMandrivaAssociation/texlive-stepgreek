%global tl_name stepgreek
%global tl_revision 57074

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0b1
Release:	%{tl_revision}.1
Summary:	A free Times/Elsevier-style Greek font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/stepgreek
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stepgreek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stepgreek.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a beta version of the STEP Greek font. Only a regular face is
available at present, though there are plans to add italic, bold and
bold italic in the future. The font only supports LGR in TeX and is
meant to serve as a Greek complement to a Times-like font such as STEP.
The font supports polytonic Greek.

