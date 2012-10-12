%{?scl:%scl_package pcp}
# BZ847916
%global _localstatedir %{_scl_root}/var

Summary: System-level performance monitoring and performance management
Name: %{?scl_prefix}pcp
Version: 3.6.9
%define buildversion 1
Release: %{buildversion}%{?dist}
License: GPLv2
URL: http://oss.sgi.com/projects/pcp
Group: Applications/System
Source0: pcp-%{version}.src.tar.gz
Patch0: pcpqa_service_prefix.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: procps bison flex
BuildRequires: python-devel
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: initscripts man /bin/hostname
 
Requires: bash gawk sed grep fileutils findutils initscripts perl python
Requires: %{?scl_prefix}pcp-libs = %{version}-%{release}
Requires: %{?scl_prefix}python-pcp = %{version}-%{release}
Requires: %{?scl_prefix}perl-PCP-PMDA = %{version}-%{release}
%{?scl:Requires:%scl_runtime}

%define _pmdasdir %{_localstatedir}/lib/pcp/pmdas
%define _testsdir %{_localstatedir}/lib/pcp/testsuite

%description
Performance Co-Pilot (PCP) provides a framework and services to support
system-level performance monitoring and performance management. 

The PCP open source release provides a unifying abstraction for all of
the interesting performance data in a system, and allows client
applications to easily retrieve and process any subset of that data. 

#
# pcp-libs
#
%package libs
License: LGPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot run-time libraries
URL: http://oss.sgi.com/projects/pcp/

%description libs
Performance Co-Pilot (PCP) run-time libraries

#
# pcp-libs-devel
#
%package libs-devel
License: GPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot (PCP) development headers and documentation
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs = %{version}-%{release}

%description libs-devel
Performance Co-Pilot (PCP) headers, documentation and tools for development.

#
# pcp-testsuite
#
%package testsuite
License: GPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot (PCP) test suite
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp = %{version}-%{release}
Requires: %{?scl_prefix}pcp-libs-devel = %{version}-%{release}
# Requires: valgrind

%description testsuite
Quality assurance test suite for Performance Co-Pilot (PCP).

#
# perl-PCP-PMDA. This is the PCP agent perl binding.
#
%package -n %{?scl_prefix}perl-PCP-PMDA
License: GPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot (PCP) Perl bindings and documentation
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}

%description -n %{?scl_prefix}perl-PCP-PMDA
The PCP::PMDA Perl module contains the language bindings for
building Performance Metric Domain Agents (PMDAs) using Perl.
Each PMDA exports performance data for one specific domain, for
example the operating system kernel, Cisco routers, a database,
an application, etc.

#
# perl-PCP-MMV
#
%package -n %{?scl_prefix}perl-PCP-MMV
License: GPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot (PCP) Perl bindings for PCP Memory Mapped Values
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}

%description -n %{?scl_prefix}perl-PCP-MMV
The PCP::MMV module contains the Perl language bindings for
building scripts instrumented with the Performance Co-Pilot
(PCP) Memory Mapped Value (MMV) mechanism.
This mechanism allows arbitrary values to be exported from an
instrumented script into the PCP infrastructure for monitoring
and analysis with pmchart, pmie, pmlogger and other PCP tools.

#
# perl-PCP-LogImport
#
%package -n %{?scl_prefix}perl-PCP-LogImport
License: GPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot (PCP) Perl bindings for importing external data into PCP archives
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}

%description -n %{?scl_prefix}perl-PCP-LogImport
The PCP::LogImport module contains the Perl language bindings for
importing data in various 3rd party formats into PCP archives so
they can be replayed with standard PCP monitoring tools.

 #
# perl-PCP-LogSummary
#
%package -n %{?scl_prefix}perl-PCP-LogSummary
License: GPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot (PCP) Perl bindings for post-processing output of pmlogsummary
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}

%description -n %{?scl_prefix}perl-PCP-LogSummary
The PCP::LogSummary module provides a Perl module for using the
statistical summary data produced by the Performance Co-Pilot
pmlogsummary utility.  This utility produces various averages,
minima, maxima, and other calculations based on the performance
data stored in a PCP archive.  The Perl interface is ideal for
exporting this data into third-party tools (e.g. spreadsheets).

#
# pcp-import-sar2pcp
#
%package import-sar2pcp
License: LGPLv2+
Group: Applications/System
Summary: Performance Co-Pilot tools for importing sar data into PCP archive logs
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}
Requires: %{?scl_prefix}perl-PCP-LogImport >= %{version}
Requires: sysstat

%description import-sar2pcp
Performance Co-Pilot (PCP) front-end tools for importing sar data
into standard PCP archive logs for replay with any PCP monitoring tool.

#
# pcp-import-iostat2pcp
#
%package import-iostat2pcp
License: LGPLv2+
Group: Applications/System
Summary: Performance Co-Pilot tools for importing iostat data into PCP archive logs
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}
Requires: %{?scl_prefix}perl-PCP-LogImport >= %{version}
Requires: sysstat

%description import-iostat2pcp
Performance Co-Pilot (PCP) front-end tools for importing iostat data
into standard PCP archive logs for replay with any PCP monitoring tool.

#
# pcp-import-mrtg2pcp
#
%package import-mrtg2pcp
License: LGPLv2+
Group: Applications/System
Summary: Performance Co-Pilot tools for importing MTRG data into PCP archive logs
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}
Requires: %{?scl_prefix}perl-PCP-LogImport >= %{version}

%description import-mrtg2pcp
Performance Co-Pilot (PCP) front-end tools for importing MTRG data
into standard PCP archive logs for replay with any PCP monitoring tool.

#
# python-pcp. This is the PCP library bindings for python.
#
%package -n %{?scl_prefix}python-pcp
License: GPLv2
Group: Development/Libraries
Summary: Performance Co-Pilot (PCP) Python bindings and documentation
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp-libs >= %{version}-%{release}

%description -n %{?scl_prefix}python-pcp
The python PCP module contains the language bindings for
building Performance Metric API (PMAPI) tools using Python.

%package scl-initscripts
License: LGPLv2+
Group: Applications/System
Summary: Performance Co-Pilot /etc/rc.d/init.d initscripts
URL: http://oss.sgi.com/projects/pcp/
Requires: %{?scl_prefix}pcp

%description scl-initscripts
Software Collection-compatible initscript wrappers for PCP daemons.

%prep
%setup -q %{?scl:-n %{pkg_name}-%{version}}
%patch0 -p1 -b .pcpqa

%clean
rm -Rf $RPM_BUILD_ROOT

%build
# TODO: --disable-shared (847911, 856651)
%configure --with-rcdir=%{_sysconfdir}/rc.d/init.d --with-docdir=%{_docdir}/%{name}-%{version}
make default_pcp

%install
rm -Rf $RPM_BUILD_ROOT
export DIST_ROOT=$RPM_BUILD_ROOT
make install_pcp

# Fix stuff we do/don't want to ship
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a	# TODO: keep when --disable-shared?
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/run/pcp

# remove sheet2pcp until BZ 830923 and BZ 754678 are resolved.
rm -f $RPM_BUILD_ROOT/%{_bindir}/sheet2pcp $RPM_BUILD_ROOT/%{_mandir}/man1/sheet2pcp.1*

# default chkconfig off for Fedora and RHEL
for f in $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/{pcp,pmcd,pmlogger,pmie,pmproxy}; do
	sed -i -e '/^# chkconfig/s/:.*$/: - 95 05/' -e '/^# Default-Start:/s/:.*$/:/' $f
done

# create dummy /etc/init.d/ files for scl packaging 
for f in $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/{pcp,pmcd,pmlogger,pmie,pmproxy}; do
    daemon=`basename $f`
    initfile=$RPM_BUILD_ROOT%{_root_sysconfdir}/rc.d/init.d/%{?scl_prefix}$daemon
    mkdir -p `dirname $initfile`
    rm -f $initfile
    sed -n '/BEGIN INIT INFO/,/END INIT INFO/p' < $f > $initfile
    # NB: there is no use setting environment variables here; /sbin/service runs things with env -i
    echo 'echo %{_sysconfdir}/rc.d/init.d/'$daemon' "$@" | scl enable %{scl} -' >> $initfile
    chmod 755 $initfile
done


# list of PMDAs in the base pkg
ls -1 $RPM_BUILD_ROOT/%{_pmdasdir} | egrep -v 'simple|sample|trivial|txmon' |\
sed -e 's#^#'%{_pmdasdir}'\/#' >base_pmdas.list

# bin and man1 files except those split out into sub packages
ls -1 $RPM_BUILD_ROOT/%{_bindir} | grep -v '2pcp' |\
sed -e 's#^#'%{_bindir}'\/#' >base_binfiles.list
ls -1 $RPM_BUILD_ROOT/%{_mandir}/man1 | grep -v '2pcp' |\
sed -e 's#^#'%{_mandir}'\/man1\/#' >base_man1files.list

cat base_pmdas.list base_binfiles.list base_man1files.list > base_specialfiles.list

# compress man pages that may be skipped by normal brp-compress (bz844028)
find $RPM_BUILD_ROOT/%{_mandir}/man3 -name '*.3pm' | xargs -r gzip -n


%files scl-initscripts
%{_root_sysconfdir}/rc.d/init.d/*

%preun scl-initscripts
if [ "$1" -eq 0 ]
then
    #
    # Stop daemons before erasing the package
    #
    /sbin/service %{?scl_prefix}pmlogger stop >/dev/null 2>&1
    /sbin/service %{?scl_prefix}pmie stop >/dev/null 2>&1
    /sbin/service %{?scl_prefix}pmproxy stop >/dev/null 2>&1
    /sbin/service %{?scl_prefix}pcp stop >/dev/null 2>&1
    /sbin/service %{?scl_prefix}pmcd stop >/dev/null 2>&1

    /sbin/chkconfig --del %{?scl_prefix}pcp >/dev/null 2>&1
    /sbin/chkconfig --del %{?scl_prefix}pmcd >/dev/null 2>&1
    /sbin/chkconfig --del %{?scl_prefix}pmlogger >/dev/null 2>&1
    /sbin/chkconfig --del %{?scl_prefix}pmie >/dev/null 2>&1
    /sbin/chkconfig --del %{?scl_prefix}pmproxy >/dev/null 2>&1
fi

%post %{?scl:scl-initscripts}
/sbin/chkconfig --add %{?scl_prefix}pmcd >/dev/null 2>&1
/sbin/service %{?scl_prefix}pmcd condrestart
/sbin/chkconfig --add %{?scl_prefix}pmlogger >/dev/null 2>&1
/sbin/service %{?scl_prefix}pmlogger condrestart
/sbin/chkconfig --add %{?scl_prefix}pmie >/dev/null 2>&1
/sbin/service %{?scl_prefix}pmie condrestart
/sbin/chkconfig --add%{?scl_prefix} pmproxy >/dev/null 2>&1
/sbin/service %{?scl_prefix}pmproxy condrestart

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%pre testsuite
getent group pcpqa >/dev/null || groupadd -r pcpqa
getent passwd pcpqa >/dev/null || useradd -c "PCP Quality Assurance" -g pcpqa -m -r -s /bin/bash pcpqa 2>/dev/null
exit 0

%files testsuite
%defattr(-,pcpqa,pcpqa)
%{_testsdir}

%files -n %{?scl_prefix}python-pcp
%defattr(-,root,root)
%{_libdir}/python*/site-packages/*

%files -f base_specialfiles.list
#
# Note: there are some headers (e.g. domain.h) and in a few cases some
# C source files that rpmlint complains about. These are not devel files,
# but rather they are (slightly obscure) PMDA config files.
#
%defattr(-,root,root)
%doc CHANGELOG COPYING INSTALL README VERSION.pcp pcp.lsm

%dir %{_pmdasdir}
%dir %{_datadir}/pcp
%dir %{_localstatedir}/run/pcp
%dir %{_localstatedir}/lib/pcp
%dir %{_localstatedir}/lib/pcp/config

%{_libexecdir}/pcp
%{_datadir}/pcp/lib
%{_localstatedir}/log/pcp
%{_localstatedir}/lib/pcp/pmns
%ghost %{_localstatedir}/lib/pcp/pmns/.NeedRebuild
%{_initrddir}/pcp
%{_initrddir}/pmcd
%{_initrddir}/pmlogger
%{_initrddir}/pmie
%{_initrddir}/pmproxy
%{_mandir}/man4/*
%config %{_sysconfdir}/bash_completion.d/pcp
%config %{_sysconfdir}/pcp.env
%config %{_sysconfdir}/pcp.sh
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmcd/pmcd.conf
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmcd/pmcd.options
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmcd/rc.local
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmie/config.default
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmie/control
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmie/crontab
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmlogger/config.default
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmlogger/control
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmlogger/crontab
%config(noreplace) %{_localstatedir}/lib/pcp/config/pmproxy/pmproxy.options
%{_localstatedir}/lib/pcp/config/*

%files libs
%defattr(-,root,root)

%dir %{_includedir}/pcp
%{_includedir}/pcp/builddefs
%{_includedir}/pcp/buildrules
%config %{_sysconfdir}/pcp.conf

%files libs-devel
%defattr(-,root,root)

%{_includedir}/pcp/*.h
%{_mandir}/man3/*
#%{_libdir}/*.a		# TODO: need static libs when --disable-shared?
%{_datadir}/pcp/demos
%{_datadir}/pcp/examples

# PMDAs that ship src and are not for production use
# straight out-of-the-box, for devel or QA use only.
%{_localstatedir}/lib/pcp/pmdas/simple
%{_localstatedir}/lib/pcp/pmdas/sample
%{_localstatedir}/lib/pcp/pmdas/trivial
%{_localstatedir}/lib/pcp/pmdas/txmon

%files import-sar2pcp
%defattr(-,root,root)
%{_bindir}/sar2pcp
%{_mandir}/man1/sar2pcp.*

%files import-iostat2pcp
%defattr(-,root,root)
%{_bindir}/iostat2pcp
%{_mandir}/man1/iostat2pcp.*

%files import-mrtg2pcp
%defattr(-,root,root)
%{_bindir}/mrtg2pcp
%{_mandir}/man1/mrtg2pcp.*

%files -n %{?scl_prefix}perl-PCP-PMDA -f perl-pcp-pmda.list
%defattr(-,root,root)

%files -n %{?scl_prefix}perl-PCP-MMV -f perl-pcp-mmv.list
%defattr(-,root,root)

%files -n %{?scl_prefix}perl-PCP-LogImport -f perl-pcp-logimport.list
%defattr(-,root,root)

%files -n %{?scl_prefix}perl-PCP-LogSummary -f perl-pcp-logsummary.list
%defattr(-,root,root)

%changelog
* Fri Oct 12 2012 Nathan Scott <nathans@redhat.com> - 3.6.9-1
- Update to latest PCP sources.
- Rebase for next DTS beta release (BZ 857773)
- Remove unused pmcollectl arguments (BZ 863210)

* Fri Sep 14 2012 Nathan Scott <nathans@redhat.com> - 3.6.8-1
- Update to latest PCP sources.
- Make use of the new --disable-shared configure option (BZ 856651)

* Mon Sep 10 2012 Frank Ch. Eigler <fche@redhat.com> - 3.6.6-2
- Bumped release number

* Fri Sep 07 2012 Nathan Scott <nathans@redhat.com> - 3.6.6-1.1
- Move configure step from prep to build section of spec (BZ 854128)
- Add %ghost to handle the .NeedRebuild build leftover (BZ 850359)
- Merge in further spec work from fedora/rawhide.

* Wed Aug 28 2012 Frank Ch. Eigler <fche@redhat.com> - 3.6.6-1
- Update to official PCP 3.6.6-1 sources.
- Adopt more spec patterns from fedora/rawhide.

* Fri Aug 24 2012 Frank Ch. Eigler <fche@redhat.com> - 3.6.6-0.3
- Switch pcpqa files' ownership.

* Fri Aug 24 2012 Frank Ch. Eigler <fche@redhat.com> - 3.6.6-0.2
- Update to 3.6.5-1-1253-ga93aa22 snapshot, add pcpqa_service_prefix.patch.

* Fri Aug 17 2012 Frank Ch. Eigler <fche@redhat.com> - 3.6.6-0.1
- Update to latest PCP sources, creates a new testsuite package.

* Fri Jul 27 2012 Frank Ch. Eigler <fche@redhat.com> - 3.6.5-0.3
- include -scl-initscripts subrpm

* Fri Jul 27 2012 Frank Ch. Eigler <fche@redhat.com> - 3.6.5-0.2
- scl trial build of a snapshot of pcpfans.git fche/prefix branch

* Thu Jul 19 2012 Mark Goodwin <mgoodwin@redhat.com>
- pmcd and pmlogger services are not supposed to be enabled by default (BZ 840763) - 3.6.3-1.3

* Thu Jun 21 2012 Mark Goodwin <mgoodwin@redhat.com>
- remove pcp-import-sheet2pcp subpackage due to missing deps (BZ 830923) - 3.6.3-1.2

* Fri May 18 2012 Dan Hork <dan[at]danny.cz> - 3.6.3-1.1
- fix build on s390x

* Mon Apr 30 2012 Mark Goodwin - 3.6.3-1
- Update to latest PCP sources

* Thu Apr 26 2012 Mark Goodwin - 3.6.2-1
- Update to latest PCP sources

* Thu Apr 12 2012 Mark Goodwin - 3.6.1-1
- Update to latest PCP sources

* Thu Mar 22 2012 Mark Goodwin - 3.6.0-1
- use %configure macro for correct libdir logic
- update to latest PCP sources

* Thu Dec 15 2011 Mark Goodwin - 3.5.11-2
- patched configure.in for libdir=/usr/lib64 on ppc64

* Thu Dec 01 2011 Mark Goodwin - 3.5.11-1
- Update to latest PCP sources.

* Fri Nov 04 2011 Mark Goodwin - 3.5.10-1
- Update to latest PCP sources.

* Mon Oct 24 2011 Mark Goodwin - 3.5.9-1
- Update to latest PCP sources.

* Mon Aug 8 2011 Mark Goodwin - 3.5.8-1
- Update to latest PCP sources.

* Fri Aug 5 2011 Mark Goodwin - 3.5.7-1
- Update to latest PCP sources.

* Fri Jul 22 2011 Mark Goodwin - 3.5.6-1
- Update to latest PCP sources.

* Tue Jul 19 2011 Mark Goodwin - 3.5.5-1
- Update to latest PCP sources.

* Wed Feb 3 2011 Mark Goodwin - 3.5.0-1
- Update to latest PCP sources.

* Thu Sep 30 2010 Mark Goodwin - 3.4.0-1
- Update to latest PCP sources.

* Fri Jul 16 2010 Mark Goodwin - 3.3.3-1
- Update to latest PCP sources.

* Sat Jul 10 2010 Mark Goodwin - 3.3.2-1
- Update to latest PCP sources.

* Tue Jun 29 2010 Mark Goodwin - 3.3.1-1
- Update to latest PCP sources.

* Fri Jun 25 2010 Mark Goodwin - 3.3.0-1
- Update to latest PCP sources.

* Thu Mar 18 2010 Mark Goodwin - 3.1.2-1
- Update to latest PCP sources.

* Wed Jan 27 2010 Mark Goodwin - 3.1.0-1
- BuildRequires: initscripts for %{_vendor} == redhat.

* Thu Dec 10 2009 Mark Goodwin - 3.0.3-1
- BuildRequires: initscripts for FC12.

* Wed Dec 02 2009 Mark Goodwin - 3.0.2-1
- Added sysfs.kernel metrics, rebased to minor community release.

* Mon Oct 19 2009 Martin Hicks <mort@sgi.com> - 3.0.1-2
- Remove IB dependencies.  The Infiniband PMDA is being moved to
  a stand-alone package.
- Move cluster PMDA to a stand-alone package.

* Fri Oct 9 2009 Mark Goodwin <mgoodwin@redhat.com> - 3.0.0-9
- This is the initial import for Fedora
- See 3.0.0 details in CHANGELOG
