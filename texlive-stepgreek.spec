%global tl_name stepgreek
%global tl_revision 57074
%global tl_version 3.0b1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A free Times/Elsevier-style Greek font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/stepgreek
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stepgreek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stepgreek.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This is a beta version of the STEP Greek font. Only a regular face is
available at present, though there are plans to add italic, bold and
bold italic in the future. The font only supports LGR in TeX and is
meant to serve as a Greek complement to a Times-like font such as STEP.
The font supports polytonic Greek.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from stepgreek:
Map STEPGreekTest.map
TL_DROPIN_EOF
