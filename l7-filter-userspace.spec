Name:		l7-filter-userspace
Version:	0.12_beta1
Release:	1
Summary:	Userspace version of l7-filter
Group:		System/Base
License:	GPLv2+
URL:		http://l7-filter.sourceforge.net
Source0:	http://download.clearfoundation.com/l7-filter/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libnetfilter_conntrack)
BuildRequires:	pkgconfig(libnetfilter_queue)
Patch0:		l7-filter-userspace-0.11-libnetfilter_conntrack-0.0.100.patch
Patch1:		l7-filter-userspace-0.11-datatype.patch

%description
L7-filter is a packet classifier for Linux. Unlike most other classifiers,
it doesn't just look at simple values such as port numbers but does 
regular expression matching on the application layer data to determine what
protocols are being used. This is a version of l7-filter that works in
userspace instead of the kernel.

%prep
%setup -q -n %{name}-0.12-beta1

%patch1 -p1
%patch0 -p1

%build
%configure2_5x
%make

%install
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/l7-protocols/
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog INSTALL README TODO NEWS THANKS sample-l7-filter.conf
%dir %{_sysconfdir}/l7-protocols/
%{_bindir}/l7-filter
%{_mandir}/man*/l7-filter*
