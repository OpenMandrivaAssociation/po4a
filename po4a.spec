Summary:	A tool maintaining translations anywhere
Name:		po4a
Version:	0.44
Release:	2
Group:		System/Internationalization
License:	GPLv2+
URL:		http://alioth.debian.org/projects/po4a/
Source0:	http://alioth.debian.org/frs/download.php/2108/%{name}-%{version}.tar.gz
BuildRequires:	perl(Locale::gettext) >= 1.01
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-SGMLSpm
# FIXME: duplicated in texlive-latex-web-companion
#BuildRequires:	perl(SGMLS) >= 1.03ii
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Text::WrapI18N)
BuildRequires:	perl(Unicode::GCString)
BuildRequires:	perl-devel
BuildRequires:	xsltproc docbook-style-xsl
BuildRequires:	gettext
Requires:	gettext
BuildArch:	noarch

%description
The po4a (po for anything) project goal is to ease translations (and
more interestingly, the maintenance of translations) using gettext
tools on areas where they were not expected like documentation.

%prep
%setup -q

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%doc README* COPYING TODO
%{_bindir}/po4a*
%{_bindir}/msguntypot
%{perl_vendorlib}/Locale/Po4a
%{_mandir}/man[137]/*.[137]*

