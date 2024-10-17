Name:		texlive-stepgreek
Version:	57074
Release:	2
Summary:	A free Times/Elsevier-style Greek font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stepgreek
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stepgreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stepgreek.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a beta version of the STEP Greek font. Only a regular
face is available at present, though there are plans to add
italic, bold and bold italic in the future. The font only
supports LGR in TeX and is meant to serve as a Greek complement
to a Times-like font such as STEP. The font supports polytonic
Greek.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/stepgreek
%{_texmfdistdir}/fonts/vf/public/stepgreek
%{_texmfdistdir}/fonts/type1/public/stepgreek
%{_texmfdistdir}/fonts/tfm/public/stepgreek
%{_texmfdistdir}/fonts/map/dvips/stepgreek
%{_texmfdistdir}/fonts/enc/dvips/stepgreek
%doc %{_texmfdistdir}/doc/fonts/stepgreek

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
