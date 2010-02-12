Summary:	A tool maintaining translations anywhere
Name:		po4a
Version:	0.39
Release:	%mkrel 1
Group:		System/Internationalization
License:	GPLv2+
URL:		http://alioth.debian.org/projects/po4a/
Source0:	http://alioth.debian.org/frs/download.php/2108/%{name}-%{version}.tar.gz
BuildRequires:	perl(Locale::gettext) >= 1.01
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SGMLS) >= 1.03ii
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Text::WrapI18N)
BuildRequires:	gettext
Requires:	gettext
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The po4a (po for anything) project goal is to ease translations (and
more interestingly, the maintenance of translations) using gettext
tools on areas where they were not expected like documentation.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}

./Build install destdir=%{buildroot}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README* COPYING TODO
%{_bindir}/po4a*
%{_bindir}/msguntypot
%{perl_vendorlib}/Locale/Po4a
%{_mandir}/man?/*
%lang(ca) %{_mandir}/ca/man?/*
%lang(es) %{_mandir}/es/man?/*
%lang(fr) %{_mandir}/fr/man?/*
%lang(it) %{_mandir}/it/man?/*
%lang(ja) %{_mandir}/ja/man?/*
%lang(pl) %{_mandir}/pl/man?/*
