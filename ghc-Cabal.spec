# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name Cabal

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        1.24.0.0
Release:        1%{?dist}
Summary:        A framework for packaging Haskell software

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-transformers-devel
%endif
# End cabal-rpm deps

%description
The Haskell Common Architecture for Building Applications and Libraries: a
framework defining a common interface for authors to more easily build their
Haskell applications in a portable way.

The Haskell Cabal is part of a larger infrastructure for distributing,
organizing, and cataloging Haskell libraries and tools.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}%{ghc_pkgdocdir}/LICENSE


%check
%if %{with tests}
%cabal test
%endif


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc README.md changelog doc


%changelog
* Tue Mar  1 2016 Jens Petersen <petersen@redhat.com> - 1.24.0.0-1
- update to 1.24.0.0

* Tue Mar  1 2016 Jens Petersen <petersen@redhat.com> - 1.22.7.0-1
- update to 1.22.7.0

* Thu Dec 25 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.3-1
- update to 1.20.0.3

* Wed Jun  4 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.1-1
- update to 1.20.0.1

* Mon Apr 21 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.0-1
- update to 1.20.0.0
- reenable shared, prof, and haddock

* Fri Mar  7 2014 Jens Petersen <petersen@fedoraproject.org> - 1.18.1.3-2
- no base pkg so don't require it!

* Thu Mar  6 2014 Jens Petersen <petersen@fedoraproject.org> - 1.18.1.3-1
- disable shared, prof, and haddock

* Thu Mar  6 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.18.1.3
- spec file generated by cabal-rpm-0.8.10
