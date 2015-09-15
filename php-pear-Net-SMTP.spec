# remirepo/fedora spec file for php-pear-Net-SMTP
#
# Copyright (c) 2006-2015 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Net_SMTP

Name:           php-pear-Net-SMTP
Version:        1.7.1
Release:        1%{?dist}
Summary:        Provides an implementation of the SMTP protocol
Summary(fr):    Fournit une mise en œuvre du protocole SMTP

Group:          Development/Libraries
License:        PHP
URL:            http://pear.php.net/package/Net_SMTP
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  php-pear

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml
Requires:       php(language) >= 5.4
Requires:       php-pear(PEAR)
Requires:       php-pear(Net_Socket)
Requires:       php-pear(Auth_SASL)
# From phpcompatinfo report for version 1.7.0
Requires:       php-pcre
Requires:       php-openssl

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_smtp) = %{version}


%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

php-pear-Net-SMTP can optionally use package "php-pear-Auth-SASL".

%description -l fr
Fournit une mise en œuvre du protocole SMTP utilisant la classe Net_Socket.

php-pear-Net-SMTP peut optionnellement utiliser
l'extension "php-pear-Auth-SASL".


%prep
%setup -q -c
cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}

%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -Dpm 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml


%check
# Sanity check
lst=$(find %{buildroot}%{pear_phpdir} -exec grep -q %{buildroot} {} \; -print)
[ ! -z "$lst" ] && echo "Reference to BUILDROOT in $lst" && exit 1;

# For documentation purpose only
# After install, as root :
# cd /usr/share/tests/pear/Net_SMTP/tests/
# cp config.php.dist config.php
# vi config.php # you should use a working mail account
# pear run-tests -p Net_SMTP
# Should return 
# 3 PASSED TESTS
# 0 SKIPPED TESTS


%clean
rm -rf %{buildroot}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc %{pear_docdir}/%{pear_name}
%{pear_phpdir}/Net/*
%{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml


%changelog
* Tue Sep  8 2015 Remi Collet <remi@fedoraproject.org> - 1.7.1-1
- update to 1.7.1

* Mon Sep  7 2015 Remi Collet <remi@fedoraproject.org> - 1.7.0-1
- update to 1.7.0
- raise minimum PHP version to 5.4

* Mon Aug  3 2015 Remi Collet <remi@fedoraproject.org> - 1.6.3-1
- Version 1.6.3 (stable) - API 1.2.0 (stable)
- add composer provide
- add spec file license
- add LICENSE file from upstream git repo
- drop generated changelog
- open https://github.com/pear/Net_SMTP/issues/18 - license clarification
- open https://github.com/pear/Net_SMTP/pull/17 - missing License

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul  5 2013 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- Version 1.6.2 (stable) - API 1.2.0 (stable)

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 1.6.1-6
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.6.1-4
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Remi Collet <Fedora@FamilleCollet.com> 1.6.1-1
- Version 1.6.1 (stable) - API 1.2.0 (stable)

* Fri Jun 10 2011 Remi Collet <Fedora@FamilleCollet.com> 1.6.0-1
- Version 1.6.0 (stable) - API 1.2.0 (stable)

* Sun Apr 17 2011 Remi Collet <Fedora@FamilleCollet.com> 1.5.2-1
- Version 1.5.2 (stable) - API 1.1.3 (stable)

* Fri Mar 11 2011 Remi Collet <Fedora@FamilleCollet.com> 1.5.1-1
- Version 1.5.1 (stable) - API 1.1.3 (stable)
- keep doc in pear_docdir

* Sun Feb 13 2011 Remi Collet <Fedora@FamilleCollet.com> 1.5.0-1
- Version 1.5.0 (stable) - API 1.1.3 (stable)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Remi Collet <Fedora@FamilleCollet.com> 1.4.4-1
- Version 1.4.4 (stable) - API 1.1.3 (stable)

* Mon Oct 11 2010 Remi Collet <Fedora@FamilleCollet.com> 1.4.3-1
- Version 1.4.3 (stable) - API 1.1.3 (stable)
- set timezone during build

* Tue Mar 09 2010 Remi Collet <Fedora@FamilleCollet.com> 1.4.2-1
- update to 1.4.2

* Mon Jan 25 2010 Remi Collet <Fedora@FamilleCollet.com> 1.4.1-1
- update to 1.4.1

* Sun Jan 24 2010 Remi Collet <Fedora@FamilleCollet.com> 1.4.0-1
- update to 1.4.0
- add examples to %%doc

* Sun Nov 29 2009 Remi Collet <Fedora@FamilleCollet.com> 1.3.4-1
- update to 1.3.4

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Remi Collet <Fedora@FamilleCollet.com> 1.3.3-1
- update to 1.3.3
- rename Net_SMTP.xml to php-pear-Net-SMTP.xml

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Remi Collet <Fedora@FamilleCollet.com> 1.3.2-1
- update to 1.3.2

* Tue Jun 10 2008 Remi Collet <Fedora@FamilleCollet.com> 1.3.1-1
- update to 1.3.1
- add Comment on howto to run test suite

* Sun Apr 27 2008 Remi Collet <Fedora@FamilleCollet.com> 1.3.0-1
- update to 1.3.0

* Fri Feb 15 2008 Remi Collet <Fedora@FamilleCollet.com> 1.2.11-1
- update to 1.2.11
- fix License

* Sat Mar 31 2007 Remi Collet <Fedora@FamilleCollet.com> 1.2.10-1
- remove PEAR from sumnary
- update to 1.2.10 
- requires Net_Socket >= 1.0.7
- spec cleanup
- add generated CHANGELOG
- don't own /usr/share/pear/Net (already own by Net_Socket)

* Fri Sep 08 2006 Remi Collet <Fedora@FamilleCollet.com> 1.2.8-5
- last template.spec

* Sun Sep 03 2006 Remi Collet <Fedora@FamilleCollet.com> 1.2.8-4
- new and simpler %%prep and %%install

* Sat Sep 02 2006 Remi Collet <Fedora@FamilleCollet.com> 1.2.8-3
- install Licence in prep
- use new macros from /etc/rpm/macros.pear
- own /usr/share/pear/Net
- require php >= 4.0.5

* Sat May 20 2006 Remi Collet <Fedora@FamilleCollet.com> 1.2.8-2
- Require pear >= 1.4.9
- bundle the v3.01 PHP LICENSE file
- use --packagingroot (instead of -R)
- check from install to check (as in php-pear)
- Remove Auth_SASL from Requires (optional)

* Sat May 06 2006 Remi Collet <Fedora@FamilleCollet.com> 1.2.8-1
- spec for extras
- workaround for buggy pear 1.4.6 installer
- use %%{_datadir}/pear/.pkgxml for XML (Bug #190252)

* Thu Apr 06 2006 Remi Collet <rpms@FamilleCollet.com> 1.2.8-3.fc{3,4,5}.remi
- change /var/lib/pear to %%{_libdir}/php/pear for XML (as in extras for FC5)
- spec cleanning

* Sat Mar 04 2006 Remi Collet <RPMS@FamilleCollet.com> 1.2.8-2.fc{3,4}.remi
- add Requires: php-pear(Auth_SASL)

* Sat Feb 25 2006 Remi Collet <RPMS@FamilleCollet.com> 1.2.8-1.fc{3,4}.remi
- update to 1.2.8

* Sat Jan  7 2006 Remi Collet <remi.collet@univ-reims.fr> 1.2.7-1.fc{3,4}.remi
- initial RPM
